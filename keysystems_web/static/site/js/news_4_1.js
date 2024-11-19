/*{
author: null
day: 19
id: 2
month: "Ноября"
text: "" 
text_preview: ""
title: "С бабушкой"year: 2024
    }
} */


console.log(news)
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
    news_date_day.innerHTML = news[i]['day']
    news_date.appendChild(news_date_day)

    let news_date_MY_flex = document.createElement('div')
    news_date_MY_flex.classList.add('date_MY_flex')
    news_date.appendChild(news_date_MY_flex)

    let news_date_mon = document.createElement('p')
    news_date_mon.classList.add('news_date_MY')
    news_date_mon.innerHTML = news[i]['month']
    news_date_MY_flex.appendChild(news_date_mon)

    let news_date_year = document.createElement('p')
    news_date_year.classList.add('news_date_MY')
    news_date_year.innerHTML = news[i]['year']
    news_date_MY_flex.appendChild(news_date_year)

    // Заголовок
    let news_title_flex = document.createElement('div')
    news_title_flex.classList.add('news_title_flex')
    news_header.appendChild(news_title_flex)

    let news_header_title = document.createElement('h3')
    news_header_title.classList.add('news_title')
    news_header_title.innerHTML = news[i]['title']
    news_title_flex.appendChild(news_header_title)

    let news_header_author = document.createElement('p')
    news_header_author.classList.add('news_author')
    news_header_author.innerHTML = `Автор: ${news[i]['author']}`
    news_title_flex.appendChild(news_header_author)

    // Текст Превью
    let news_text_preview = document.createElement('p')
    news_text_preview.classList.add('news_text_preview')
    if (news[i]['text_preview']) {
        news_text_preview.innerHTML = news[i]['text_preview']
    }
    else{
        news_text_preview.innerHTML = news[i]['text']
    }
    news_preview.appendChild(news_text_preview)

    // кнопка "Читать"
    let btn_link_read = document.createElement('div')
    btn_link_read.classList.add('news_link_read')
    news_preview.appendChild(btn_link_read)

    let news_link_read = document.createElement('a')
    news_link_read.setAttribute('href', `/client/news/${news[i].id}`)
    news_link_read.innerHTML = `Читать`
    btn_link_read.appendChild(news_link_read)

    // Создать предпросмотр новости
    document.querySelector('.page_flex_body').append(news_preview)
}