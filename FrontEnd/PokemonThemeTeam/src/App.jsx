import axios from 'axios'
import './App.css'
import { colours } from './pokemon-type-colors'

function App() {
  let pokemonID = null
  let firstPokemon = null
  let pokemonType = null
 

  const setPokemonID = (limit = 1000) => {
    pokemonID = Math.floor(Math.random()*limit) + 1
  }
  


  const getPokemon = async (e) => {
    e.preventDefault()
    if (document.getElementById('images')){
      document.getElementById('images').replaceChildren();
    }
    setPokemonID()
    try {
      const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemonID}`)
      const data = response.data
      firstPokemon = {name: data.name, url: data.sprites.front_shiny}
      pokemonType = data.types[0].type.name
      document.getElementById('type').innerHTML = `Type: ${pokemonType}`
      let typeUrl = data.types[0].type.url
      buildTeam(typeUrl)
    } catch (error) {
      console.log(error.toJSON)
    }
  }

  const buildTeam = async (type) => {
    const appImages = document.getElementById('images')
    try {
      const fullResponse = await axios.get(`${type}`)
      const allData = fullResponse.data.pokemon
      let idList = []
      while (idList.length < 5){
        setPokemonID(allData.length)
        if (!idList.includes(allData[pokemonID-1]) && allData[pokemonID-1]['pokemon']['name'] !== firstPokemon['name']){
          idList.push(allData[pokemonID-1])
        }
      }

      const firstCard = document.createElement('div')
      firstCard.setAttribute('class', 'pokemon')
      firstCard.setAttribute("style", `background-color : ${colours[pokemonType]};`)
      const newimage = document.createElement('img')
      newimage.setAttribute('src', firstPokemon.url)
      const firstName = document.createElement('p')
      firstName.innerHTML = firstPokemon.name
      firstCard.appendChild(newimage)
      firstCard.appendChild(firstName)


      const pokemonTeam = idList.map(async (pokemon) => {
        const pokemonResponse = await axios.get(pokemon.pokemon.url);
        const pokemonData = pokemonResponse.data;
        const pokemonCard = document.createElement('div');
        pokemonCard.setAttribute('class', 'pokemon')
        pokemonCard.setAttribute("style", `background-color : ${colours[pokemonType]};`)
        const image = document.createElement('img');
        image.setAttribute('src', pokemonData.sprites.front_shiny);
        const pokemonName = document.createElement('p');
        pokemonName.innerHTML = pokemonData.name
        pokemonCard.appendChild(image)
        pokemonCard.appendChild(pokemonName)

        return pokemonCard
      })

      const pokemonImages = [firstCard, ...await Promise.all(pokemonTeam)];
      console.log(pokemonImages)
    
      
      pokemonImages.forEach(image => {
        appImages.appendChild(image)
      })

      
    } catch (er) {
      console.log(er)
    }
  }
  

  return (
    <>
      <img id="title" src="https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pokémon_logo.svg" />
      <div id="images" className="images">
      </div>
      <p id='type'></p>
      <div className="card">
        <button onClick={(e) => getPokemon(e)}>
          Summon a Team
        </button>
      </div>
    </>
  )
}

export default App
