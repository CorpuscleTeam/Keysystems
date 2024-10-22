/*{
    "model": "client_app.news",
    "pk": 1,
    "fields": {
        "created_at": "2024-07-23T08:05:33.090Z",
        "updated_at": "2024-07-23T08:05:33.090Z",
        "type_entry": "news",
        "author": "Иванов Иван",
        "title": "Новейшество",
        "text_preview": "15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як",
        "text": "15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як\r\n15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як\r\n15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як",
        "photo": "news/5c23a3e243fb3167eb382be6.png",
        "is_active": true,
        "day": 23,
        "month": "Июля",
        "year": 2024
    }
} */

for (let i=0; i<news.length; i++) {
    let news_preview = document.createElement('div')
    // news.innerHTML = `Предпросмотр новости`
    news_preview.classList.add('page_body_news_preview')

    // шапка новости (дата, заголовок, автор)
    let news_header = document.createElement('div')
    news_header.classList.add('page_news_header')
    news_preview.appendChild(news_header)

    // шапка новости (дата)
    let news_date = document.createElement('div')
    news_date.classList.add('page_news_date')
    news_header.appendChild(news_date)

    // let news_date_flex = document.createElement('div')
    // news_date_flex.classList.add('news_date_flex')
    // news_date.appendChild(news_date_flex)

    let news_date_day = document.createElement('p')
    news_date_day.classList.add('news_date_day')
    news_date_day.innerHTML = news[i]['fields']['day']
    news_date.appendChild(news_date_day)

    let news_date_MY_flex = document.createElement('div')
    news_date_MY_flex.classList.add('date_MY_flex')
    news_date.appendChild(news_date_MY_flex)

    let news_date_mon = document.createElement('p')
    news_date_mon.classList.add('news_date_MY')
    news_date_mon.innerHTML = news[i]['fields']['month']
    news_date_MY_flex.appendChild(news_date_mon)

    let news_date_year = document.createElement('p')
    news_date_year.classList.add('news_date_MY')
    news_date_year.innerHTML = news[i]['fields']['year']
    news_date_MY_flex.appendChild(news_date_year)

    // Заголовок
    let news_title_flex = document.createElement('div')
    news_title_flex.classList.add('news_title_flex')
    news_header.appendChild(news_title_flex)

    let news_header_title = document.createElement('h3')
    news_header_title.classList.add('news_title')
    news_header_title.innerHTML = news[i]['fields']['title']
    news_title_flex.appendChild(news_header_title)

    let news_header_author = document.createElement('p')
    news_header_author.classList.add('news_author')
    news_header_author.innerHTML = `Автор: ${news[i]['fields']['author']}`
    news_title_flex.appendChild(news_header_author)

    // Текст Превью
    let news_text_preview = document.createElement('p')
    console.log(news[i]['fields']['text_preview'])
    news_text_preview.classList.add('news_text_preview')
    if (news[i]['fields']['text_preview']) {
        news_text_preview.innerHTML = news[i]['fields']['text_preview']
    }
    else{
        news_text_preview.innerHTML = news[i]['fields']['text']
    }
    news_preview.appendChild(news_text_preview)

    // кнопка "Читать"
    let btn_link_read = document.createElement('div')
    btn_link_read.classList.add('news_link_read')
    news_preview.appendChild(btn_link_read)

    let news_link_read = document.createElement('a')
    // news_link_read.setAttribute('href', `index_4_2?news=${news[i].pk}`)
    news_link_read.setAttribute('href', `/client/news?news=${news[i].pk}`)
    news_link_read.innerHTML = `Читать`
    btn_link_read.appendChild(news_link_read)

    // Создать предпросмотр новости
    document.querySelector('.page_flex_body').append(news_preview)
}