// Кнопка закрыть
function btnClose() {
    let ModalRequestClose = document.createElement('div')
    ModalRequestClose.classList.add('modal1_img')
    ModalRequestClose.classList.add('modal-close')

    let modalCloseImg = document.createElement('img')
    modalCloseImg.setAttribute('src', link)
    ModalRequestClose.appendChild(modalCloseImg)

    return ModalRequestClose
}

// Заголовок
function modalTitle(title) {
    let ModalRequestH = document.createElement('h4')
    ModalRequestH.innerHTML = title
    return ModalRequestH
}

// функция создает сообщения
function createMsg(ObjMsg, userId, withHeader = true) {
    let newMsg = document.createElement('div')
    newMsg.classList.add('msg')
    if (userId == ObjMsg['from_user']['id']) {
        newMsg.classList.add('msgFromMe')
    } else {
        newMsg.classList.add('msgFromHim')
    }

    if (withHeader == true) {
        let headerMsg = document.createElement('div')
        headerMsg.classList.add('header_msg')
        newMsg.appendChild(headerMsg)

        let fromMsg = document.createElement('p')
        fromMsg.classList.add('from_msg')
        fromMsg.innerHTML = ObjMsg['from_user']['full_name']
        headerMsg.appendChild(fromMsg)

        let timeMsg = document.createElement('p')
        timeMsg.classList.add('time_msg')
        timeMsg.innerHTML = ObjMsg['time']
        headerMsg.appendChild(timeMsg)
    }

    let contextMsg = document.createElement('div')
    contextMsg.classList.add('context_msg')
    contextMsg.innerHTML = ObjMsg['text']
    newMsg.appendChild(contextMsg)

    return newMsg
}

// функция создает чат
function createChat(selector, arr_message, userId, chatType) {
    let lastUser = 0
    let chat_message = document.createElement('div')
    chat_message.classList.add('chat_msg_item')
    if (chatType == BASE.CLIENT) {
        chat_message.setAttribute('id', idOfChat.clientChat)
    } else {
        chat_message.setAttribute('id', idOfChat.curatorChat)
    }

    // chat_message.setAttribute('id', `area_chat_${arr_message[0]['chat']}`)
    for (let i = 0; i < arr_message.length; i++) {
        let withHeader = true
        if (i > 0 && arr_message[i]['from_user']['id'] == arr_message[i - 1]['from_user']['id']) {
            withHeader = false
        }
        let newMsg = createMsg(arr_message[i], userId, withHeader)
        chat_message.appendChild(newMsg)
        lastUser = arr_message[i]['from_user']['id']
    }

    // let fdf = document.querySelector(selector);
    // fdf.appendChild(chat_message);

    return chat_message
    // chat_message.scrollTop = chat_message.scrollHeight;
}


// функция для списка кураторов
function createCuratorsList(selector, arr) {
    for (let i = 0; i < arr.length; i++) {
        let curatorForRequest = document.createElement('div')
        curatorForRequest.classList.add('curator_item')
        document.querySelector(selector).appendChild(curatorForRequest)

        let curatorItemLeft = document.createElement('div')
        curatorItemLeft.classList.add('curator_item_left')
        curatorForRequest.appendChild(curatorItemLeft)

        let curItemImg = document.createElement('img')
        curItemImg.setAttribute('src', curatorItemImg)
        curatorItemLeft.appendChild(curItemImg)

        let curatorUser = document.createElement('div')
        curatorUser.classList.add('curator_item_center')
        curatorUser.innerHTML = arr[i]['full_name']
        curatorForRequest.appendChild(curatorUser)

        if (arr[i]['id'] == window.userId) {
            let userMe = document.createElement('span')
            userMe.innerHTML = ` (Я)`
            curatorUser.append(userMe)

            let curatorItemRight = document.createElement('a')
            curatorItemRight.setAttribute('href', '#modal_closeFromMe')
            curatorItemRight.classList.add('curator_item_right')
            curatorForRequest.appendChild(curatorItemRight)

            let curItemImgClose = document.createElement('img')
            curItemImgClose.setAttribute('src', link)
            curatorItemRight.appendChild(curItemImgClose)
        }
    }

    // кнопка добавить испольнителей
    let addCurator = document.createElement('a')
    addCurator.setAttribute('href', '#modal_add_curator')
    addCurator.classList.add('btn_add_curator')
    document.querySelector(selector).appendChild(addCurator)

    let addCuratorImg = document.createElement('img')
    addCuratorImg.setAttribute('src', imgPlus)
    addCurator.appendChild(addCuratorImg)
}


