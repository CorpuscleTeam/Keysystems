document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

//   Модальное окно "Написать в тех Поддержку"

let modalSupport = document.createElement('div')
modalSupport.classList.add('modal')
modalSupport.setAttribute('id', 'modal_tech_support')

// Modal_content
let SupportContent = document.createElement('div')
SupportContent.classList.add('modal-content')
modalSupport.appendChild(SupportContent)

// Кнопка закрыть - функция записана в main_create_request.js
let supportClose = btnClose()
SupportContent.appendChild(supportClose)

// Заголовок - функция записана в main_create_request.js
let supportTitle = modalTitle('Написать в техподдержку')
SupportContent.appendChild(supportTitle)

// Форма
let formSupport = document.createElement('form')
formSupport.classList.add('mod_support_form')
formSupport.setAttribute('method', 'post')
formSupport.innerHTML = tokenForForm
SupportContent.appendChild(formSupport)

// Написать в техподдержку
let formSupportWrite = document.createElement('p')
formSupport.appendChild(formSupportWrite)

let labelSupportWrite = document.createElement('label')
labelSupportWrite.setAttribute('for', 'support_write')
labelSupportWrite.classList.add('required')
labelSupportWrite.innerHTML = `Ваш вопрос`
formSupportWrite.appendChild(labelSupportWrite)

let textareaSupportWrite = document.createElement('textarea')
textareaSupportWrite.setAttribute('name', 'support_write')
textareaSupportWrite.setAttribute('id', 'support_write')
formSupportWrite.appendChild(textareaSupportWrite)

// Кнопки - футер
let footerSupport = document.createElement('div')
formSupport.appendChild(footerSupport)

let btnSupportCancel = document.createElement('button')
btnSupportCancel.classList.add('btn_support_cancel')
btnSupportCancel.innerHTML = `Отмена`
footerSupport.appendChild(btnSupportCancel)

let btnSupportSubmit = document.createElement('button')
btnSupportSubmit.classList.add('btn_support_submit')
btnSupportSubmit.innerHTML = `Отправить`
footerSupport.appendChild(btnSupportSubmit)

// создать модальное окно
document.body.append(modalSupport)
