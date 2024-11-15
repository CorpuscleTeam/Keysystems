// console.log(push)

/* 
[
    {
        "id": 49,
        "order": {
            "id": 13,
            "text": "Тест заявки с файлом"
        },
        "type_notice": "В заявке #00013 куратор оставил новое сообщение.",
        "date": "ВЧЕРА / 010:29",
        "text": "В заявке #00013 куратор оставил новое сообщение."
    },
   ...
]*/

let allPush = document.createElement('div')
allPush.classList.add('page_body_push_flex')

for(let i = 0; i < push.length; i++) {
    // console.log(push[i])
    let modalLinkPush = document.createElement('a')
    modalLinkPush.classList.add('modal_link_push')
    modalLinkPush.classList.add('modal_cr_order')
    modalLinkPush.setAttribute('data-order-id', push[i]['order']['id'])
    modalLinkPush.setAttribute('href', '#statusOrder') // добавить ссылку как в 5.1

    let newCardPush = document.createElement('div')
    newCardPush.classList.add('new_card_push')
    modalLinkPush.appendChild(newCardPush)

    // левая часть уведомления
    let newCardLeft = document.createElement('div')
    newCardLeft.classList.add('card_push_left')
    newCardPush.appendChild(newCardLeft)

    let textNewCard = document.createElement('p')
    textNewCard.classList.add('text_new_push')
    textNewCard.innerHTML = push[i]['text']
    newCardLeft.appendChild(textNewCard)

    let timeNewCard = document.createElement('p')
    timeNewCard.classList.add('time_new_push')
    timeNewCard.innerHTML = push[i]['date']
    newCardLeft.appendChild(timeNewCard)

    // правая часть стрелочка
    let newCardRight = document.createElement('div')
    newCardRight.classList.add('card_new_right')
    newCardPush.appendChild(newCardRight)

    let imgNewRight = document.createElement('img')
    imgNewRight.setAttribute('src', arrow_right)
    newCardRight.appendChild(imgNewRight)

    allPush.appendChild(modalLinkPush)
}

// создать флекс все уведомления
document.querySelector('.page_flex_body').appendChild(allPush)

document.querySelectorAll('.modal_cr_order').forEach(link => {
    link.addEventListener('click', function () {
        let orderId = this.getAttribute('data-order-id');
        // console.log(orderId)

        // Здесь делаем запрос на бэк с использованием Fetch API
        craeteOrderModal(orderId)

    });
});