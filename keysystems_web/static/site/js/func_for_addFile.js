function create_icon_path(ext) {
    const upload_file_type = ['avi', 'doc', 'gif', 'jpg', 'mov', 'mp3', 'mp4', 'pdf', 'png', 'xls', 'zip']
    let file_name
    if (upload_file_type.includes(ext)) {
        file_name = ext
    } else {
        file_name = 'file'
    }
    file_path = `../static/site/img/files/${file_name}.svg`
    console.log('file_path')
    console.log(file_path)
    return file_path
}

// создаём строку с размером
function getSizeFileStr(size) {
    let sizeInt = parseInt(size)
    const units = ['байт', 'КБ', 'МБ', 'ГБ'];
    for (let i = 0; i < units.length; i++) {
        if (sizeInt < 1024) {
            return sizeInt.toFixed(2) + ' ' + units[i];
        }
        sizeInt /= 1024;
    }
}


// // эта функция должна нам прогрес-бар оживлять
// function uploadForm(formElement, progressBar) {
//     let xhr = new XMLHttpRequest();
//     let formData = new FormData(formElement); // Собираем все данные формы

//     xhr.open('POST', formElement.action, true);

//     xhr.upload.onprogress = function (event) {
//         if (event.lengthComputable) {
//             let percentComplete = (event.loaded / event.total) * 100;
//             progressBar.style.width = percentComplete + '%';
//         }
//     };

//     xhr.onload = function () {
//         if (xhr.status == 200) {
//             progressBar.style.backgroundColor = 'green'; // успешная загрузка
//         } else {
//             progressBar.style.backgroundColor = 'red'; // ошибка
//         }
//     };

//     xhr.send(formData); // Отправляем данные формы
// }

// прогрессбар
function myTimer(seconds, callback) {
    let startDate = new Date();
    let endDate = new Date();
    endDate = endDate.setSeconds(endDate.getSeconds() + seconds);
    
    let interval = setInterval(() => {
        let currentDate = new Date();
        let leftPercent = Math.trunc((endDate - currentDate) / (endDate - startDate) * 100);
        let passedPercent = +(100 - leftPercent);

        document.querySelector('.progress_fill').style.width = passedPercent + '%';
        document.querySelector('.progress_empty').style.width = leftPercent + '%';

        if (leftPercent <= 0) {
            clearInterval(interval);
            document.querySelector('.progress_empty').style.display = 'none';
            
            // Вызываем колбэк после завершения таймера
            if (typeof callback === 'function') {
                callback();
            }
        }
    }, 1000);
}


// загрузка файла + прогресс бар загрузка файла
function inDnl(parent, data) {
    let inDnlFile = document.createElement('div')
    inDnlFile.classList.add('update_file_btn')
    parent.appendChild(inDnlFile)

    let inDnlFileItem = document.createElement('div')
    inDnlFileItem.classList.add('update_file_item')
    inDnlFile.appendChild(inDnlFileItem)

    // картинка слева
    let inDnlLeft = document.createElement('div')
    inDnlLeft.classList.add('update_file_img')
    inDnlFileItem.appendChild(inDnlLeft)

    let FileImg = document.createElement('img')
    FileImg.setAttribute('src', create_icon_path(data.name.slice(-3)))
    inDnlLeft.appendChild(FileImg)

    // центр - название файла, размер
    let FileCenter = document.createElement('div')
    FileCenter.classList.add('update_file_center')
    inDnlFileItem.appendChild(FileCenter)

    let FileName = document.createElement('p')
    FileName.classList.add('file_in_dnl')
    FileName.innerHTML = data['name']
    FileCenter.appendChild(FileName)

    // прогресс-бар
    let progressBar = document.createElement('div')
    progressBar.classList.add('progress_bar')
    FileCenter.appendChild(progressBar)

    let progressBarFill = document.createElement('div')
    progressBarFill.classList.add('progress_fill')
    progressBar.appendChild(progressBarFill)

    let progressBarEmpty = document.createElement('div')
    progressBarEmpty.classList.add('progress_empty')
    progressBar.appendChild(progressBarEmpty)

    // картинка справа
    let FileRight = document.createElement('button')
    FileRight.classList.add('update_file_del')
    inDnlFileItem.appendChild(FileRight)

    let FileDnl = document.createElement('img')
    FileDnl.setAttribute('src', link)
    FileRight.appendChild(FileDnl)

    // удаление всего
    FileRight.addEventListener('click', (event) => {
        btnFile.remove()
    })

    myTimer(2, () => {
        inDnlFile.remove();
    })
}

