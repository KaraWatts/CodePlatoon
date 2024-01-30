import tasks from "./data/tasks.json"
import "./App.css";

// every guess submitted an li tag should be added
function App() {
  let guesses = []
  const randomNumber = Math.floor(Math.random() * 50) + 1

  const takeAGuess = (e) => {
    e.preventDefault()
    let guess = Number(document.getElementById("guess").value)
    let output = document.getElementById("output")
    if (guess === randomNumber){
      output.innerHTML = "<h1>You Won!</h1>"
    }
    else{
      guesses.push(guess)
      if (guess > randomNumber){
        output.innerText = 'Too High'
      }
      else{
        output.innerText = 'Too Low'
      }
      let li = document.createElement("li")
      li.innerText = guess
      document.getElementById("guess-taken").appendChild(li)
    }
  }
  return (
    <>
      <h1>Guess the Number</h1>
      <form onSubmit={(e)=>takeAGuess(e)}>
        <input type="number" id="guess" />
        <button type="submit">Submit</button>
      </form>
      <p id="output"></p>
      <ul id="guess-taken">
        {tasks.map((task)=>(
          <li>{task.task}</li>
        ))}
      </ul>
    </>
  );
}

export default App;
