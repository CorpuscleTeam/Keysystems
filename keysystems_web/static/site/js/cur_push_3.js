console.log(card_push)

/* 
[
    {
        "order_id": 3,
        "num_push": 3,
        "date": "26 Июля 2024 / 08:16",
        "text": "Ваша задача #00003 переведена в статус «В РАБОТЕ»."
    },
    {
        "order_id": 6,
        "num_push": 2,
        "date": "26 Июля 2024 / 08:15",
        "text": "Ваша задача #00002 переведена в статус «ВЫПОЛНЕНО». Оцените качество выполненной работы."
    },
    {
        "order_id": 2,
        "num_push": 1,
        "date": "26 Июля 2024 / 08:15",
        "text": "Ваша задача #00001 переведена в статус «В РАБОТЕ»."
    }
] */

let allPush = document.createElement('div')
allPush.classList.add('page_body_push_flex')

for(let i=0; i<card_push.length; i++) {
    // console.log(push[i])
    let modalLinkPush = document.createElement('a')
    modalLinkPush.classList.add('modal_link_push')
    modalLinkPush.setAttribute('href', '#') // добавить ссылку как в 5.1

    let newCardPush = document.createElement('div')
    newCardPush.classList.add('new_card_push')
    modalLinkPush.appendChild(newCardPush)

    // левая часть уведомления
    let newCardLeft = document.createElement('div')
    newCardLeft.classList.add('card_push_left')
    newCardPush.appendChild(newCardLeft)

    let textNewCard = document.createElement('p')
    textNewCard.classList.add('text_new_push')
    textNewCard.innerHTML = card_push[i]['text']
    newCardLeft.appendChild(textNewCard)

    let timeNewCard = document.createElement('p')
    timeNewCard.classList.add('time_new_push')
    timeNewCard.innerHTML = card_push[i]['date']
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
