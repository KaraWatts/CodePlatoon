import { useState } from 'react'
import { useEffect } from 'react';
import './App.css'
import { wordBank } from './data/wordbank.js'
// import gallows from 



function App() {
  // const [words, newWord] = useState(wordBank);
  const [word, setWord] = useState(false)
  
  useEffect(() => {
    let selectedWord = wordBank[(Math.floor(Math.random()* wordBank.length) - 1)];
    selectedWord.split('');
    console.log(selectedWord)
  }, [word])
  // let attempts = 6;
  // let guessedLetters = [];
  return (
    <>
    <div>
      <button onClick={() => setWord(!word)}>Generate Word</button>
    </div>
    <div className='blanks'>
      {/* {selectedWord.map} */}
      <div className="letters">
        <p>A</p>
      </div>
    </div>
    </>
  )
}

export default App
