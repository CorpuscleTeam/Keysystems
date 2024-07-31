document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

let modalApplicationStatus = document.createElement('div')
modalApplicationStatus.setAttribute('id', 'statusOrder')
modalApplicationStatus.classList.add('modal')

let modalApplicationStatusContent = document.createElement('div')
modalApplicationStatusContent.classList.add('modal-content')
modalApplicationStatus.appendChild(modalApplicationStatusContent)

let modASClose = btnClose()
modalApplicationStatusContent.appendChild(modASClose)

document.body.append(modalApplicationStatus)
