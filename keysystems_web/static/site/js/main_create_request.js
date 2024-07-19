document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    // Обработчик нажатия на кнопку подтверждения в модальном окне
    document.getElementById('btnRequestConfirm').addEventListener('click', function () {
        document.getElementById('request_form').submit();
    });

    // Обработчик для предотвращения отправки формы и открытия подтверждающего модального окна
    document.querySelector('#modal_create_request form button').addEventListener('click', function (event) {
        event.preventDefault();
        var instance = M.Modal.getInstance(document.getElementById('modalRequestConfirm'));
        instance.open();
    });
});

//   Модальное окно "create_request"

let ModalCreateRequest = document.createElement('div')
ModalCreateRequest.classList.add('modal')
ModalCreateRequest.setAttribute('id', 'modal_create_request')

// Modal_content
let modalContent = document.createElement('div')
modalContent.classList.add('modal-content')
ModalCreateRequest.appendChild(modalContent)

// Кнопка закрыть
function btnClose() {
    let ModalRequestClose = document.createElement('div')
    ModalRequestClose.classList.add('modal1_img')
    ModalRequestClose.classList.add('modal-close')
    // modalContent.appendChild(ModalRequestClose)

    let modalCloseImg = document.createElement('img')
    modalCloseImg.setAttribute('src', link)
    ModalRequestClose.appendChild(modalCloseImg)

    return ModalRequestClose
}
let requestClose = btnClose()
modalContent.appendChild(requestClose)


// let modalContent = document.createElement('div')
// modalContent.classList.add('modal-content')
// ModalCreateRequest.appendChild(modalContent)

// // Кнопка закрыть
// let ModalRequestClose = document.createElement('div')
// ModalRequestClose.classList.add('modal1_img')
// ModalRequestClose.classList.add('modal-close')
// modalContent.appendChild(ModalRequestClose)

// let modalCloseImg = document.createElement('img')
// modalCloseImg.setAttribute('src', link)
// ModalRequestClose.appendChild(modalCloseImg)

// Заголовок
function modalTitle(title) {
    let ModalRequestH = document.createElement('h4')
    ModalRequestH.innerHTML = title
    return ModalRequestH
}
let requestH = modalTitle('Создать заявку')
modalContent.appendChild(requestH)

// Форма
let form = document.createElement('form')
form.classList.add('mod_request_form')
form.classList.add('enter_form')
form.setAttribute('id', 'request_form')
form.setAttribute('method', 'post')
form.setAttribute('enctype', 'multipart/form-data')
form.innerHTML = tokenForForm
modalContent.appendChild(form)

// Тип обращения
let typeAppeal = document.createElement('p')
form.appendChild(typeAppeal)

let labelTypeAppeal = document.createElement('label')
labelTypeAppeal.setAttribute('for', 'type_appeal')
labelTypeAppeal.classList.add('required')
labelTypeAppeal.innerHTML = `Тема обращения`
typeAppeal.appendChild(labelTypeAppeal)

let selectTypeAppeal = document.createElement('select')
selectTypeAppeal.setAttribute('name', 'type_appeal')
selectTypeAppeal.setAttribute('id', 'type_appeal')
typeAppeal.appendChild(selectTypeAppeal)

// добавить цикл с вариантами выбора
for (let i = 0; i < soft.length; i++) {
    let optionTypeAppeal = document.createElement('option')
    optionTypeAppeal.setAttribute('value', topics[i].pk)
    optionTypeAppeal.innerHTML = topics[i].fields.topic
    selectTypeAppeal.appendChild(optionTypeAppeal)
}

