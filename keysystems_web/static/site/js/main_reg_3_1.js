for(let i=0; i<optionPO.length; i++) {
    let softPO = document.createElement('option')
    // console.log(optionPO[i])

    softPO.setAttribute('value', optionPO[i]['id'])
    softPO.innerHTML = optionPO[i]['title']
    document.querySelector('#reg_progr').appendChild(softPO)
}
