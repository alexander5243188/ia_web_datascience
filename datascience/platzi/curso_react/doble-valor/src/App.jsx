// Mostrar el doble valor de nota
import './App.css'
import React, {useState} from 'react'

function App() {  
  const [nota, setNota] = useState('')
  const [dobleNota, setDobleNota] = useState(0)
  
  const comprobarNota = (event) => {
    const inputValue = event.target.value    
    setNota(inputValue)
    const numero = parseFloat(inputValue)
    if (!isNaN(numero)){
      setDobleNota(numero * 2)
    } else {
      setDobleNota(0)
    }
  }


  return (
    <>
      <h2>Comprobador de notas</h2>
      <input type="text" id='nota' value={nota} onChange={comprobarNota}/>
      <p>La nota ingresada es: {nota === '' ? '...' : nota}</p>
      <p>El doble del valor de la {nota} es {dobleNota}</p>
    </>
  )
}

export default App
