import './App.css'
import BotonEstado from './components/BotonEstado'

function App() {
  return (
    <> 
      <h3>Ejemplo 6: Estilos Condicionales por Props</h3>
      
      {/* 1. Botón en estado activo: Prop booleano en true */}
      <BotonEstado estaActivo={true} />
      
      {/* 2. Botón en estado inactivo: Prop booleano en false */}
      <BotonEstado estaActivo={false} />
      
      {/* Opcional: Probar con contenido children */}
      <BotonEstado estaActivo={true}>Guardar Cambios</BotonEstado>
            
    </>
  )
}
export default App