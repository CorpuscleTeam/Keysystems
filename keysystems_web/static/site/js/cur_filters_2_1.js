// на странице 2_1 кураторской панели

let filter_flex_link = document.createElement('a')
filter_flex_link.setAttribute('src', '#modalFilter') // добавить ссылку на модальное окно
filter_flex_link.classList.add('page_body_right')
document.querySelector('.page_flex_body_title').appendChild(filter_flex_link)

let filter_flex = document.createElement('div')
filter_flex.classList.add('filter_flex_right')
filter_flex_link.appendChild(filter_flex)

let filterImg = document.createElement('img')
filterImg.setAttribute('src', filter_img)
filter_flex.appendChild(filterImg)

let filterText = document.createElement('p')
filterText.innerHTML = `Фильтр`
filter_flex.appendChild(filterText)

// МО Фильтр
let modalFilter = document.createElement('div')
modalFilter.setAttribute('id', 'modalFilter')
modalFilter.classList.add('modal')

document.body.append(modalFilter)

let modalFilterContent = document.createElement('div')
modalFilterContent.classList.add('modal-content')
modalFilter.appendChild(modalFilterContent)

let Close = btnClose()
modalFilterContent.appendChild(Close)

let title = modalTitle('Фильтр')
modalFilterContent.appendChild(title)


