// отображене ИНН в шапке десктоп
let headerInn = document.createElement('p')
headerInn.classList.add('menu_INN')
headerInn.innerHTML = `ИНН: ${mainData['inn']}`

document.querySelector('.header_client_menu_ul li:first-child').appendChild(headerInn)

// отображение ИНН в сайднав
let sidnavInn = headerInn.cloneNode(true)
document.querySelector('.sidnav_li_inn').appendChild(sidnavInn)

// отображение названия учр-я в шапке десктоп
let headerInst = document.createElement('p')
headerInst.innerHTML = mainData['institution']

document.querySelector('.header_client_menu_ul li:first-child').appendChild(headerInst)

// отображение названия учр-я в сайднав
let sidenavInst = headerInst.cloneNode(true)
document.querySelector('.sidnav_li_inn').appendChild(sidenavInst)
