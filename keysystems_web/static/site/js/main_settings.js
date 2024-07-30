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

let inputHiddenSetting = document.createElement('input')
inputHiddenSetting.setAttribute('type', 'hidden')
inputHiddenSetting.setAttribute('value', 'setting')
inputHiddenSetting.setAttribute('name', 'type_form')
formSettings.appendChild(inputHiddenSetting)

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
inputSettingsINN.setAttribute('value', inn)
inputSettingsINN.setAttribute('readonly', 'readonly')
inputSettingsINN.setAttribute('tabindex', '-1')
inputSettingsINN.classList.add('not_active_input')
formSettingsINN.appendChild(inputSettingsINN)

// Наименование - не активная
let formSettingsName = document.createElement('p')
formSettings.appendChild(formSettingsName)

let labelSettingsName = document.createElement('label')
labelSettingsName.setAttribute('for', 'settings_name')
labelSettingsName.classList.add('not_active')
labelSettingsName.innerHTML = `Наименование `
formSettingsName.appendChild(labelSettingsName)

let inputSettingsName = document.createElement('input')
inputSettingsName.setAttribute('name', 'settings_name')
inputSettingsName.setAttribute('id', 'settings_name')
inputSettingsName.setAttribute('value', institution)
inputSettingsName.setAttribute('readonly', 'readonly')
inputSettingsName.setAttribute('tabindex', '-1')
inputSettingsName.classList.add('not_active_input')
formSettingsName.appendChild(inputSettingsName)

// Регион - не активная
let formSettingsReg = document.createElement('p')
formSettings.appendChild(formSettingsReg)

let labelSettingsReg = document.createElement('label')
labelSettingsReg.setAttribute('for', 'settings_reg')
labelSettingsReg.classList.add('not_active')
labelSettingsReg.innerHTML = `Район `
formSettingsReg.appendChild(labelSettingsReg)

let inputSettingsReg = document.createElement('input')
inputSettingsReg.setAttribute('name', 'settings_reg')
inputSettingsReg.setAttribute('id', 'settings_reg')
inputSettingsReg.setAttribute('value', region)
inputSettingsReg.setAttribute('readonly', 'readonly')
inputSettingsReg.setAttribute('tabindex', '-1')
inputSettingsReg.classList.add('not_active_input')
formSettingsReg.appendChild(inputSettingsReg)

// ПО - функция записана в main_create_request.js
let formSettingsTypeSoft = chooseSoft()
formSettings.appendChild(formSettingsTypeSoft)

// Почта - озательное для заполнения
let formSettingsEmail = document.createElement('p')
formSettings.appendChild(formSettingsEmail)

let labelSettingsEmail = document.createElement('label')
labelSettingsEmail.setAttribute('for', 'settings_email')
labelSettingsEmail.classList.add('required')
labelSettingsEmail.innerHTML = `Почта `
formSettingsEmail.appendChild(labelSettingsEmail)

let inputSettingsEmail = document.createElement('input')
inputSettingsEmail.setAttribute('name', 'settings_email')
inputSettingsEmail.setAttribute('id', 'settings_email')
inputSettingsEmail.setAttribute('type', 'email')
formSettingsEmail.appendChild(inputSettingsEmail)

//  ответственный - обязательно для заполнения
let formSettingsResponsible = document.createElement('p')
formSettings.appendChild(formSettingsResponsible)

let labelSettingsResponsible = document.createElement('label')
labelSettingsResponsible.setAttribute('for', 'settings_responsible')
labelSettingsResponsible.classList.add('required')
labelSettingsResponsible.innerHTML = `Ответственный `
formSettingsResponsible.appendChild(labelSettingsResponsible)

let inputSettingsResponsible = document.createElement('input')
inputSettingsResponsible.setAttribute('name', 'settings_responsible')
inputSettingsResponsible.setAttribute('id', 'settings_responsible')
formSettingsResponsible.appendChild(inputSettingsResponsible)

// Телефон - обязательно для заполнения
let formSettingsPhone = document.createElement('p')
formSettings.appendChild(formSettingsPhone)

let labelSettingsPhone = document.createElement('label')
labelSettingsPhone.setAttribute('for', 'settings_phone')
labelSettingsPhone.classList.add('required')
labelSettingsPhone.innerHTML = `Телефон `
formSettingsPhone.appendChild(labelSettingsPhone)

let inputSettingsPhone = document.createElement('input')
inputSettingsPhone.setAttribute('name', 'settings_phone')
inputSettingsPhone.setAttribute('id', 'settings_phone')
inputSettingsPhone.setAttribute('type', 'tel')
formSettingsPhone.appendChild(inputSettingsPhone)

// Кнопка "Сохранить изменения" - функция записана в main_create_request.js
// let btnSubmitSettings = form_btn_submit(`Сохранить изменения`)
// formSettings.appendChild(btnSubmitSettings)

let btnSubmitSettings = document.createElement('button')
btnSubmitSettings.classList.add('enter_button')
btnSubmitSettings.innerHTML = `Сохранить изменения`
formSettings.appendChild(btnSubmitSettings)

// создать модальное окно
document.body.append(ModalSettings)
