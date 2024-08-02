if (curator['orders_count']>0) {
    let curator_orders = document.createElement('div')
    curator_orders.classList.add('page_menu_li_right')
    curator_orders.classList.add('orders_count')
    curator_orders.innerHTML = curator['orders_count']

    document.querySelector('.page_orders').append(curator_orders)

    let curator_orders_mob = document.createElement('div')
    curator_orders_mob.classList.add('sidenav_li_right')
    curator_orders_mob.classList.add('orders_count')
    curator_orders_mob.innerHTML = curator['orders_count']

    document.querySelector('.mobile_orders').append(curator_orders_mob)
}

if (curator['notice']>0) {
    let curator_push = document.createElement('div')
    curator_push.classList.add('page_menu_li_right')
    curator_push.classList.add('orders_count')
    curator_push.innerHTML = curator['notice']

    document.querySelector('.page_notice').append(curator_push)

    let curator_push_mob = document.createElement('div')
    curator_push_mob.classList.add('sidenav_li_right')
    curator_push_mob.classList.add('orders_count')
    curator_push_mob.innerHTML = curator['notice']

    document.querySelector('.mobile_notice').append(curator_push_mob)
}