function initOrderSocket(roomName, userId) {
    // const roomName = JSON.parse(document.getElementById('room-name').textContent);

    window.chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + roomName
        + '/'
    );
//    window.chatSocket = chatSocket
    // получение сообщений
    window.chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);

        console.log('window.chatSocket.onmessage')
        console.log(data)
        let withHeader = true
        // if (lastUser == data.message.from_user.id) {
        //     withHeader = false
        // }
        // let newMsg = createMsg(data.message, userId, withHeader)
        // let chat_message = document.querySelector('.chat_msg_item')
        // chat_message.appendChild(newMsg)

        if (data.type == 'msg') {

            if (data.message.chat == BASE.CLIENT) {
                if (data.message.from_user.id == window.lastMsgForClientChat) {
                    withHeader = false
                }
                let newMsg = createMsg(data.message, userId, withHeader)
                let chat_message = document.querySelector('#client_chat_item')
                chat_message.appendChild(newMsg)

                // Прокрутка вниз при получении нового сообщения
                chat_message.scrollTop = chat_message.scrollHeight;

                window.lastMsgForClientChat = data.message.from_user.id
            } else {
                if (data.message.from_user.id == window.lastMsgForCuratorChat) {
                    withHeader = false
                }
                let newMsg = createMsg(data.message, userId, withHeader)
                let chat_message = document.querySelector('#curator_chat_item')
                chat_message.appendChild(newMsg)

                // Прокрутка вниз при получении нового сообщения
                chat_message.scrollTop = chat_message.scrollHeight;

                window.lastMsgForCuratorChat = data.message.from_user.id
            }
        }

        else if (data.type == 'edit_curator') {
            createCuratorsList('.curators_of_request', data.curators)
        }

        // lastUser = data.message.from_user.id
    };

    window.chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    // отправка сообщений client_chat
    document.querySelector('#client-msg-input').focus();
    document.querySelector('#client-msg-input').onkeyup = function (e) {
        if (e.key === 'Enter') {  // enter, return
            document.querySelector('#client-msg-submit').click();
        }
    };

    document.querySelector('#client-msg-submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#client-msg-input');
        const message = messageInputDom.value;
        window.chatSocket.send(JSON.stringify({
            'event': 'msg',
            'message': message,
            'tab': window.selectedTab,
            'order_id': window.orderId,
            'user_id': window.userId
        }));
        messageInputDom.value = '';
    };

    // отправка сообщений curator_chat
    document.querySelector('#curator-msg-input').focus();
    document.querySelector('#curator-msg-input').onkeyup = function (e) {
        if (e.key === 'Enter') {  // enter, return
            document.querySelector('#curator-msg-submit').click();
        }
    };

    document.querySelector('#curator-msg-submit').onclick = function (e) {
        const messageInputDom = document.querySelector('#curator-msg-input');
        const message = messageInputDom.value;
        window.chatSocket.send(JSON.stringify({
            'message': message,
            'tab': window.selectedTab,
            'order_id': window.orderId,
            'user_id': window.userId
        }));
        messageInputDom.value = '';
    };
}

// для скачивания файлов (приложены к заявкам)
function btnLdFile(selector, arr) {
    for (let i = 0; i < arr.length; i++) {
        let btnFile = document.createElement('button')
        btnFile.classList.add('update_file_btn')
        document.querySelector(selector).appendChild(btnFile)

        let ldFileLink = document.createElement('a')
        ldFileLink.setAttribute('href', arr[i]['url'])
        ldFileLink.setAttribute('download', arr[i]['filename']);
        btnFile.appendChild(ldFileLink)

        let ldFileLinkItem = document.createElement('div')
        ldFileLinkItem.classList.add('update_file_item')
        ldFileLink.appendChild(ldFileLinkItem)

        // картинка слева
        let ldFileLeft = document.createElement('div')
        ldFileLeft.classList.add('update_file_img')
        ldFileLinkItem.appendChild(ldFileLeft)

        let ldFileImg = document.createElement('img')
        // добавить переменную
        ldFileImg.setAttribute('src', arr[i]['icon'])
        ldFileLeft.appendChild(ldFileImg)

        // центр - название файла, размер
        let ldFileCenter = document.createElement('div')
        ldFileCenter.classList.add('update_file_center')
        ldFileLinkItem.appendChild(ldFileCenter)

        let ldFileName = document.createElement('p')
        ldFileName.classList.add('update_file_name')
        ldFileName.classList.add('file_name_width')
        ldFileName.innerHTML = arr[i]['filename']
        ldFileCenter.appendChild(ldFileName)

        let ldFileSize = document.createElement('p')
        ldFileSize.classList.add('update_file_size')
        ldFileSize.innerHTML = arr[i]['file_size']
        ldFileCenter.appendChild(ldFileSize)

        // картинка справа
        let ldFileRight = document.createElement('div')
        ldFileRight.classList.add('update_file_dnl')
        ldFileLinkItem.appendChild(ldFileRight)

        let ldFileDnl = document.createElement('img')
        ldFileDnl.setAttribute('src', fileDnl)
        ldFileRight.appendChild(ldFileDnl)
    }
}

