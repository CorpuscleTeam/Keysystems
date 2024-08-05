// console.log(orders)
console.log(cur_orders)
// let orders = orders1

// for (let i=0; i<orders.length; i++) {

// }

function createOrderCard(order) {
    // console.log(order['status'])
    let modalLinkCard = document.createElement('a')
    modalLinkCard.classList.add('modal_link_cards')
    modalLinkCard.classList.add('modal-trigger')
    modalLinkCard.setAttribute('href', '#statusOrder') // добавить ссылку на модальное окно заявки

    let newOrder = document.createElement('div')
    newOrder.classList.add('card_order')

    let textNewOrder = document.createElement('p')
    textNewOrder.classList.add('textOfOrder')
    textNewOrder.innerHTML = order['text']
    newOrder.appendChild(textNewOrder)

    let softNewOrder = document.createElement('p')
    softNewOrder.classList.add('softOfOrder')
    softNewOrder.innerHTML = order['soft']['title']
    newOrder.appendChild(softNewOrder)

    let numOfOrder = document.createElement('p')
    numOfOrder.classList.add('numOfOrder')
    numOfOrder.innerHTML = order['id_str']
    newOrder.appendChild(numOfOrder)

    modalLinkCard.appendChild(newOrder)
    // newOrderFlex.appendChild(modalLinkCard)

    return modalLinkCard
}

// Создать div_grid со всеми заявками
let all_orders = document.createElement('div')
all_orders.classList.add('page_body_orders')
// создать серку grid со всеми заявками
document.querySelector('.page_flex_body').appendChild(all_orders)

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

// let countOfNewOrders = document.createElement('p')
// countOfNewOrders.innerHTML = new_orders.length
// headerOfNewOrders.appendChild(countOfNewOrders)

// карточки с заявками
let newOrderFlex = document.createElement('div')
newOrderFlex.classList.add('order_flex')
groupOfNewOrders.appendChild(newOrderFlex)

// for (let i = 0; i < new_orders.length; i++) {

// }

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

// let countOfActiveOrders = document.createElement('p')
// countOfActiveOrders.innerHTML = active_orders.length
// headerOfActiveOrders.appendChild(countOfActiveOrders)

// карточки с заявками
let activeOrderFlex = document.createElement('div')
activeOrderFlex.classList.add('order_flex')
groupOfActiveOrders.appendChild(activeOrderFlex)

// for (let i = 0; i < active_orders.length; i++) {

// }

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

// let countOfDoneOrders = document.createElement('p')
// countOfDoneOrders.innerHTML = done_orders.length
// headerOfDoneOrders.appendChild(countOfDoneOrders)

// карточки с заявками
let doneOrderFlex = document.createElement('div')
doneOrderFlex.classList.add('order_flex')
groupOfDoneOrders.appendChild(doneOrderFlex)

for (let i = 0; i < cur_orders.length; i++) {
    let card = createOrderCard(cur_orders[i])

    if (cur_orders[i]['status']=='new') {
        newOrderFlex.appendChild(card)
    }
    if (cur_orders[i]['status']=='active') {
        activeOrderFlex.appendChild(card)
    }
    if (cur_orders[i]['status']=='done') {
        doneOrderFlex.appendChild(card)
    }
}



