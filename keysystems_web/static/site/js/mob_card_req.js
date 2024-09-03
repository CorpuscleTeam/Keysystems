document.addEventListener('DOMContentLoaded', function() {
    // Находим элемент с классом .tabs
    let tabsElement = document.querySelector('.tabs');

    // Инициализируем вкладки только если элемент tabsElement существует
    if (tabsElement) {
        let tabsInstance = M.Tabs.init(tabsElement);
    }


// let tabsElement = document.querySelector('.tabs');
// let tabsInstance = M.Tabs.init(tabsElement);


let mobNewOrders = document.createElement('div')
mobNewOrders.classList.add('mob_orders_grid')
document.querySelector('#tab1_mob').appendChild(mobNewOrders)

let mobActiveOrders = document.createElement('div')
mobActiveOrders.classList.add('mob_orders_grid')
document.querySelector('#tab2_mob').appendChild(mobActiveOrders)

let mobDoneOrders = document.createElement('div')
mobDoneOrders.classList.add('mob_orders_grid')
document.querySelector('#tab3_mob').appendChild(mobDoneOrders)

// карточки с заявками
for (let i = 0; i < card_orders.length; i++) {
    let mobCard = createOrderCard(card_orders[i])

    if (card_orders[i]['status'] == 'new') {
        mobNewOrders.appendChild(mobCard)
    }
    if (card_orders[i]['status'] == 'active') {
        mobActiveOrders.appendChild(mobCard)
    }
    if (card_orders[i]['status'] == 'done') {
        mobDoneOrders.appendChild(mobCard)
    }
}
})
