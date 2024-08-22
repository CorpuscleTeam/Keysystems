console.log('cur_main_5_3.js')
/* 
{
    "order": {
        "id": 4,
        "from_user": {
            "id": 3,
            "full_name": "as df gh",
            "username": "grudoav@gmail.com"
        },
        "customer": {
            "id": 1,
            "inn": 1234567890,
            "district": {
                "title": "Верхнеколымский район"
            },
            "title": "ООО plastic world"
        },
        "text": "Учет поступления платежей в бюджет",
        "soft": {
            "id": 1,
            "title": "ПО 1",
            "description": "Описание ПО 1",
            "is_active": true
        },
        "topic": {
            "id": 1,
            "topic": "Сломалос(",
            "is_active": true
        },
        "status": "new",
        "id_str": "#00004",
        "order_curators": [
            {
                "id": 1,
                "user": {
                    "id": 3,
                    "full_name": "as df gh",
                    "username": "grudoav@gmail.com"
                }
            },
            
        ],
        "curators": "as df gh, as df gh, as df gh, as df gh",
        "files": []
    },
    "chat": [
        {
            "type_msg": "msg",
            "from_user": {
                "id": 3,
                "full_name": "as df gh",
                "username": "grudoav@gmail.com"
            },
            "text": "привет",
            "time": "07:14",
            "chat": "client",
            "file_url": null,
            "file_size": "н/д",
            "icon": null,
            "filename": null
        },
        
    ],
    "user_id": 4,
    "unv_msg_client": 3,
    "unv_msg_curator": 4
}
    */



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

//                создаём переменную для сокета
                // создаём переменную для сокета
                window.chatSocket = 'null';

                // Заполняем модальное окно данными из `data`
                modalApplicationStatusContent.innerHTML = `
                    <div class="modal1_img modal-close">
                        <img src="${imgLink}" alt="">
                    </div>
                    <h4>${data.order.customer.title}</h4>
                    <p class="status_new_req status_req_p">Задача</p>
                    <ul class="tabs">
                        <li class="tab"><a href="#tab1">Описание</a></li>
                        <li class="tab">
                            <a href="#tab2">
                                <div class="order_tab">Комментарии</div>

                            </a>
                        </li>
                        <li class="tab">
                            <a href="#tab3">
                                <div class="order_tab">Чат кураторов</div>

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
                        <h6 class="title_in_modal">Исполнители</h6>
                        <div class="curators_of_request"></div>
                        <div class="btn_footer_request"></div>

                    </div>
                    
                    <div id="tab2" class="tab-content">
                        <div class="client_chat">
                                <div id="client_chat" cols="100" rows="20" class="chat_area"></div>
                            <div class="footer_message">
                                <input id="client-msg-input" class="chat-message-input" type="text" size="100">
                                <p>
                                    <input id="client-msg-file" name="client-msg-file" class="chat_add_file" type="file" multiple style="display: none;">
                                        <label for="client-msg-file" class="chat_add_file">
                                        <img src="${addFile2}" alt="">
                                    </label>
                                </p>
                                <p>
                                    <input id="client-msg-submit" name="client-msg-submit" class="chat_submit" type="button" value="Send" style="display: none;">
                                        <label for="client-msg-submit" class="chat_submit">
                                        <img src="${sentMsg}" alt="">
                                    </label>
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div id="tab3" class="tab-content">
                        <div class="curator_chat">
                            <div id="curator_chat" cols="100" rows="20" class="chat_area"></div>
                            <div class="footer_message">
                                <input id="curator-msg-input" name="curator-msg-input" class="chat-message-input" type="text" size="100">
                                <p>
                                    <input id="curator-msg-file" name="curator-msg-file" class="chat_add_file" type="file" multiple style="display: none;">
                                    <label for="curator-msg-file" class="chat_add_file">
                                        <img src="${addFile2}" alt="">
                                    </label>
                                </p>
                                <p>
                                    <input id="curator-msg-submit" name="curator-msg-submit" class="chat_submit" type="button" value="Send" style="display: none;">
                                        <label for="curator-msg-submit" class="chat_submit">
                                        <img src="${sentMsg}" alt="">
                                    </label>
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <button class="btn_new_req btn_req_p">Взять в работу</button>
                `;

                // Инициализация вкладок Materialize
                let tabs = document.querySelectorAll('.tabs');
                M.Tabs.init(tabs);

                // Открываем модальное окно
                M.Modal.getInstance(modalApplicationStatus).open();

                // кнопка скачать файл
                btnLdFile('.files_in_modal', data['order']['files'])

                // исполнители
                createCuratorsList('.curators_of_request', data['order']['curators'])

                let client_chat = createChat('#client_chat', data.client_chat, data.user_id, BASE.CLIENT)

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

                modalAddCurators('.curator_item_right')
                modalAddCurators('.btn_add_curator')

                if(data['order']['status'] == 'new') {
                    changeStatusNewToWork()
                    // data['order']['status'] = 'active'
                } else if (data['order']['status'] == 'active') {
                    let btnElem = document.querySelector('.btn_work_req')
                    let statusElem = document.querySelector('.status_work_req')
                    btnElem.addEventListener('click', function() {
                        changeStatusWorkToEnd(btnElem, statusElem)
                    })
                }

                // сокет. оставляем последним
                initOrderSocket(data.room, data.user_id)
            })
            .catch(error => console.error('Error:', error));
    });
});

// МО добавить исполнителя

let modalAddCurator = document.createElement('div')
modalAddCurator.setAttribute('id', 'modal_add_curator')
modalAddCurator.classList.add('modal')
// все что в МО заполняется через function modalAddCurators()

document.body.append(modalAddCurator)
