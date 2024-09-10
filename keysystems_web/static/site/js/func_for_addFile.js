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

// функция для кнопки "скачать файл"
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
    FileCenter.appendChild(FileName)

    let FileSize = document.createElement('p')
    FileSize.classList.add('update_file_size')
    FileSize.innerHTML = data['size']
    FileCenter.appendChild(FileSize)

    // картинка справа
    let FileRight = document.createElement('button')
    FileRight.classList.add('update_file_dnl')
    btnFileItem.appendChild(FileRight)

    let FileDnl = document.createElement('img')
    FileDnl.setAttribute('src', link)
    FileRight.appendChild(FileDnl)

    // удаление всего
    FileRight.addEventListener('click', (event) => {
        btnFile.remove()
    })
}

// 