// Программное обеспечение
function chooseSoft() {
    let typeSoft = document.createElement('p')

    let labelTypeSoft = document.createElement('label')
    labelTypeSoft.setAttribute('for', 'type_soft')
    labelTypeSoft.classList.add('required')
    labelTypeSoft.innerHTML = `Програмное обеспечение`
    typeSoft.appendChild(labelTypeSoft)

    let selectTypeSoft = document.createElement('select')
    selectTypeSoft.setAttribute('name', 'type_soft')
    selectTypeSoft.setAttribute('id', 'type_soft')
    typeSoft.appendChild(selectTypeSoft)

    // цикл с вариантами выбора
    for (let i = 0; i < soft.length; i++) {
        let optionTypeSoft = document.createElement('option')
        optionTypeSoft.setAttribute('value', soft[i].pk)
        optionTypeSoft.innerHTML = soft[i].fields.title
        selectTypeSoft.appendChild(optionTypeSoft)
    }
    return typeSoft
}
let typeSoft = chooseSoft()
form.appendChild(typeSoft)


// let typeSoft = document.createElement('p')
// form.appendChild(typeSoft)

// let labelTypeSoft = document.createElement('label')
// labelTypeSoft.setAttribute('for', 'type_soft')
// labelTypeSoft.classList.add('required')
// labelTypeSoft.innerHTML = `Програмное обеспечение`
// typeSoft.appendChild(labelTypeSoft)

// let selectTypeSoft = document.createElement('select')
// selectTypeSoft.setAttribute('name', 'type_soft')
// selectTypeSoft.setAttribute('id', 'type_soft')
// typeSoft.appendChild(selectTypeSoft)

// // цикл с вариантами выбора
// for (let i = 0; i < soft.length; i++) {
//     let optionTypeSoft = document.createElement('option')
//     optionTypeSoft.setAttribute('value', soft[i].pk)
//     optionTypeSoft.innerHTML = soft[i].fields.title
//     selectTypeSoft.appendChild(optionTypeSoft)
// }

// Краткое описание
let description = document.createElement('p')
form.appendChild(description)

let labelDescription = document.createElement('label')
labelDescription.setAttribute('for', 'description')
labelDescription.classList.add('required')
labelDescription.innerHTML = `Краткое описание`
description.appendChild(labelDescription)

// счетчик символов
let textareaConteiner = document.createElement('div')
textareaConteiner.style.position = 'relative'
description.appendChild(textareaConteiner)
// textareaConteiner.appendChild(textareaDescription)

let textareaDescription = document.createElement('textarea')
textareaDescription.setAttribute('name', 'description')
textareaDescription.setAttribute('id', 'description')
textareaDescription.setAttribute('maxlength', '55')
textareaConteiner.appendChild(textareaDescription)

// элемент для отображения количества символов
let charCount = document.createElement('div');
charCount.id = 'charCount'
charCount.textContent = '0/55'
textareaConteiner.appendChild(charCount)

// обработчик событий input для обновления счетсика
textareaDescription.addEventListener('input', () => {
    const currentLength = textareaDescription.value.length
    const maxLength = textareaDescription.getAttribute('maxlength')
    charCount.textContent = `${currentLength}/${maxLength}`
})

// приложить файл
let addFile = document.createElement('p')
form.appendChild(addFile)

let inputAddFile = document.createElement('input')
inputAddFile.classList.add('add_file')
inputAddFile.setAttribute('type', 'file')
inputAddFile.setAttribute('id', 'addfile')
inputAddFile.setAttribute('name', 'addfile')
inputAddFile.setAttribute('multiple', 'multiple')
inputAddFile.style.display = 'none'
addFile.appendChild(inputAddFile)

let labelAddFile = document.createElement('label')
labelAddFile.setAttribute('for', 'addfile')
labelAddFile.classList.add('add_file')
labelAddFile.textContent = 'Добавить файлы'
labelAddFile.style.cursor = 'pointer'
addFile.appendChild(labelAddFile)

let labelAddFileImg = document.createElement('img')
labelAddFileImg.setAttribute('src', linkAddFile)
labelAddFile.prepend(labelAddFileImg)

let fileList = []

