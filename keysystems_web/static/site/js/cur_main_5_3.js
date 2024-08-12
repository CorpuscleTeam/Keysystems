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
            {
                "id": 2,
                "user": {
                    "id": 3,
                    "full_name": "as df gh",
                    "username": "grudoav@gmail.com"
                }
            },
            {
                "id": 3,
                "user": {
                    "id": 3,
                    "full_name": "as df gh",
                    "username": "grudoav@gmail.com"
                }
            },
            {
                "id": 4,
                "user": {
                    "id": 3,
                    "full_name": "as df gh",
                    "username": "grudoav@gmail.com"
                }
            }
        ],
        "curators": "as df gh, as df gh, as df gh, as df gh",
        "files": []
    },
    "client_chat": [
        {
            "created_at": "2024-08-09T16:14:02.119024+09:00",
            "from_user": {
                "id": 3,
                "full_name": "as df gh",
                "username": "grudoav@gmail.com"
            },
            "text": "привет"
        },
        {
            "created_at": "2024-08-09T16:14:29.845423+09:00",
            "from_user": {
                "id": 3,
                "full_name": "as df gh",
                "username": "grudoav@gmail.com"
            },
            "text": "ывдлаофыжваощжвапщшч чваавфвафав"
        }
    ],
    "curator_chat": [
        {
            "created_at": "2024-08-09T16:14:16.335624+09:00",
            "from_user": {
                "id": 3,
                "full_name": "as df gh",
                "username": "grudoav@gmail.com"
            },
            "text": "ддллорпаааимтоьл"
        },
        {
            "created_at": "2024-08-09T16:14:45.712592+09:00",
            "from_user": {
                "id": 3,
                "full_name": "as df gh",
                "username": "grudoav@gmail.com"
            },
            "text": "лвыдаофыодплзсзчсдль члаопфвшфцхмм звааэ"
        }
    ],
    "user_id": 4,
    "unv_msg_client": 3,
    "unv_msg_curator": 4
}
    */

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    // document.querySelectorAll('.modal_link_cards').forEach(link => {
    //     link.addEventListener('click', function(event) {
    //         const orderId = this.getAttribute('data-order-id');
    //         const modalContent = document.querySelector('#statusOrder .modal-content');
    //     });
    // });
});

let modalApplicationStatus = document.createElement('div')
// modalApplicationStatus.setAttribute('id', new_orders[i]['id'])
modalApplicationStatus.setAttribute('id', 'statusOrder')
modalApplicationStatus.classList.add('modal')

let modalApplicationStatusContent = document.createElement('div')
modalApplicationStatusContent.classList.add('modal-content')
modalApplicationStatus.appendChild(modalApplicationStatusContent)

// let modASClose = btnClose()
// modalApplicationStatusContent.appendChild(modASClose)

document.body.append(modalApplicationStatus)
console.log('должно создатьс модальное окно')

{/* <img src="/static/site/img/close-large.svg" alt=""> */}
// обработчик событий данные с бэка
document.querySelectorAll('.modal_cr_order').forEach(link => {
    // console.log('должно создатьс модальное окно!!')

    link.addEventListener('click', function () {
        let orderId = this.getAttribute('data-order-id');
        // console.log('должно создатьс модальное окно!!')
        // Здесь делаем запрос на бэк с использованием Fetch API
        fetch(`/order-data/${orderId}`)
            .then(response => response.json())
            .then(data => {
                // Заполняем модальное окно данными из `data`
                modalApplicationStatusContent.innerHTML = `
                    <div class="modal1_img modal-close">
                        
                        <img src="${imgLink}" alt="">
                    </div>
                    <h4>${data.order.customer.title}</h4>
                    <p>${data.order.status}</p>
                    <ul class="tabs">
                        <li class="tab"><a href="#tab1">Описание</a></li>
                        <li class="tab">
                            <a href="#tab2">
                                <p class="order_tab">Комментарии</p>

                            </a>
                        </li>
                        <li class="tab">
                            <a href="#tab3">
                                <p class="order_tab">Чат кураторов</p>

                            </a>
                        </li>
                    </ul>

                    <div id="tab1" class="tab-content active">
                        <h6 class="title_in_modal">Тема</h6>
                        <p class="text_in_modal">${data.order.topic.topic}</p>
                        <form action="" method="post">
                            <p>
                                <label for="soft_in_chat">Програмное обеспечение</label>
                                <select name="soft_in_chat" id="soft_in_chat">
                                </select>
                            </p>
                        </form>
                        <h6 class="title_in_modal">Описание</h6>
                        <p class="text_in_modal">${data.order.text}</p>
                        <div class="files_in_modal"></div>
                        <h6 class="title_in_modal">Исполнители</h6>
                        <div class="curators_of_request"></div>
                        

                    </div>

                    <div id="tab2" class="tab-content">
                        <div id="tab2" class="tab-content client_chat">
                            <div class="chat-window">
                                <div class="chat-header">
                                    <h4>Чат</h4>
                                </div>
                                <div class="chat-body">
                                    <div class="chat-messages"></div>
                                </div>
                                <div class="chat-footer">
                                    <input type="text" id="chat-input" placeholder="Введите сообщение..." />
                                    <button id="send-btn">Отправить</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="tab3" class="tab-content">
                        <p>Status: ${data.order.status}</p>
                    </div>
                `;
                console.log(data)

                // Инициализация вкладок Materialize
                let tabs = document.querySelectorAll('.tabs');
                M.Tabs.init(tabs);

                // Открываем модальное окно
                M.Modal.getInstance(modalApplicationStatus).open();
            })
            .catch(error => console.error('Error:', error));
    });
});

// дальше непонятная хрень с вебсокетом



