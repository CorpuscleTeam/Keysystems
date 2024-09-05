console.log('cur_main_5_3.js')

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

let modalApplicationStatus = document.createElement('div')
modalApplicationStatus.setAttribute('id', 'statusOrder')
modalApplicationStatus.classList.add('modal')

let modalApplicationStatusContent = document.createElement('div')
modalApplicationStatusContent.classList.add('modal-content')
modalApplicationStatus.appendChild(modalApplicationStatusContent)

document.body.append(modalApplicationStatus)
console.log('должно создатьс модальное окно')

// МО добавить новых кураторов

let modalAddCurator = document.createElement('div')
modalAddCurator.setAttribute('id', 'modal_add_curator')
modalAddCurator.classList.add('modal')
// все что в МО заполняется через function modalAddCurators()
document.body.append(modalAddCurator)

// МО вернуть в работу (клиент)

let moBackToWork = document.createElement('div')
moBackToWork.classList.add('modal')
moBackToWork.setAttribute('id', 'modalBackToWork')
// заполняется в function modalBackToWork()
document.body.append(moBackToWork)

// обработчик событий данные с бэка

document.querySelectorAll('.modal_cr_order').forEach(link => {

    link.addEventListener('click', function () {
        let orderId = this.getAttribute('data-order-id');

        // Здесь делаем запрос на бэк с использованием Fetch API
        fetch(`/order-data/${orderId}`)
            .then(response => response.json())
            .then(data => {

                console.log(data)
                if (data.client_chat.length > 0) {
                    window.lastMsgForClientChat = data.client_chat[data.client_chat.length - 1].from_user.id;
                } else {
                    window.lastMsgForClientChat = null;
                }

                if (data.curator_chat.length > 0) {
                    window.lastMsgForClientChat = data.curator_chat[data.curator_chat.length - 1].from_user.id;
                } else {
                    window.lastMsgForClientChat = null;
                }

                window.selectedTab = '#tab1'
                window.orderId = orderId
                window.userId = data.user_id
                window.roomName = data.room
                window.mgtOrder = isMyOrder(data.order.curators)

                //                создаём переменную для сокета
                // создаём переменную для сокета
                window.chatSocket = 'null';

                // Заполняем модальное окно данными из `data`
                modalApplicationStatusContent.innerHTML = `
                    <div class="modal1_img modal-close">
                        <img src="${imgLink}" alt="">
                    </div>
                    <h5>${data.order.customer.title}</h5>
                    <div id="mark_status"></div>
                    <ul class="tabs">
                        <li class="tab"><a href="#tab1">Описание</a></li>
                        <li class="tab">
                            <a href="#tab2" id="id_client_chat">
                                <div class="order_tab chat_tab">Комментарии</div>

                            </a>
                        </li>
                        <li class="tab">
                            <a href="#tab3"  id="id_curator_chat">
                                <div class="order_tab chat_tab">Чат кураторов</div>

                            </a>
                        </li>
                    </ul>

                    <div id="tab1" class="tab-content active">
                        <h6 class="title_in_modal">Тема</h6>
                        <div class="text_in_modal">${data.order.topic.topic}</div>
                        <form action="" method="post">
                            <div class="select_PO">
                                <label class="title_in_modal" for="soft_in_chat">Програмное обеспечение</label>
                                <select name="soft_in_chat" id="soft_in_chat">
                                </select>
                            </div>
                        </form>
                        <h6 class="title_in_modal">Описание</h6>
                        <div class="text_in_modal">${data.order.text}</div>
                        <div class="files_in_modal"></div>
                        <h6 class="title_in_modal title_of_curators_request">Исполнители</h6>
                        <div class="curators_of_request"></div>
                        <div id="btn_mark_status"></div>

                    </div>
                    
                    <div id="tab2" class="tab-content">
                        <div class="client_chat chat_flex">
                                <div id="client_chat" cols="100" rows="20" class="chat_area"></div>
                            <div class="footer_message">
                                <input id="client-msg-input" class="chat-message-input" type="text" size="100">
                                <div>
                                    <input id="client-msg-file" name="client-msg-file" class="chat_add_file" type="file" multiple style="display: none;">
                                        <label for="client-msg-file" class="chat_add_file">
                                        <img src="${addFile2}" alt="">
                                    </label>
                                </div>
                                <div>
                                    <input id="client-msg-submit" name="client-msg-submit" class="chat_submit" type="button" value="Send" style="display: none;">
                                        <label for="client-msg-submit" class="chat_submit">
                                        <img src="${sentMsg}" alt="">
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div id="tab3" class="tab-content">
                        <div class="curator_chat chat_flex">
                            <div id="curator_chat" cols="100" rows="20" class="chat_area"></div>
                            <div class="footer_message">
                                <input id="curator-msg-input" name="curator-msg-input" class="chat-message-input" type="text" size="100">
                                <div>
                                    <input id="curator-msg-file" name="curator-msg-file" class="chat_add_file" type="file" multiple style="display: none;">
                                    <label for="curator-msg-file" class="chat_add_file">
                                        <img src="${addFile2}" alt="">
                                    </label>
                                </div>
                                <div>
                                    <input id="curator-msg-submit" name="curator-msg-submit" class="chat_submit" type="button" value="Send" style="display: none;">
                                        <label for="curator-msg-submit" class="chat_submit">
                                        <img src="${sentMsg}" alt="">
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                `;

                // Инициализация вкладок Materialize
                let tabs = document.querySelectorAll('.tabs');
                M.Tabs.init(tabs);

                // Открываем модальное окно
                M.Modal.getInstance(modalApplicationStatus).open();
                // M.Modal.getInstance(modalAddCurator).open();



                // отображение вкладки "чат кураторов"
                if (curatorUser == false) {
                    let tabCuratorChat = document.querySelector('.tabs>li:nth-child(3)')

                    if (tabCuratorChat) {
                        tabCuratorChat.style.display = "none"
                    }
                }

                // список ПО
                if (curatorUser == false) {
                    let selectPOClientTab = document.querySelector('.select_PO select')
                    selectPOClientTab.style.display = "none"

                    let textPOClientTab = document.createElement('p')
                    textPOClientTab.classList.add('text_in_modal')
                    textPOClientTab.innerHTML = data['order']['soft']['title']
                    document.querySelector('.select_PO').appendChild(textPOClientTab)
                } else {
                    selectPO('#soft_in_chat', data['soft'], data.order.soft.title)
                }


                // кнопка скачать файл
                btnLdFile('.files_in_modal', data['order']['files'])

                // исполнители
                if (curatorUser == true) {
                    createCuratorsList('.curators_of_request', data['order']['curators'], data['order']['status'])
                } else {
                    let titleOfCuratorsList = document.querySelector('.title_of_curators_request')
                    titleOfCuratorsList.style.display = "none"
                }

                // список кураторов
                if (curatorUser == true) {
                    modalAddCurators('.curator_item_right')
                    modalAddCurators('.btn_add_curator')
                }

                // отображение статуса заявки (+кнопка в первой вкладке)
                status_btn(data.order.status)

                modalBackToWork()

                // !!_проперить надо ли?
                let client_chat = createChat('#client_chat', data.client_chat, data.user_id, BASE.CLIENT)

                // !!_проперить надо ли?
                let curator_chat = createChat('#curator_chat', data.curator_chat, data.user_id, BASE.CURATOR)

                // вкладки
                document.querySelectorAll('.tabs .tab a').forEach(tabLink => {
                    tabLink.addEventListener('click', function (event) {
                        event.preventDefault();

                        // Показываем контент для выбранной вкладки
                        const selectedTab = this.getAttribute('href');
                        window.selectedTab = selectedTab

                        // вернуться позже сюда!!!
                        if (selectedTab == '#tab2') {
                            let chat = document.querySelector('#client_chat_item')
                            if (chat) {
                                chat.scrollTop = chat.scrollHeight
                            }

                        }

                        // Логируем ID открытой вкладки
                        console.log('Открыта вкладка:', selectedTab);
                    });
                });

                notice('id_client_chat', data['unv_msg_client'])
                notice('id_curator_chat', data['unv_msg_curator'])



                // btn_mark_status (data['order']['status'])

                // !!_вернуться к этому!!
                // if (curatorUser == true) {
                //     if (data['order']['status'] == 'new') {
                //         // changeStatusNewToWork()
                //         // data['order']['status'] = 'active'
                //     } else if (data['order']['status'] == 'active') {
                //         let btnElem = document.querySelector('.btn_work_req')
                //         let statusElem = document.querySelector('.status_work_req')
                //         btnElem.addEventListener('click', function () {
                //             changeStatusWorkToEnd(btnElem, statusElem)
                //         })
                //     }
                // } else {
                //     noBtnNewReq ()
                //     if (data['order']['status'] == 'done') {
                //         btnBackReq ()
                //         modalBackToWork ()
                //     }

                // }
                // modalBackToWork ()


                // сокет. оставляем последним
                initOrderSocket(data.room, data.user_id)
            })
            .catch(error => console.error('Error:', error));
    });
});


