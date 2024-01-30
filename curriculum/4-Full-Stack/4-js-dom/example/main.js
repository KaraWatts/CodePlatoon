// scripts.js

const favoriteColor = (event) => {
    event.preventDefault()
    const formData = new FormData(event.target)
    const formatData = Object.fromEntries(formData)
    console.log(formatData)
    let output = document.getElementById('output')
    output.innerText = `${formatData.name}s favorite color is ${formatData.color}`
}

// const sayHi = (evt) => {
//   evt.stopPropagation();
//   console.log("hi (inner)");
// };

// const sayHello = (evt) => {
//   console.log("hello (outer)");
// };

// let box = document.getElementById("box")
// box.addEventListener("mouseover" , (event) => {
//     event.target.style.backgroundColor = 'cyan'
// })

// box.addEventListener("mouseout", (event)=> {
//     event.target.style.backgroundColor = 'white'
// })

// const changeColor = (event) => {
//     event.target.style.backgroundColor = 'black'
// }
// const dog = "https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-653001154-e1691965000531.jpg?w=1024"
// const cat = "https://cdn.pixabay.com/photo/2017/11/09/21/41/cat-2934720_1280.jpg"
// const showName = () => {
//     let nameInput = document.getElementById("input-name").value
//     let parent = document.getElementById("output")
//     let img = document.createElement("img")
//     if (nameInput === 'dog'){
//         img.src = dog
//     }
//     else {
//         img.src = cat
//     }
//     parent.appendChild(img)
// }
// console.log("Good Morning")
// headerValue = document.getElementById("headerTitle");
// console.log(headerValue.innerText)
// headerValue.innerText = "GoodBye Victor Platoon"
// console.log(headerValue.innerText);
// console.log(document.body.children[0].children[0].innerText)
// image = document.body.children[4]
// .children[2].children[0].children[1].src
// console.log(image)
