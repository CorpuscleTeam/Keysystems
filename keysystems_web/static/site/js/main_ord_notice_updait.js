if (orders > 0) {
    let application = document.createElement('div')
    application.classList.add('page_menu_li_right')
    application.classList.add('orders_count')
    application.innerHTML = orders

    document.querySelector('.page_orders').append(application)

    let applicationMob = document.createElement('div')
    applicationMob.classList.add('sidenav_li_right')
    applicationMob.classList.add('orders_count')
    applicationMob.innerHTML = orders

    document.querySelector('.mobile_orders').append(applicationMob)
}

if (notice >0 ) {
    let push = document.createElement('div')
    push.classList.add('page_menu_li_right')
    push.classList.add('notice')
    push.innerHTML = notice

    document.querySelector('.page_notice').append(push)

    let pushMob = document.createElement('div')
    pushMob.classList.add('sidenav_li_right')
    pushMob.classList.add('notice')
    pushMob.innerHTML = notice

    document.querySelector('.mobile_notice').append(pushMob)
}

if (update_count > 0) {
    let updatePO = document.createElement('div')
    updatePO.classList.add('page_menu_li_right')
    updatePO.classList.add('update_count')
    updatePO.innerHTML = update_count

    document.querySelector('.page_update').append(updatePO)

    let updatePOMob = document.createElement('div')
    updatePOMob.classList.add('sidenav_li_right')
    updatePOMob.classList.add('update_count')
    updatePOMob.innerHTML = update_count

    document.querySelector('.mobile_update').append(updatePOMob)
}
