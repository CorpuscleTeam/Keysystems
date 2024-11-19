// Кнопка "Назад"
let btn_link_back = document.createElement('div')
btn_link_back.classList.add('page_4_2_btn_back')

let news_link_back = document.createElement('a')
news_link_back.setAttribute('href', `index_4_1`)
news_link_back.classList.add('btn_back')
btn_link_back.appendChild(news_link_back)

let btn_back = document.createElement('button')
btn_back.innerHTML = `&larr; Назад`
news_link_back.appendChild(btn_back)

document.querySelector('.page_flex_body').appendChild(btn_link_back)

// шапка новости (дата, заголовок, автор)
let news_header = document.createElement('div')
news_header.classList.add('page_news_header')

document.querySelector('.page_flex_body').appendChild(news_header)

// шапка новости (дата)
let news_date = document.createElement('div')
news_date.classList.add('page_news_date')
news_header.appendChild(news_date)

let news_date_day = document.createElement('p')
news_date_day.classList.add('news_date_day')
news_date_day.innerHTML = news['day']
news_date.appendChild(news_date_day)

let news_date_MY_flex = document.createElement('div')
news_date_MY_flex.classList.add('date_MY_flex')
news_date.appendChild(news_date_MY_flex)

let news_date_mon = document.createElement('p')
news_date_mon.classList.add('news_date_MY')
news_date_mon.innerHTML = news['month']
news_date_MY_flex.appendChild(news_date_mon)

let news_date_year = document.createElement('p')
news_date_year.classList.add('news_date_MY')
news_date_year.innerHTML = news['year']
news_date_MY_flex.appendChild(news_date_year)

// Заголовок
let news_title_flex = document.createElement('div')
news_title_flex.classList.add('news_title_flex')
news_header.appendChild(news_title_flex)

let news_header_title = document.createElement('h3')
news_header_title.classList.add('news_title')
news_header_title.innerHTML = news['title']
news_title_flex.appendChild(news_header_title)

let news_header_author = document.createElement('p')
news_header_author.classList.add('news_author')
news_header_author.innerHTML = `Автор: ${news['author']}`
news_title_flex.appendChild(news_header_author)

// картинка новости
let news_img_div = document.createElement('div')
news_img_div.classList.add('page_news_img')
// news_img_div.innerHTML = news_img
document.querySelector('.page_flex_body').appendChild(news_img_div)

if (news.photo) {
    let news_img = document.createElement('img')
    news_img.setAttribute('src', news.photo)
    news_img_div.appendChild(news_img)
}
// Текст новости
let news_content = document.createElement('div')
news_content.classList.add('page_news_content')
news_content.innerHTML = news['text']
document.querySelector('.page_flex_body').appendChild(news_content)

// кнопки "Предыдущая новость", "Следующая новость"
let btn_news_footer = document.createElement('div')
btn_news_footer.classList.add('page_4_2_btn_news_footer-flex')

// Предыдущая новость
let news_footer_left = document.createElement('div')
news_footer_left.classList.add('btn_link_footer')
btn_news_footer.appendChild(news_footer_left)

if (news_previous > 0) {
    let link_news_previous = document.createElement('a')
    link_news_previous.setAttribute('href', `/client/news/${news_previous}`)
    link_news_previous.classList.add('link_news_previous')
    news_footer_left.appendChild(link_news_previous)

    let btn_news_previous = document.createElement('button')
    btn_news_previous.innerHTML = `&larr; Предыдущая запись`
    link_news_previous.appendChild(btn_news_previous)
}

// Следующая новость
let news_footer_right = document.createElement('div')
news_footer_right.classList.add('btn_link_footer')
btn_news_footer.appendChild(news_footer_right)

if (news_next > 0) {
    let link_news_next = document.createElement('a')
    link_news_next.setAttribute('href', `/client/news/${news_next}`)
    link_news_next.classList.add('link_news_next')
    news_footer_right.appendChild(link_news_next)

    let btn_news_next = document.createElement('button')
    btn_news_next.innerHTML = `Следующая запись &rarr;`
    link_news_next.appendChild(btn_news_next)
}

document.querySelector('.page_flex_body').appendChild(btn_news_footer)

