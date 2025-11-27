import './App.css'
import ContenedorConBorde from './components/ContenedorConBorde'

function App() {
  const miContenido = (
  <>
    <p>Este parrafo es pasado como **childern** al contenedor</p>
    <button onClick={()=> alert('¡Funciona!')}>Boton de prueba.</button>
    <small>La magia del prop children.</small>
  </>);
  return (
    <>
      <div>
        <ContenedorConBorde titulo={"Programando en React"}>{miContenido}</ContenedorConBorde>
      </div>
    </>
  )
}

export default App
