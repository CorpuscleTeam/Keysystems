function reg_error(selector, text) {
    if(selector) {
        let input = document.getElementById(selector)
        if(input){
            input.classList.add('border_error')

            let text_er = document.createElement('span')
            text_er.classList.add('text_error')
            text_er.innerHTML = text
            input.insertAdjacentElement('afterend', text_er)
        }
    }
}

reg_error(type_error, text_error)
