import './App.css'
import Card from './components/Card'

function App() {

  return (
    <>
      <div>        
        <h1>Reutilizando componentes</h1>
        <h3>Props pasa información de un componnete padre a uno hijo</h3>
      </div>      
      <div className="card">
        <Card title={"Card 1"} description={"Esta es una descripción"}/>        
      </div>
      
    </>
  )
}

export default App
