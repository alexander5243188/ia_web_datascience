import './App.css'
import TarjetaUsuario from './components/TarjetaUsuario'

function App() {
  const usuario = {
    nombre: 'Alicia Pérez',
    edad: 28,
    email: 'alicia.perez@ejemplo.com',
  };

  return (
    <>      
      <div className="card">        
        <TarjetaUsuario usuario={usuario}/>
      </div>      
    </>
  )
}

export default App
