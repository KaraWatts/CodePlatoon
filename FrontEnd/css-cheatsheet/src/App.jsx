import './App.css'

function App() {

  return (
    <>
      <div id="boxes" className='boxContainer'>
        <div className='box'>1</div> {/*position static is the default */}
        <div className='box'>2</div>
        <div className='box'>3</div>
        <div className='box'>4</div>
        <div className='relativebox'>5
          <div className='absolutebox'>6</div> {/*pins obejc to single point on the page*/}
        </div> {/*positions objects relative to parent classes */}
      </div>
    </>
  )
}

export default App
