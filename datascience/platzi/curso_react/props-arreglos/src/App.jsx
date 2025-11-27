import './App.css'
import ListaItems from './components/ListaItems'

function App() {
  const lenguajes = ["Pyrhon", "JavaScript", "PHP", "Vala"];
  return (
    <>
      <div>
        <ListaItems items={lenguajes}/>
      </div>
    </>
  )
}

export default App
