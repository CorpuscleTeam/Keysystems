document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    // Обработчик нажатия на кнопку подтверждения в модальном окне
    document.getElementById('btnSupportConfirm').addEventListener('click', function () {
        document.getElementById('mod_support_form').submit();
    });

    // Обработчик для предотвращения отправки формы и открытия подтверждающего модального окна
    document.querySelector('#modal_tech_support form button').addEventListener('click', function (event) {
        event.preventDefault();
        var instance = M.Modal.getInstance(document.getElementById('modalSupportConfirm'));
        instance.open();
    });
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
formSupport.setAttribute('id', 'mod_support_form')
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
footerSupport.classList.add('mod_support_flex')
formSupport.appendChild(footerSupport)

let btnSupportCancel = document.createElement('a')
btnSupportCancel.classList.add('btn_support_cancel')
btnSupportCancel.innerHTML = `Отмена`
footerSupport.appendChild(btnSupportCancel)

let btnSupportSubmit = document.createElement('button')
btnSupportSubmit.classList.add('btn_support_submit')
btnSupportSubmit.setAttribute('href', '#modalSupportConfirm')
btnSupportSubmit.innerHTML = `Отправить`
footerSupport.appendChild(btnSupportSubmit)

// создать модальное окно
document.body.append(modalSupport)


// Модальное окно "подтверждение"
let modSupportConfirm = document.createElement('div')
modSupportConfirm.setAttribute('id', 'modalSupportConfirm')
modSupportConfirm.classList.add('modal')

// modal_content
let modSupportConfirmContent = document.createElement('div')
modSupportConfirmContent.classList.add('modal-content')
modSupportConfirm.appendChild(modSupportConfirmContent)

// кнопка закрыть
let btnSupportConfirmClose = btnClose()
modSupportConfirmContent.appendChild(btnSupportConfirmClose)

// ззаголовок
let SupportConfirmH = modalTitle('Спасибо за обращение')
modSupportConfirmContent.appendChild(SupportConfirmH)

let SupportConfirmP = document.createElement('p')
SupportConfirmP.innerHTML = `Мы отправим ответ вам на электронную посту, которая была указана при регистрации.`
modSupportConfirmContent.appendChild(SupportConfirmP)

// кнопки футер
let footerSupportConfirm = document.createElement('div')
footerSupportConfirm.classList.add('mod_support_flex')
modSupportConfirmContent.appendChild(footerSupportConfirm)

let btnSupportConfirmCancel = document.createElement('a')
btnSupportConfirmCancel.classList.add('btn_support_cancel')
btnSupportConfirmCancel.innerHTML = `Отмена`
footerSupportConfirm.appendChild(btnSupportConfirmCancel)

let btnSupportConfirmSubmit = document.createElement('button')
btnSupportConfirmSubmit.setAttribute('id', 'btnSupportConfirm')
btnSupportConfirmSubmit.classList.add('btn_support_submit')
btnSupportConfirmSubmit.innerHTML = `Да`
footerSupportConfirm.appendChild(btnSupportConfirmSubmit)

// Создать Модальное окно "Пдтвертить отправку формы"
document.body.append(modSupportConfirm)
