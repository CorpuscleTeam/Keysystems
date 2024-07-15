document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

//   Модальное окно Настройки "Settings"

let ModalSettings = document.createElement('div')
ModalSettings.classList.add('modal')
ModalSettings.setAttribute('id', 'modal_settings')

// Modal_content
let modalContent = document.createElement('div')
modalContent.classList.add('modal-content')
ModalSettings.appendChild(modalContent)



// создать модальное окно
document.body.append(ModalSettings)
