document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
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
let ModalRequestClose = document.createElement('div')
ModalRequestClose.classList.add('modal1_img')
modalContent.appendChild(ModalRequestClose)

let modalCloseImg = document.createElement('img')
modalCloseImg.setAttribute('src', link)
ModalRequestClose.appendChild(modalCloseImg)

// Заголовок
let ModalRequestH = document.createElement('h4')
ModalRequestH.innerHTML = 'Создать заявку'
modalContent.appendChild(ModalRequestH)

// Форма
let form = document.createElement('form')
form.classList.add('mod_request_form')
form.setAttribute('method', 'post')
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

    // !! добавить цикл с вариантами выбора
let optionTypeAppeal = document.createElement('option')
selectTypeAppeal.appendChild(optionTypeAppeal)

// Программное обеспечение
let typeSoft = document.createElement('p')
form.appendChild(typeSoft)

let labelTypeSoft = document.createElement('label')
labelTypeSoft.setAttribute('for', 'type_soft')
labelTypeSoft.classList.add('required')
labelTypeSoft.innerHTML = `Програмное обеспечение`
typeSoft.appendChild(labelTypeSoft)

let selectTypeSoft = document.createElement('select')
selectTypeSoft.setAttribute('name', 'type_soft')
selectTypeSoft.setAttribute('id', 'type_soft')
typeSoft.appendChild(selectTypeSoft)

    // !! добавить цикл с вариантами выбора
let optionTypeSoft = document.createElement('option')
selectTypeSoft.appendChild(optionTypeSoft)

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
// textareaDescription.style.width = '100%'
// textareaDescription.style.height = '100px'
// textareaDescription.style.paddingBottom = '20px'
// textareaDescription.style.resize = 'none'
textareaConteiner.appendChild(textareaDescription)

// элемент для отображения количества символов
let charCount = document.createElement('div');
charCount.id = 'charCount'
// charCount.style.position = 'absolute'
// charCount.style.bottom = '5px'
// charCount.style.right = '10px'
// charCount.style.fontSize = '12px'
// charCount.style.color = 'gray'
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
inputAddFile.setAttribute('type', 'file')
inputAddFile.setAttribute('id', 'addfile')
inputAddFile.setAttribute('name', 'addfile')
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

// загруженный файл
// Элемент для отображения названия загруженного файла
let fileNameDisplay = document.createElement('span');
fileNameDisplay.classList.add('file_name_display');
fileNameDisplay.style.marginLeft = '10px';
addFile.appendChild(fileNameDisplay);

// Обработчик события изменения файла
inputAddFile.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        fileNameDisplay.textContent = file.name;
    } else {
        fileNameDisplay.textContent = '';
    }
});

// кнопка отправить заявку
let btnSubmitRequest = document.createElement('button')
btnSubmitRequest.classList.add('enter_button')
btnSubmitRequest.innerHTML = `Отправить запрос`
form.appendChild(btnSubmitRequest)


// создать модальное окно
document.body.append(ModalCreateRequest)
