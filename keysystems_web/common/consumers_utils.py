from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


import os
import base64
import logging

from . import models as m
from .serializers import MessageSerializer
from .logs import log_error
from enums import EditOrderAction, MsgType, NoticeType, notices_dict, CountSelector, ChatType, OrderStatus, TAB, soft_dict


# список всех относящихся к заказу пользователей
def get_related_users_list(order: m.Order, chat: str = ChatType.CLIENT.value) -> list[int]:
    curators = m.OrderCurator.objects.select_related('user').filter(order=order).all()
    if chat == ChatType.CLIENT:
        return [curator.user.id for curator in curators] + [order.from_user.id]
    else:
        return [curator.user.id for curator in curators]


# обработка входящего сообщения
def ws_proc_msg(msg_data: dict, ws_consumer: WebsocketConsumer):
    user_id = int(msg_data['user_id'])
    order_id = int(msg_data['order_id'])

    user = m.UserKS.objects.filter(id=user_id).first()
    # log_error(wt=False, message=f'user: {user}\n')
    if user:
        order = m.Order.objects.select_related('from_user').filter(id=order_id).first()

        # сохраняем сообщение
        if msg_data['event'] == EditOrderAction.MSG:
            new_message = m.Message(
                type_msg=MsgType.MSG.value,
                from_user=user,
                chat=msg_data['chat'],
                order_id=order_id,
                text=msg_data['message']
            )
            new_message.save()

        else:
            # создаём путь к папке и саму папку
            folder_path = os.path.join('media', 'msg_files', str(msg_data['order_id']), str(msg_data['user_id']))
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_path = os.path.join(folder_path, msg_data['file_name'])
            new_message = m.Message(
                type_msg=MsgType.FILE.value,
                from_user=user,
                chat=msg_data['chat'],
                order_id=int(msg_data['order_id']),
                file_path=file_path,
                file_size=msg_data['file_size'],

            )
            new_message.save()
            # сохраняем файл
            file_data = base64.b64decode(msg_data['file_data'])
            with open(file_path, 'wb') as f:
                f.write(file_data)

        # рассылаем уведомления
        notice_list = get_related_users_list(order=order, chat=msg_data['chat'])
        if msg_data['user_id'] in notice_list:
            notice_list.remove(msg_data['user_id'])

        notice: str = notices_dict.get(NoticeType.NEW_MSG.value)
        notice_text = notice.format(pk=order.id)
        log_error(f'user_ids: {notice_list}', wt=False)

        for user_id in notice_list:
            new_notice = m.Notice(
                order=order,
                user_ks_id=user_id,
                text=notice_text
            )
            new_notice.save()

            # обновляем циферки
            async_to_sync(ws_consumer.channel_layer.group_send)(
                f'user{user_id}',  # Имя группы
                # f'user5',  # Имя группы
                {
                    'type': 'update.counter',  # Это соответствует методу 'counter' в UserConsumer
                    'add': 1,
                    'selector': CountSelector.PUSH.value
                }
            )

        # отправляем сообщение
        async_to_sync(ws_consumer.channel_layer.group_send)(
            ws_consumer.room_group_name, {
                "type": "chat.message",
                'data': MessageSerializer(new_message).data,
            }
        )


# {'event': 'edit_curator', 'add': '2', 'del': 5, 'order_id': '10', 'room_name': 'order10'}
# обработка изменения списка кураторов
def ws_proc_curator(event_data: dict, ws_consumer: WebsocketConsumer):
    order_id = int(event_data.get('order_id', 0))

    # если есть кого добавить
    if event_data.get('add'):
        add_user_id = int(event_data.get('add', 0))
        # можно убрать
        curator = m.OrderCurator.objects.filter(order_id=order_id, user_id=add_user_id).first()
        if add_user_id and not curator:
            m.OrderCurator.objects.create(order_id=order_id, user_id=add_user_id)
            # logging.warning(f'Добавил: {add_user_id}')

    # если есть кого удалить
    if event_data.get('del'):
        del_user_id = int(event_data.get('del', 0))
        m.OrderCurator.objects.filter(order_id=order_id, user_id=del_user_id).delete()
        # logging.warning(f'Удалил: {del_user_id}')

    async_to_sync(ws_consumer.channel_layer.group_send)(
        ws_consumer.room_group_name, {"type": "curator.list", 'order_id': order_id}
    )


