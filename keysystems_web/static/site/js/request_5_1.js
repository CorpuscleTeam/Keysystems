/* {
    "model": "common.order",
    "pk": 4,
    "fields": {
        "created_at": "2024-07-25T08:40:24.122Z",
        "updated_at": "2024-07-25T08:40:24.122Z",
        "from_user": 3,
        "customer": 1,
        "text": "Учет поступления платежей в бюджет",
        "soft": 1,
        "topic": 1,
        "executor": 3,
        "status": "new"
    }
} */

// Создать div_grid со всеми заявками
let all_orders = document.createElement('div')
all_orders.classList.add('page_body_orders')

// колонка "Новые заявки"
let groupOfNewOrders = document.createElement('div')
groupOfNewOrders.classList.add('groups_orders')
all_orders.appendChild(groupOfNewOrders)

// Заголовок "Новые заявки"
let headerOfNewOrders = document.createElement('div')
headerOfNewOrders.classList.add('new_orders')
headerOfNewOrders.classList.add('header_orders')
groupOfNewOrders.appendChild(headerOfNewOrders)

let titleOfNewOrders = document.createElement('h4')
titleOfNewOrders.innerHTML = 'Задачи'
headerOfNewOrders.appendChild(titleOfNewOrders)

let countOfNewOrders = document.createElement('p')
countOfNewOrders.innerHTML = new_orders.length
headerOfNewOrders.appendChild(countOfNewOrders)

// карточки с заявками
let newOrderFlex = document.createElement('div')
newOrderFlex.classList.add('order_flex')
groupOfNewOrders.appendChild(newOrderFlex)

for (let i = 0; i < new_orders.length; i++) {
    let modalLinkCard = document.createElement('a')
    modalLinkCard.classList.add('modal_link_cards')
    modalLinkCard.setAttribute('href', '#') // добавить ссылку на модальное окно заявки

    let newOrder = document.createElement('div')
    newOrder.classList.add('card_order')

    let textNewOrder = document.createElement('p')
    textNewOrder.classList.add('textOfOrder')
    textNewOrder.innerHTML = new_orders[i]['fields']['text']
    newOrder.appendChild(textNewOrder)

    let softNewOrder = document.createElement('p')
    softNewOrder.classList.add('softOfOrder')
    softNewOrder.innerHTML = new_orders[i]['fields']['soft']
    newOrder.appendChild(softNewOrder)

    let numOfOrder = document.createElement('p')
    numOfOrder.classList.add('numOfOrder')
    numOfOrder.innerHTML = new_orders[i]['pk']
    newOrder.appendChild(numOfOrder)

    modalLinkCard.appendChild(newOrder)
    newOrderFlex.appendChild(modalLinkCard)
}

// колонка "В работе"
let groupOfActiveOrders = document.createElement('div')
groupOfActiveOrders.classList.add('groups_orders')
all_orders.appendChild(groupOfActiveOrders)

// Заголовок "В работе"
let headerOfActiveOrders = document.createElement('div')
headerOfActiveOrders.classList.add('active_orders')
headerOfActiveOrders.classList.add('header_orders')
groupOfActiveOrders.appendChild(headerOfActiveOrders)

let titleOfActiveOrders = document.createElement('h4')
titleOfActiveOrders.innerHTML = 'В работе'
headerOfActiveOrders.appendChild(titleOfActiveOrders)

let countOfActiveOrders = document.createElement('p')
countOfActiveOrders.innerHTML = active_orders.length
headerOfActiveOrders.appendChild(countOfActiveOrders)

// карточки с заявками
let activeOrderFlex = document.createElement('div')
activeOrderFlex.classList.add('order_flex')
groupOfActiveOrders.appendChild(activeOrderFlex)

for (let i = 0; i < active_orders.length; i++) {
    let modalLinkCard = document.createElement('a')
    modalLinkCard.classList.add('modal_link_cards')
    modalLinkCard.setAttribute('href', '#') // добавить ссылку на модальное окно заявки

    let activeOrder = document.createElement('div')
    activeOrder.classList.add('card_order')

    let textActiveOrder = document.createElement('p')
    textActiveOrder.classList.add('textOfOrder')
    textActiveOrder.innerHTML = active_orders[i]['fields']['text']
    activeOrder.appendChild(textActiveOrder)

    let softActiveOrder = document.createElement('p')
    softActiveOrder.classList.add('softOfOrder')
    softActiveOrder.innerHTML = active_orders[i]['fields']['soft']
    activeOrder.appendChild(softActiveOrder)

    let numOfOrder = document.createElement('p')
    numOfOrder.classList.add('numOfOrder')
    numOfOrder.innerHTML = active_orders[i]['pk']
    activeOrder.appendChild(numOfOrder)

    modalLinkCard.appendChild(activeOrder)
    activeOrderFlex.appendChild(modalLinkCard)
}

// колонка "Выполнено"
let groupOfDoneOrders = document.createElement('div')
groupOfDoneOrders.classList.add('groups_orders')
all_orders.appendChild(groupOfDoneOrders)

// Заголовок "В работе"
let headerOfDoneOrders = document.createElement('div')
headerOfDoneOrders.classList.add('done_orders')
headerOfDoneOrders.classList.add('header_orders')
groupOfDoneOrders.appendChild(headerOfDoneOrders)

let titleOfDoneOrders = document.createElement('h4')
titleOfDoneOrders.innerHTML = 'Выполнено'
headerOfDoneOrders.appendChild(titleOfDoneOrders)

let countOfDoneOrders = document.createElement('p')
countOfDoneOrders.innerHTML = done_orders.length
headerOfDoneOrders.appendChild(countOfDoneOrders)

// карточки с заявками
let doneOrderFlex = document.createElement('div')
doneOrderFlex.classList.add('order_flex')
groupOfDoneOrders.appendChild(doneOrderFlex)

for (let i = 0; i < done_orders.length; i++) {
    let modalLinkCard = document.createElement('a')
    modalLinkCard.classList.add('modal_link_cards')
    modalLinkCard.setAttribute('href', '#') // добавить ссылку на модальное окно заявки

    let doneOrder = document.createElement('div')
    doneOrder.classList.add('card_order')

    let textDoneOrder = document.createElement('p')
    textDoneOrder.classList.add('textOfOrder')
    textDoneOrder.innerHTML = done_orders[i]['fields']['text']
    doneOrder.appendChild(textDoneOrder)

    let softDoneOrder = document.createElement('p')
    softDoneOrder.classList.add('softOfOrder')
    softDoneOrder.innerHTML = done_orders[i]['fields']['soft']
    doneOrder.appendChild(softDoneOrder)

    let numOfOrder = document.createElement('p')
    numOfOrder.classList.add('numOfOrder')
    numOfOrder.innerHTML = done_orders[i]['pk']
    doneOrder.appendChild(numOfOrder)

    modalLinkCard.appendChild(doneOrder)
    doneOrderFlex.appendChild(modalLinkCard)
}

// создать серку grid со всеми заявками
document.querySelector('.page_flex_body').appendChild(all_orders)
