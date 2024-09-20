

// создание сокета и все с ним функции
function initUserSocket(userId) {
    roomName = `user${userId}`

    window.chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/user/'
        + roomName
        + '/'
    );

    console.log(`Приконнектились! ${roomName} ${userId}`)

    // получение сообщений
    window.chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        console.log('Новый сокет')
        console.log(data)

        // обновлем счётчики
        if (data.type == 'count_update') {
            count_notice(data.selector, data.add)
        }

        // обновляем поле заказа
        else if (data.type == 'order_status') {
            let wsOrderId = parseInt(data.order_id)
            let orderDataUpdated = false

            for (let i = 0; i < card_orders.length; i++) {
                if (card_orders[i].id == wsOrderId) {
                    card_orders[i].status = data.status
                    orderDataUpdated = true
                    break
                }
            }
            if (orderDataUpdated) {
                createOrdersArea(card_orders)
            }


        }

    }

    window.chatSocket.onclose = function (e) {
        console.log('Мы закрылись');
    };


};




initUserSocket(userId = mainData.user_id)