import './App.css'
import ResultadoOperacion from './components/ResultadoOperacion'

function App() {
  return (
    <>
      <div>        
        <ResultadoOperacion numero = {2} mostrarDoble = {false} />
      </div>
      
      <div className="card">      
        <ResultadoOperacion numero = {2} mostrarDoble = {true} />
      </div>      
    </>
  )
}

export default App
