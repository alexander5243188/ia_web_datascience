
import './App.css'

function App() {
  const items = ["Python", "JavaScript", "PHP", "Vala"]; 
  return (
    <> 
      <div>
        <h2>Lenguajes de programación</h2>
        <ul>
          {
            items.map((item, index) => (
              <li key={index}>{item}</li>
            ))
          }
        </ul>            
      </div>    
    </>
  )
}

export default App
