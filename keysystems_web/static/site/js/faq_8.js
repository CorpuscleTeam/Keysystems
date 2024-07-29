let faq_div = document.createElement('div')
faq_div.classList.add('question-items')

for(let i=0; i<faq.length; i++) {
    console.log(faq[i])
}

document.querySelector('.page_flex_body').appendChild(faq_div)
