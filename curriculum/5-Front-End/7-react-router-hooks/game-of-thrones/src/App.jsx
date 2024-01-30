import { useEffect, useState } from 'react'
import Header from './components/Header'
import './App.css'
import { Outlet } from 'react-router-dom'

// function App() {
const App = () => {
  const [favorites, setFavorites] = useState([])

  useEffect(()=>{
    console.log(favorites)
  }, [favorites])

  return (
    <>
      <Header favorites={favorites} />
      <Outlet context={{favorites, setFavorites}}/>
    </>
  )
}

export default App