// функция для div загруженного файла в заявке
function dnlFile(selector, data) {
    let btnFile = document.createElement('div')
    btnFile.classList.add('update_file_btn')
    selector.appendChild(btnFile)

    let btnFileItem = document.createElement('div')
    btnFileItem.classList.add('update_file_item')
    btnFile.appendChild(btnFileItem)

    // картинка слева
    let FileLeft = document.createElement('div')
    FileLeft.classList.add('update_file_img')
    btnFileItem.appendChild(FileLeft)

    let FileImg = document.createElement('img')
    FileImg.setAttribute('src', create_icon_path(data.name.slice(-3)))
    FileLeft.appendChild(FileImg)

    // центр - название файла, размер
    let FileCenter = document.createElement('div')
    FileCenter.classList.add('update_file_center')
    btnFileItem.appendChild(FileCenter)

    let FileName = document.createElement('p')
    FileName.classList.add('update_file_name')
    FileName.innerHTML = data['name']
    console.log(data)
    FileCenter.appendChild(FileName)

    let FileSize = document.createElement('p')
    FileSize.classList.add('update_file_size')
    // заменил на функцию
    FileSize.innerHTML = getSizeFileStr(data['size'])
    // FileSize.innerHTML = data['size']
    FileCenter.appendChild(FileSize)

    // прогресс-бар
    let progressBarContainer = document.createElement('div')
    progressBarContainer.classList.add('progress-bar-container')
    FileCenter.appendChild(progressBarContainer)

    let progressBar = document.createElement('div')
    progressBar.classList.add('progress-bar')
    progressBarContainer.appendChild(progressBar)

    // картинка справа
    let FileRight = document.createElement('button')
    FileRight.classList.add('update_file_del')
    btnFileItem.appendChild(FileRight)

    let FileDnl = document.createElement('img')
    FileDnl.setAttribute('src', link)
    FileRight.appendChild(FileDnl)

    // удаление всего
    FileRight.addEventListener('click', (event) => {
        btnFile.remove()
    })

}

// кнопка скачать файл

function addUpdateFile(parent, arr) {
    console.log('addUpdateFile')
    console.log(arr)
    let fileUrl = arr['url'] || arr['file_url'];
    let fileName = arr['name'] || arr['filename'];
    let filSize = arr['size'] || arr['file_size'];

    let updateFile = document.createElement('button')
    updateFile.classList.add('update_file_btn')
    parent.appendChild(updateFile)

    // ссылка на скачивание файла
    let updateFileLink = document.createElement('a')

    updateFileLink.setAttribute('href', fileUrl)
    updateFileLink.setAttribute('download', fileName);
    updateFile.appendChild(updateFileLink)

    let updateFileItem = document.createElement('div')
    updateFileItem.classList.add('update_file_item')
    updateFileLink.appendChild(updateFileItem)

    // картинка слева
    let updateFileLeft = document.createElement('div')
    updateFileLeft.classList.add('update_file_img')
    updateFileItem.appendChild(updateFileLeft)

    let updateFileImg = document.createElement('img')
    // добавить переменную
    updateFileImg.setAttribute('src', arr['icon'])
    updateFileLeft.appendChild(updateFileImg)

    // центр - название файла, размер
    let updateFileCenter = document.createElement('div')
    updateFileCenter.classList.add('update_file_center')
    updateFileItem.appendChild(updateFileCenter)

    let updateFileName = document.createElement('p')
    updateFileName.classList.add('update_file_name')
    updateFileName.innerHTML = fileName
    // updateFileName.innerHTML = arr['name']
    updateFileCenter.appendChild(updateFileName)

    let updateFileSize = document.createElement('p')
    updateFileSize.classList.add('update_file_size')
    updateFileSize.innerHTML = filSize
    // updateFileSize.innerHTML = arr['size']
    updateFileCenter.appendChild(updateFileSize)

    // картинка справа
    let updateFileRight = document.createElement('div')
    updateFileRight.classList.add('update_file_dnl')
    updateFileItem.appendChild(updateFileRight)

    let updateFileDnl = document.createElement('img')
    updateFileDnl.setAttribute('src', fileDnl)
    updateFileRight.appendChild(updateFileDnl)
}
