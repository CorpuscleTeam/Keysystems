for(let i=0; i<optionPO.length; i++) {
    let softPO = document.createElement('option')
    // console.log(optionPO)

    softPO.setAttribute('value', optionPO[i]['pk'])
    softPO.innerHTML = optionPO[i]['fields']['title']
    document.querySelector('#reg_progr').appendChild(softPO)
}
