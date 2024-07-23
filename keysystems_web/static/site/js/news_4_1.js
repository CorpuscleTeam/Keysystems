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
    news_preview.classList.add('page_body_news')

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

    // Создать предпросмотр новости
    document.querySelector('.page_flex_body').append(news_preview)
}