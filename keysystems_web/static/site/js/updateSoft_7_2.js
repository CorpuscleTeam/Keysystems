console.log(updateSoft72)


let pageH2 = document.createElement('h2')
pageH2.classList.add('page_body_h2')
pageH2.innerHTML = updateSoft72['soft']

document.querySelector('.page_flex_body').appendChild(pageH2)

let updateContent = document.createElement('p')
updateContent.classList.add('page_news_content')
updateContent.innerHTML = updateSoft72['description']

document.querySelector('.page_flex_body').appendChild(updateContent)

// футер - список файлов - грид
let updateFiles_grid = document.createElement('div')
updateFiles_grid.classList.add('update_files_grid')
document.querySelector('.page_flex_body').appendChild(updateFiles_grid)

for (let i = 0; i < updateSoft72['update_files'].length; i++) {
    // загрузить файл
    let updateFile = document.createElement('button')
    updateFile.classList.add('update_file_btn')
    updateFiles_grid.appendChild(updateFile)

    // ссылка на скачивание файла
    let updateFileLink = document.createElement('a')
    updateFileLink.setAttribute('href', updateSoft72['update_files'][i]['url'])
    updateFileLink.setAttribute('download', updateSoft72['update_files'][i]['name']);
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
    updateFileImg.setAttribute('src', updateSoft72['update_files'][i]['icon'])
    updateFileLeft.appendChild(updateFileImg)

    // центр - название файла, размер
    let updateFileCenter = document.createElement('div')
    updateFileCenter.classList.add('update_file_center')
    updateFileItem.appendChild(updateFileCenter)

    // let updateCenterItem = document.createElement('div')
    // updateCenterItem.classList.add('update_center_item')
    // updateFileCenter.appendChild(updateCenterItem)

    let updateFileName = document.createElement('p')
    updateFileName.classList.add('update_file_name')
    updateFileName.innerHTML = updateSoft72['update_files'][i]['name']
    updateFileCenter.appendChild(updateFileName)

    let updateFileSize = document.createElement('p')
    updateFileSize.classList.add('update_file_size')
    updateFileSize.innerHTML = updateSoft72['update_files'][i]['size']
    updateFileCenter.appendChild(updateFileSize)

    // картинка справа
    let updateFileRight = document.createElement('div')
    updateFileRight.classList.add('update_file_dnl')
    updateFileItem.appendChild(updateFileRight)

    let updateFileDnl = document.createElement('img')
    updateFileDnl.setAttribute('src', fileDnl)
    updateFileRight.appendChild(updateFileDnl)
}

