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

// загрузить файл
let updateFile = document.createElement('div')
updateFile.classList.add('update_file_item')
updateFiles_grid.appendChild(updateFile)

// картинка слева
let updateFileLeft = document.createElement('div')
updateFileLeft.classList.add('update_file_img')
updateFile.appendChild(updateFileLeft)

let updateFileImg = document.createElement('img')
updateFileImg.setAttribute('src', fileImg)
updateFileLeft.appendChild(updateFileImg)

// картинки центр
let updateFileCenter = document.createElement('div')
updateFileCenter.classList.add('update_file_center')
updateFile.appendChild(updateFileCenter)

let updateFileName = document.createElement('p')
updateFileName.classList.add('update_file_name')
updateFileCenter.appendChild(updateFileName)

