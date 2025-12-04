import React from "react";

const Formulario = () => {
    const [fruta, setFruta] = React.useState('')
    const [descripcion, setDescripcion] = React.useState('')
    const [lista, setLista] = React.useState([])
        
    const guardarDatos = (e) => {
        e.preventDefault()

        if(!fruta.trim()){
            console.log('esta vacia fruta')
            return
        }

        if(!descripcion.trim()){
            console.log('Esta vacia descripcion');
            return            
        }
        console.log('procesando datos....' + fruta + descripcion);

        setLista([
            ...lista,
            {nombraFruta: fruta, nombreDescripcion: descripcion}
        ])

        e.target.reset()
        setFruta('')
        setDescripcion('')
        
    }
    return(
        <>
            <h2>Formulario</h2>
            <form action="" onSubmit={guardarDatos}>
                <input type="text" placeholder="Ingrese fruta" className="" onChange={ (e) => setFruta(e.target.value)} />
                <input type="text" placeholder="Ingrese descripcion" className="" onChange={ e => setDescripcion(e.target.value)} />
                <button type="submit">Agregar</button>               
            </form>
            <ul>
                {
                    lista.map((item, index) => (
                        <li key={index}>{item.nombraFruta} - {item.nombreDescripcion}</li>))
                }
            </ul>
        </>
    )
}

export default Formulario;