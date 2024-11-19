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
console.log(updateSoft)


for (let i = 0; i < updateSoft.length; i++) {
    // console.log(updateSoft[i])
    let updatePOitem = document.createElement('dev')
    updatePOitem.classList.add('updateItem')

    // Шапка обновления
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

    // Превью контент
    let updateText = document.createElement('p')
    updateText.classList.add('update_text')
    updateText.innerHTML = updateSoft[i]['description']
    updatePOitem.appendChild(updateText)

    // кнопка "читать"

    // let btnLinkRead = document.createElement('div')
    // btnLinkRead.classList.add('news_link_read')
    // updatePOitem.appendChild(btnLinkRead)

    // let updateLinkRead = document.createElement('a')
    // updateLinkRead.setAttribute('href', `index_7_2?update=${updateSoft[i].pk}`)
    // updateLinkRead.innerHTML = `Читать`
    // btnLinkRead.appendChild(updateLinkRead)

    let btnLinkRead = document.createElement('a')
    btnLinkRead.classList.add('read_link')
    // btnLinkRead.setAttribute('href', `index_7_2?update=${updateSoft[i].pk}`)
    btnLinkRead.setAttribute('href', `/client/upgrade/${updateSoft[i].id}`)
    btnLinkRead.innerHTML = `Читать`
    updatePOitem.appendChild(btnLinkRead)

    updatePO.appendChild(updatePOitem)
}

document.querySelector('.page_flex_body').appendChild(updatePO)