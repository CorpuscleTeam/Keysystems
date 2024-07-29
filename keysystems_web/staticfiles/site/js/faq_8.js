/* {
    "model": "client_app.faq",
    "pk": 4,
    "fields": {
        "created_at": "2024-07-26T15:37:08.076Z",
        "updated_at": "2024-07-26T15:37:08.076Z",
        "question": "Начальник отдела консолидированной",
        "answer": "Программный комплекс «Бюджет-СМАРТ» предназначен для автоматизации процессов составления, анализа и исполнения бюджета субъекта и бюджетов муниципальных образований.",
        "is_active": true
    }
} */

let faqDiv = document.createElement('div')
faqDiv.classList.add('question_flex')

for(let i=0; i<faq.length; i++) {
    // console.log(faq[i])
    let faqItem = document.createElement('details')
    faqItem.classList.add('faq_item')
    faqDiv.appendChild(faqItem)

    let faqSummary = document.createElement('summary')
    faqSummary.classList.add('faq_h5')
    faqSummary.classList.add('question_h3')
    faqSummary.innerHTML = faq[i]['fields']['question']
    faqItem.appendChild(faqSummary)

    let faqP = document.createElement('p')
    faqP.classList.add('faq_p')
    faqP.classList.add('question_p')
    faqP.innerHTML = faq[i]['fields']['answer']
    faqItem.appendChild(faqP)
}

document.querySelector('.page_flex_body').appendChild(faqDiv)