//// функция для списка кураторов
//function createCuratorsList(selector, arr) {
//    for (let i = 0; i < arr.length; i++) {
//        let curatorForRequest = document.createElement('div')
//        curatorForRequest.classList.add('curator_item')
//        document.querySelector(selector).appendChild(curatorForRequest)
//
//        let curatorItemLeft = document.createElement('div')
//        curatorItemLeft.classList.add('curator_item_left')
//        curatorForRequest.appendChild(curatorItemLeft)
//
//        let curItemImg = document.createElement('img')
//        curItemImg.setAttribute('src', curatorItemImg)
//        curatorItemLeft.appendChild(curItemImg)
//
//        let curatorUser = document.createElement('div')
//        curatorUser.classList.add('curator_item_center')
//        curatorUser.innerHTML = arr[i]['full_name']
//        curatorForRequest.appendChild(curatorUser)
//
//        if (arr[i]['id'] == window.userId) {
//            let userMe = document.createElement('span')
//            userMe.innerHTML = ` (Я)`
//            curatorUser.append(userMe)
//
//            let curatorItemRight = document.createElement('a')
//            curatorItemRight.setAttribute('href', '#modal_closeFromMe')
//            curatorItemRight.classList.add('curator_item_right')
//            curatorForRequest.appendChild(curatorItemRight)
//
//            let curItemImgClose = document.createElement('img')
//            curItemImgClose.setAttribute('src', link)
//            curatorItemRight.appendChild(curItemImgClose)
//        }
//    }
//
//    // кнопка добавить испольнителей
//    let addCurator = document.createElement('a')
//    addCurator.setAttribute('href', '#modal_add_curator')
//    addCurator.classList.add('btn_add_curator')
//    document.querySelector(selector).appendChild(addCurator)
//
//    let addCuratorImg = document.createElement('img')
//    addCuratorImg.setAttribute('src', imgPlus)
//    addCurator.appendChild(addCuratorImg)
//}


