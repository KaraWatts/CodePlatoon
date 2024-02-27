console.log(fetch("https://geek-jokes.sameerkumar.website/api?format=json"))

const getJoke = async() => {
    let response = await fetch("https://geek-jokes.sameerkumar.website/api?format=json")
    let responseData = await response.json()
    while (responseData['joke'].length > 42){
        response = await fetch("https://geek-jokes.sameerkumar.website/api?format=json")
        responseData = await response.json()
    }
document.getElementById('joke').innerHTML = `>  ${responseData['joke']}`
console.log(responseData['joke'])

}

getJoke()