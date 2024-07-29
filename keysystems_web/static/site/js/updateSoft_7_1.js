/* {
    "model": "client_app.news",
    "pk": 3,
    "fields": {
        "created_at": "2024-07-29T13:34:16.120Z",
        "updated_at": "2024-07-29T13:34:16.120Z",
        "type_entry": "update",
        "author": null,
        "title": "ПК «Финконтроль-смарт»",
        "text_preview": "Программный комплекс «Бюджет-СМАРТ» предназначен для автоматизации процессов составления, анализа и исполнения бюджета субъекта и бюджетов муниципальных образований. \r\nСоставление, уточнение бюджетной росписи, лимитов бюджетных обязательств;\r\nИсполнение бюджета по программно-целевому принципу;\r\nУчет бюджетных обязательств;\r\nКассовое обслуживание лицевых счетов бюджетных и автономных учреждений, бухгалтерский учет и отчетность по операциям со средствами бюджетных, автономных учреждений;\r\nВедение планов финансово-хозяйственной деятельности;",
        "text": "Программный комплекс «Бюджет-СМАРТ» предназначен для автоматизации процессов составления, анализа и исполнения бюджета субъекта и бюджетов муниципальных образований. \r\nСоставление, уточнение бюджетной росписи, лимитов бюджетных обязательств;\r\nИсполнение бюджета по программно-целевому принципу;\r\nУчет бюджетных обязательств;\r\nКассовое обслуживание лицевых счетов бюджетных и автономных учреждений, бухгалтерский учет и отчетность по операциям со средствами бюджетных, автономных учреждений;\r\nВедение планов финансово-хозяйственной деятельности;",
        "photo": "",
        "is_active": true,
        "date": "29 Июля 2024 / 13:34"
    }
} */

let updatePO = document.createElement('div')
updatePO.classList.add('update_soft_flex')

for (let i=0; i<updateSoft.length; i++) {
    console.log(updateSoft[i])
    let updatePOitem = document.createElement('dev')
    updatePOitem.classList.add('updateItem')

    let updateHeader = document.createElement('div')
    updateHeader.classList.add('updateHeader_flex')
    updatePOitem.appendChild(updateHeader)

    let header_left = document.createElement('h4')
    header_left.classList.add('update_title')
    header_left.innerHTML = updateSoft[i]['fields']['title']
    updateHeader.appendChild(header_left)

    let header_right = document.createElement('div')
    header_right.classList.add('update_date')
    header_right.innerHTML = updateSoft[i]['fields']['date']
    updateHeader.appendChild(header_right)

    updatePO.appendChild(updatePOitem)
}

document.querySelector('.page_flex_body').appendChild(updatePO)