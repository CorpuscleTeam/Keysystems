function create_icon_path (ext) {
    const upload_file_type = ['avi', 'doc', 'gif', 'jpg', 'mov', 'mp3', 'mp4', 'pdf', 'png', 'xls', 'zip']
    let file_name
    if (upload_file_type.includes(ext)) {
        file_name = ext
    } else {
        file_name = 'file'
    }
    return `../static/site/img/files/${file_name}.svg`
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
    FileImg.setAttribute('src', create_icon_path (data.name.slice(-3)))
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
    FileSize.innerHTML = data['size']
    FileCenter.appendChild(FileSize)

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

function addUpdateFile (parent, arr) {
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
