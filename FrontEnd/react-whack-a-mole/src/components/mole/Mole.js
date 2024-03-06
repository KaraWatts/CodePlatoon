import './Mole.css'
import MoleIcon from './Mole.svg'


function Mole(props) {
  if(props.popUp){
  return (
    <div className="den" >
      <img src={MoleIcon} className="Mole" alt="Mole" onClick={props.onClick}/>
    </div>
  )
  }
  return (
    <div className="den">
    </div>
  )
}

export default Mole
