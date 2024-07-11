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
let ModalRequestClose = document.createElement('img')
// ModalRequestClose.setAttribute('src', '../img/close-large.svg')
ModalRequestClose.setAttribute('src', link)
modalContent.appendChild(ModalRequestClose)

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


// создать модальное окно
document.body.append(ModalCreateRequest)
