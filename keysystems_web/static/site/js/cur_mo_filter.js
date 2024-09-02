document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });

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

let formFilter = document.createElement('form')
formFilter.classList.add('mod_request_form')
formFilter.classList.add('enter_form')
formFilter.setAttribute('id', 'form_filter')
formFilter.setAttribute('method', 'post')
modalFilterContent.appendChild(formFilter)

// сортировка по дате
let sort = document.createElement('p')
formFilter.appendChild(sort)

let labelSort = document.createElement('label')
labelSort.setAttribute('for', 'sort')
labelSort.innerHTML = 'Сортировать по дате'
sort.appendChild(labelSort)

let selectSort = document.createElement('select')
selectSort.setAttribute('name', 'sort')
selectSort.setAttribute('id', 'sort')
sort.appendChild(selectSort)

let optionSort1 = document.createElement('option')
optionSort1.setAttribute('value', 'optionSort1')
optionSort1.innerHTML = 'Сначала новые'
selectSort.appendChild(optionSort1)

let optionSort2 = document.createElement('option')
optionSort2.setAttribute('value', 'optionSort2')
optionSort2.innerHTML = 'Сначала старые'
selectSort.appendChild(optionSort2)

// ИНН
let innFilter = document.createElement('p')
formFilter.appendChild(innFilter)

let labelInnFilter = document.createElement('label')
labelInnFilter.setAttribute('for', 'inn_filter')
labelInnFilter.innerHTML = 'ИНН'
innFilter.appendChild(labelInnFilter)

let selectInnFilter = document.createElement('select')
selectInnFilter.setAttribute('name', 'inn_filter')
selectInnFilter.setAttribute('id', 'inn_filter')
innFilter.appendChild(selectInnFilter)

    // добавить объект
for(let i=0; i<Arr.length; i++) {
    let optionInnFilter = document.createElement('option')
    optionInnFilter.setAttribute('value', 'Arr[i]') 
    optionInnFilter.innerHTML = Arr[i]
    selectInnFilter.appendChild(optionInnFilter)
}

// Кураторы
let curatorFilter = document.createElement('p')
formFilter.appendChild(curatorFilter)

let labelCuratorFilter = document.createElement('label')
labelCuratorFilter.setAttribute('for', 'curator_filter')
labelCuratorFilter.innerHTML = 'Кураторы'
curatorFilter.appendChild(labelCuratorFilter)

let selectCuratorFilter = document.createElement('select')
selectCuratorFilter.setAttribute('name', 'curator_filter')
selectCuratorFilter.setAttribute('id', 'curator_filter')
curatorFilter.appendChild(selectCuratorFilter)

    // добавить объект
for(let i=0; i<Arr.length; i++) {
    let optionCuratorFilter = document.createElement('option')
    optionCuratorFilter.setAttribute('value', 'Arr[i]')
    optionCuratorFilter.innerHTML = Arr[i]
    selectCuratorFilter.appendChild(optionCuratorFilter)
}

// Район
let districtFilter = document.createElement('p')
formFilter.appendChild(districtFilter)

let labelDistrictFilter = document.createElement('label')
labelDistrictFilter.setAttribute('for', 'district_filter')
labelDistrictFilter.innerHTML = 'Район'
districtFilter.appendChild(labelDistrictFilter)

let selectDistrictFilter = document.createElement('select')
selectDistrictFilter.setAttribute('name', 'district_filter')
selectDistrictFilter.setAttribute('id', 'district_filter')
districtFilter.appendChild(selectDistrictFilter)

    // добавить объект
for(let i=0; i<Arr.length; i++) {
    let optionDistrictFilter = document.createElement('option')
    optionDistrictFilter.setAttribute('value', 'Arr[i]')
    optionDistrictFilter.innerHTML = Arr[i]
    selectDistrictFilter.appendChild(optionDistrictFilter)
}

// ПО
let softFilter = document.createElement('p')
formFilter.appendChild(softFilter)

let labelSoftFilter = document.createElement('label')
labelSoftFilter.setAttribute('for', 'soft_filter')
labelSoftFilter.innerHTML = 'Програмное обеспечение'
softFilter.appendChild(labelSoftFilter)

let selectSoftFilter = document.createElement('select')
selectSoftFilter.setAttribute('name', 'soft_filter')
selectSoftFilter.setAttribute('id', 'soft_filter')
softFilter.appendChild(selectSoftFilter)

    // добавить объект
for(let i=0; i<Arr.length; i++) {
    let optionSoftFilter = document.createElement('option')
    optionSoftFilter.setAttribute('value', 'Arr[i]')
    optionSoftFilter.innerHTML = Arr[i]
    selectSoftFilter.appendChild(optionSoftFilter)
}

// кнопка
let btnSubmitFilter = document.createElement('button')
btnSubmitFilter.classList.add('submit_request')
btnSubmitFilter.innerHTML = 'Применить'
formFilter.appendChild(btnSubmitFilter)
