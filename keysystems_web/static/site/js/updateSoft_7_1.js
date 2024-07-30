/* {
     "date": "ВЧЕРА / 15:25",
     "soft": "ПО 3",
     "description": "Программный комплекс «WEB-Торги-КС» предоставляет возможности автоматизированной работы для следующих групп пользователей",
     "update_files": [
         {
             "url": "/media/updates/5c23a3e243fb3167eb382be6.png",
             "name": "updates/5c23a3e243fb3167eb382be6.png"
         },
         {
             "url": "/media/updates/H8fJYUqYp9.jpeg",
             "name": "updates/H8fJYUqYp9.jpeg"
         }
     ]
 } */

let updatePO = document.createElement('div')
updatePO.classList.add('update_soft_flex')

for (let i = 0; i < updateSoft.length; i++) {
    // console.log(updateSoft[i])
    let updatePOitem = document.createElement('dev')
    updatePOitem.classList.add('updateItem')

    let updateHeader = document.createElement('div')
    updateHeader.classList.add('updateHeader_flex')
    updatePOitem.appendChild(updateHeader)

    let header_left = document.createElement('h4')
    header_left.classList.add('update_title')
    header_left.innerHTML = updateSoft[i]['soft']
    updateHeader.appendChild(header_left)

    let header_right = document.createElement('div')
    header_right.classList.add('update_date')
    header_right.innerHTML = updateSoft[i]['date']
    updateHeader.appendChild(header_right)

    updatePO.appendChild(updatePOitem)
}

document.querySelector('.page_flex_body').appendChild(updatePO)