# обработка смены статуса
def ws_proc_status(event_data: dict, ws_consumer: WebsocketConsumer):
    user_id = int(event_data.get('user_id', 0))
    order_id = int(event_data['order_id'])

    order = m.Order.objects.filter(id=order_id).first()
    order.status = event_data['status']
    order.save()

    # пишем коммент, если есть
    comment = event_data.get('comment')
    # log_error(comment, wt=False)
    add_counter_ws = -1
    if comment:
        # сохраняем сообщение
        new_message = m.Message(
            type_msg=MsgType.MSG.value,
            from_user_id=user_id,
            chat=ChatType.CLIENT.value,
            order_id=order_id,
            text=comment
        )
        new_message.save()
        add_counter_ws = 1

    ws_send_list = get_related_users_list(order=order)

    notice_type = NoticeType.ORDER_DONE.value if event_data['status'] == OrderStatus.DONE else NoticeType.ORDER_ACTIVE.value
    notice_text: str = notices_dict.get(notice_type).format(pk=order.id)
    # notice_text = notice.format(pk=order.id)
    for user in ws_send_list:
        # new_notice = m.Notice(order=order, user_ks_id=user, text=notice_text)
        m.Notice.objects.create(order=order, user_ks_id=user, text=notice_text)
        async_to_sync(ws_consumer.channel_layer.group_send)(
            f'user{user}',
            {
                'type': 'order.status',
                'order_id': order_id,
                'status': event_data['status']
            }
        )

    # если заказ закрыт отнимает у всех циферку
    log_error(f'ws_send_list: {ws_send_list} {event_data["status"]} {add_counter_ws}')
    if event_data['status'] == OrderStatus.DONE or add_counter_ws == 1:
        for user in ws_send_list:
            async_to_sync(ws_consumer.channel_layer.group_send)(
                f'user{user}',
                {
                    'type': 'update.counter',
                    'add': add_counter_ws,
                    'selector': CountSelector.REQUEST.value
                }
            )

    async_to_sync(ws_consumer.channel_layer.group_send)(
        ws_consumer.room_group_name, {"type": "select.status", 'status': event_data['status']}
    )


# отмечает сообщения в чате как просмотренные
def ws_proc_view_msg(event_data: dict, ws_consumer: WebsocketConsumer):
    order_id = int(event_data['order_id'])
    user_id = int(event_data['user_id'])
    tab = event_data['tab']
    chat = ChatType.CLIENT.value if tab == TAB.TAB2 else ChatType.CURATOR.value

    # log_error(f'tab: {tab}\norder_id: {order_id}\nuser_id: {user_id}\n', wt=False)

    viewed_msgs = m.Message.objects.filter(chat=chat, order_id=order_id).all()
    # log_error(f'viewed_msgs: {len(viewed_msgs)}', wt=False)
    for msg in viewed_msgs:
        m.ViewMessage.objects.create(message=msg, user_ks_id=user_id)


# изменяет выбор софта
def ws_proc_soft(event_data: dict, ws_consumer: WebsocketConsumer):
    order_id = int(event_data['order_id'])
    soft = event_data['soft_id']

    order = m.Order.objects.filter(id=order_id).first()
    order.soft = soft
    order.save()

    async_to_sync(ws_consumer.channel_layer.group_send)(
        ws_consumer.room_group_name, {"type": "edit.soft", 'soft_id': soft, 'soft_name': event_data['soft_name']}
    )
    # обновляем поле заказа
    ws_send_list = get_related_users_list(order)
    log_error(f'add_new_order: {type(ws_consumer)} {ws_consumer}', wt=False)

    for user in ws_send_list:
        async_to_sync(ws_consumer.channel_layer.group_send)(
            f'user{user}',
            {
                'type': 'order.soft',
                'order_id': order_id,
                'soft': soft,
                'soft_title': soft_dict.get(soft, 'Обновлено'),

            }
        )


def add_new_order(event_data: dict, ws_consumer: WebsocketConsumer):
    user_list = get_related_users_list(event_data['order'])
    if event_data['user_id'] in user_list:
        user_list.remove(event_data['user_id'])

    log_error(f'add_new_order: {type(ws_consumer)} {ws_consumer}', wt=False)
    for user_id in user_list:
        # добавляем заказ
        async_to_sync(ws_consumer.channel_layer.group_send)(
            f'user{user_id}',  # Имя группы
            {
                'type': 'order.add',  # Это соответствует методу 'counter' в UserConsumer
                'order': event_data['order'],
            }
        )