// загруженный файл
// Элемент для отображения названия загруженного файла
let fileNameDisplay = document.createElement('div');
fileNameDisplay.classList.add('file_name_display');
fileNameDisplay.style.marginTop = '10px';
addFile.appendChild(fileNameDisplay);

// Обработчик события изменения файла
inputAddFile.addEventListener('change', (event) => {
    const files = event.target.files;
    if (files.length > 0) {
        for (let i = 0; i < files.length; i++) {
            const file = files[i]
            const fileItem = document.createElement('div')
            fileItem.textContent = file.name
            fileNameDisplay.appendChild(fileItem)
        }
    }
});

// Обработка измения файлов
inputAddFile.addEventListener('change', function () {
    for (let i = 0; i < inputAddFile.files.length; i++) {
        fileList.push(inputAddFile.files[i]);
    }
    updateFileList();
});

// Функция для обновления списка файлов в форме
function updateFileList() {
    let dataTransfer = new DataTransfer();
    fileList.forEach(file => dataTransfer.items.add(file));
    inputAddFile.files = dataTransfer.files;

    // Обновляем отображение выбранных файлов (опционально)
    console.log(fileList);
}

// кнопка отправить заявку
// function form_btn_submit(title) {
//     let btnSubmitRequest = document.createElement('button')
//     btnSubmitRequest.classList.add('enter_button')
//     btnSubmitRequest.innerHTML = title
//     return btnSubmitRequest
// }
// let btnSubmitRequest = form_btn_submit(`Отправить запрос`)
// form.appendChild(btnSubmitRequest)

let btnSubmitRequest = document.createElement('button')
btnSubmitRequest.classList.add('modal-trigger')
btnSubmitRequest.setAttribute('href', '#modalRequestConfirm')
btnSubmitRequest.innerHTML = `Отправить запрос`
form.appendChild(btnSubmitRequest)

// let btnSubmitRequest = document.createElement('button')
// btnSubmitRequest.classList.add('enter_button')
// btnSubmitRequest.innerHTML = `Отправить запрос`
// form.appendChild(btnSubmitRequest)

// создать модальное окно
document.body.append(ModalCreateRequest)


// Модальное окно "подтвердить отправку формы"
let modRequestConfirm = document.createElement('div')
modRequestConfirm.setAttribute('id', 'modalRequestConfirm')
modRequestConfirm.classList.add('modal')

// modal_content
let modRequestConfirmContent = document.createElement('div')
modRequestConfirmContent.classList.add('modal-content')
modRequestConfirm.appendChild(modRequestConfirmContent)

// кнопка закрыть
let btnRequestConfirmClose = btnClose()
modRequestConfirmContent.appendChild(btnRequestConfirmClose)

// ззаголовок
let requestConfirmH = modalTitle('Подтверждение')
modRequestConfirmContent.appendChild(requestConfirmH)

let requestConfirmP = document.createElement('p')
requestConfirmP.innerHTML = `Вы действительно хотите отправить запрос на создание заявки?`
modRequestConfirmContent.appendChild(requestConfirmP)

// кнопки футер
let footerRequestConfirm = document.createElement('div')
footerRequestConfirm.classList.add('mod_support_flex')
modRequestConfirmContent.appendChild(footerRequestConfirm)

let btnRequestConfirCancel = document.createElement('a')
btnRequestConfirCancel.classList.add('btn_support_cancel')
btnRequestConfirCancel.innerHTML = `Отмена`
footerRequestConfirm.appendChild(btnRequestConfirCancel)

let btnRequestConfirSubmit = document.createElement('button')
btnRequestConfirSubmit.setAttribute('id', 'btnRequestConfirm')
btnRequestConfirSubmit.classList.add('btn_support_submit')
btnRequestConfirSubmit.innerHTML = `Да`
footerRequestConfirm.appendChild(btnRequestConfirSubmit)


// Создать Модальное окно "Пдтвертить отправку формы"
document.body.append(modRequestConfirm)


