// const sendARequest = () => {
//     let request = (method = 'POST', endpoint = "app.com/students", data = {
//         'first_name':'Francisco',
//         'last_name':'Avila',
//         'age': 54,
//         'subject':3
//     }) 
//     let request2 = (
//         method = 'POST',
//         endpoint = "app.com/students?first_name=Francisco&last_name=Avila&age=54&subject=3"
//     )
// }

const getStudents = async() => {
    let response = await fetch("http://127.0.0.1:5000/students")
    let data = await response.json()
    let ul = document.getElementById("student-list")
    for (student of data){
        let li = document.createElement("li")
        li.innerText = `Student Name: ${student.first_name}`
        ul.appendChild(li) 
    }
}

const getPokemon = async() => {
    let response = await fetch("https://pokeapi.co/api/v2/pokemon/charizard")
    let data = await response.json()
    let pokemonPhoto = data.sprites.front_default
    // let div = document.createElement('div')
    // div.id = 'image-holder'
    // let img = document.createElement("img")
    // let img = document.getElementById("pokemonImg")
    img.src = pokemonPhoto
    // img.id = 'pokemonImg'
    // div.appendChild(img)
    // document.body.appendChild(div)
}
getStudents()
getPokemon()