document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });

//   Модальное окно Настройки "Settings"

let ModalSettings = document.createElement('div')
ModalSettings.classList.add('modal')
// ModalSettings.classList.add('modal_setting')
ModalSettings.setAttribute('id', 'modal_settings')

// Modal_content
let settingContent = document.createElement('div')
settingContent.classList.add('modal-content')
ModalSettings.appendChild(settingContent)

// Кнопка закрыть
let ModalSettingsClose = document.createElement('div')
ModalSettingsClose.classList.add('modal1_img')
ModalSettingsClose.classList.add('modal-close')
settingContent.appendChild(ModalSettingsClose)

let ModalSettingsImg = document.createElement('img')
ModalSettingsImg.setAttribute('src', link)
ModalSettingsClose.appendChild(ModalSettingsImg)

// Заголовок
let ModalSettingsH = document.createElement('h4')
ModalSettingsH.innerHTML = 'Настройки'
settingContent.appendChild(ModalSettingsH)

// Форма
let formSettings = document.createElement('form')
formSettings.classList.add('mod_settings_form')
formSettings.setAttribute('method', 'post')
formSettings.innerHTML = tokenForForm
settingContent.appendChild(formSettings)

// ИНН - не активная
let formSettingsINN = document.createElement('p')
formSettings.appendChild(formSettingsINN)

let labelSettingsINN = document.createElement('label')
labelSettingsINN.setAttribute('for', 'settings_inn')
labelSettingsINN.classList.add('not_active')
labelSettingsINN.innerHTML = `ИНН`
formSettingsINN.appendChild(labelSettingsINN)

let inputSettingsINN = document.createElement('input')
inputSettingsINN.setAttribute('name', 'settings_inn')
inputSettingsINN.setAttribute('id', 'settings_inn')
inputSettingsINN.setAttribute('value', institution)
inputSettingsINN.setAttribute('readonly', 'readonly')
inputSettingsINN.setAttribute('tabindex', '-1')
inputSettingsINN.classList.add('not_active_input')
formSettingsINN.appendChild(inputSettingsINN)

// Наименование - не активная
let formSettingsName = document.createElement('p')
formSettings.appendChild(formSettingsName)

let 

// создать модальное окно
document.body.append(ModalSettings)