// вызывает токен безопасности
function getCSFRT() {
    let name = 'csrftoken'
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Если это cookie с именем 'csrftoken', верните его значение
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// изменяет список кураторов
function clickAddCurator() {

    document.getElementById('btnAddCurator').addEventListener('click', function () {

        // Получаем выбранный элемент
         const selectedOption = document.getElementById('add_curator_1').value;

        // Выполняем нужную функцию
        console.log(selectedOption);
        console.log(window.chatSocket);
         // Отправляем данные на бэкэнд через WebSocket
        window.chatSocket.send(JSON.stringify({
            'event': 'edit_curator',
            'add': selectedOption,
            'order_id': window.orderId,
            'room_name': window.roomName
        }));
    });
}
//<form class="mod_request_form enter_form" id="add_curator" method="post"><p><label for="add_curator" class="required">Выберите исполнителя</label><select name="add_curator" id="add_curator"><option value="4">Меркул Иванович</option><option value="3">Пётр</option></select></p></form><form class="mod_request_form enter_form" id="add_curator" method="post"><p><label for="add_curator" class="required">Выберите исполнителя</label><select name="add_curator" id="add_curator"><option value="4">Меркул Иванович</option><option value="3">Пётр</option></select></p></form>

// создает модальное окно с выбором исполнителей
function modalAddCurators() {
    // обработчик событий для открытия второго окна
    document.querySelector('#statusOrder .btn_add_curator').addEventListener('click', function () {
        // Открываем второе модальное окно
        let modalInstance = M.Modal.getInstance(document.querySelector('#modal_add_curator'));
        modalInstance.open();

        // Выполняем запрос к бэку
        fetch("get-curators", {
            method: "POST", // Указываем метод POST
            headers: {
                "Content-Type": "application/json", // Указываем, что отправляем JSON данные
                "X-CSRFToken": getCSFRT() // Добавляем CSRF токен, если используете Django
            },
            body: JSON.stringify({
                order_id: window.orderId,
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log('data')
                console.log(data)
                // МО добавить исполнителя
                // let modalAddCurator = document.createElement('div')
                // modalAddCurator.setAttribute('id', 'modal_add_curator')
                // modalAddCurator.classList.add('modal')

                // document.body.append(modalAddCurator)

                let modalAddCuratorContent = document.createElement('div')
                modalAddCuratorContent.classList.add('modal-content')
                modalAddCurator.appendChild(modalAddCuratorContent)

                let modalAddCuratorClose = btnClose()
                modalAddCuratorContent.appendChild(modalAddCuratorClose)

                let modalAddCuratorTitle = modalTitle('Добавить исполнителя')
                modalAddCuratorContent.appendChild(modalAddCuratorTitle)

                // Форма
                let formAddCurator = document.createElement('form')
                formAddCurator.classList.add('mod_request_form')
                formAddCurator.classList.add('enter_form')
                formAddCurator.setAttribute('id', 'form_add_curator')
                formAddCurator.setAttribute('method', 'post')
                formAddCurator.innerHTML = getCSFRT()
                modalAddCuratorContent.appendChild(formAddCurator)

                // Выбрать исполнителя
                let addCurator = document.createElement('p')
//                addCurator.id = 'test-id-addCurator'
                formAddCurator.appendChild(addCurator)

                let labelAddCurator = document.createElement('label')
                labelAddCurator.setAttribute('for', 'add_curator')
                labelAddCurator.classList.add('required')
                labelAddCurator.innerHTML = `Выберите исполнителя`
                addCurator.appendChild(labelAddCurator)

                let selectAddCurator = document.createElement('select')
                selectAddCurator.setAttribute('name', 'add_curator')
                selectAddCurator.setAttribute('id', 'add_curator_1')
                addCurator.appendChild(selectAddCurator)

                // добавить цикл с вариантами выбора
                console.log('data.length')
                console.log(data.length)
                for (let i = 0; i < data.length; i++) {
                    console.log(data[i])
                    let optionAddCurator = document.createElement('option')
                    optionAddCurator.setAttribute('value', data[i]['id'])
                    optionAddCurator.innerHTML = data[i]['full_name']
                    selectAddCurator.appendChild(optionAddCurator)
                }

                // футер-кнопки
                let footerAddCurator = document.createElement('div')
                footerAddCurator.classList.add('mod_support_flex')
                modalAddCuratorContent.appendChild(footerAddCurator)

                let btnAddCuratorCancel = document.createElement('a')
                btnAddCuratorCancel.classList.add('btn_support_cancel')
                btnAddCuratorCancel.innerHTML = `Отмена`
                footerAddCurator.appendChild(btnAddCuratorCancel)

                let btnAddCuratorSubmit = document.createElement('button')
                btnAddCuratorSubmit.setAttribute('id', 'btnAddCurator')
                btnAddCuratorSubmit.classList.add('btn_support_submit')
                btnAddCuratorSubmit.innerHTML = `Добавить`
                footerAddCurator.appendChild(btnAddCuratorSubmit)

                clickAddCurator()
            })
            .catch(error => console.error('Error:', error));
    });
}


// функция для кнопки "завершить работу" и изменение статуса
function changeStatusWorkToEnd(btnElem, statusElem) {
    statusElem.classList.replace('status_work_req', 'status_end_req')
    statusElem.textContent = 'выполнено'

    btnElem.classList.replace('btn_work_req', 'btn_end_req')
    btnElem.textContent = 'завершено'

    let btnAddCurator = document.querySelector('.btn_add_curator')
    btnAddCurator.classList.replace('btn_add_curator', 'btn_end_curator')
}
// функция для кнопки "взять в работу" и изменение статуса
function changeStatusNewToWork() {
    document.querySelector('.btn_new_req').addEventListener('click', function () {
        let statusElem = document.querySelector('.status_new_req')
        let btnElem = this

        statusElem.classList.replace('status_new_req', 'status_work_req')
        statusElem.textContent = 'в работе'

        btnElem.classList.replace('btn_new_req', 'btn_work_req')
        btnElem.textContent = 'Завершить работу'

        btnElem.removeEventListener('click', changeStatusNewToWork)
        btnElem.addEventListener('click', function () {
            changeStatusWorkToEnd(btnElem, statusElem)
        })
    })
}


