import React, {Fragment, useState} from "react";

const Lista = () => {
    const[numeros, setNumeros] = useState([1,2,3,4,5,6])
    const[tiempo, setTiempo] = useState(1)

    const aumentar = () =>{
        setTiempo(tiempo + 1)
        setNumeros([...numeros, tiempo+6])
    }
    return(
        <>
            <button onClick={aumentar}>Aumentar</button>            
            <p>Tiempo: {tiempo}</p>
            {
                numeros.map((item, index) => <li key={index}> {item} - {index} Indice</li>)
            }
        </>
    )
}

export default Lista;