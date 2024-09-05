function notice(selector, num) {
    // console.log(`${selector} найден`)
    let parentElem = document.getElementById(selector)
    if (!parentElem) {
        return
    }

    if (parentElem) {
        let countNum = parentElem.querySelector('.page_menu_li_right')
        // countNum.classList.add('orders_count')

        if (num == 0 && countNum) {
            countNum.remove()
        }
        else if (num > 0 && !countNum) {
            let countNum = document.createElement('div')
            countNum.classList.add('page_menu_li_right')
            countNum.classList.add('orders_count')
            countNum.innerHTML = num

            parentElem.appendChild(countNum)
        }
        else if (num > 0 && countNum) {
            let newNum = parseInt(countNum.textContent)
            newNum += num
            countNum.innerHTML = newNum
        }
    } else {
        console.log(`${selector} не найден`)
    }
}

notice('id_menu_request', mainData['orders_count'])
notice('id_menu_request_mob', mainData['orders_count'])

notice('id_menu_push', mainData['notice'])
notice('id_menu_push_mob', mainData['notice'])


notice('id_menu_updatePO', mainData['update_count'])
notice('id_menu_updatePO_mob', mainData['update_count'])



// для чатов




// if (curator['orders_count'] > 0) {
//     let curator_orders = document.createElement('div')
//     curator_orders.classList.add('page_menu_li_right')
//     curator_orders.classList.add('orders_count')
//     curator_orders.innerHTML = curator['orders_count']

//     document.querySelector('.page_orders').append(curator_orders)

//     let curator_orders_mob = document.createElement('div')
//     curator_orders_mob.classList.add('sidenav_li_right')
//     curator_orders_mob.classList.add('orders_count')
//     curator_orders_mob.innerHTML = curator['orders_count']

//     document.querySelector('.mobile_orders').append(curator_orders_mob)
// }

// if (curator['notice'] > 0) {
//     let curator_push = document.createElement('div')
//     curator_push.classList.add('page_menu_li_right')
//     curator_push.classList.add('orders_count')
//     curator_push.innerHTML = curator['notice']

//     document.querySelector('.page_notice').append(curator_push)

//     let curator_push_mob = document.createElement('div')
//     curator_push_mob.classList.add('sidenav_li_right')
//     curator_push_mob.classList.add('orders_count')
//     curator_push_mob.innerHTML = curator['notice']

//     document.querySelector('.mobile_notice').append(curator_push_mob)
// }
