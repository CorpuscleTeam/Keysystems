function pag(parent, allPage) {
    if (allPage > 0) {
        let pag = document.createElement('div')
        pag.classList.add('pag')

        parent.appendChild(pag)

        let pagFlex = document.createElement('div')
        pagFlex.classList.add('pag_flex')
        pag.appendChild(pagFlex)

        // цикл 
        for (let i=1; i<=allPage.length; i++) {
            let num = document.createElement('div')
            num.classList.add('page_item')
            pagFlex.appendChild(num)

            let numLink = document.createElement('a')
            numLink.setAttribute('href', '#') // добавить ссылку
            numLink.innerHTML = i
            num.appendChild(numLink)
        }
        let num_active = document.querySelector('.page_item:first-child')
        num_active.classList.add('page_active')

        let btns = document.querySelectorAll('.page_item')
        for (let btn of btns) {
            btn.onclick = function() {
                document.querySelector('.pag_flex .page_active').classList.remove('page_active')
                this.classList.add('page_active')
            }
        }

        // кнопка "далее"
        let nextPag = document.createElement('div')
        nextPag.classList.add('next_pag_item')
        pagFlex.appendChild(nextPag)

        let nextPagLink = document.createElement('a')
        nextPagLink.setAttribute('href', '#') // добавить ссылку
        nextPagLink.innerHTML = 'Далее &rarr;'
        nextPag.appendChild(nextPagLink)
    }
}

// вызов функции (к странице 4.1 подключен)
// pag(parent, allPage)
