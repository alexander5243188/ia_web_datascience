//    Añadir botón que muestre la división de los dos números introducidos.

import React, { useState } from "react";

const Calculadora = () => {
    const[numero1, setnumero1] = useState(0)
    const[numero2, setnumero2] = useState(0)

    const[resultadoSuma, setresultadoSuma] = useState(0)
    const[resultadoResta, setresultadoResta] = useState(0)
    const[resultadoMultipicacion, setresultadoMultiplicacion] = useState(0)
    const[resultadoDivision, setresultadoDivision] = useState(0)

    const onChangeNum1 = event => {setnumero1(event.target.value)}
    const onChangeNum2 = event => {setnumero2(event.target.value)}
    //const onChangeNum1 = event => {setnumero1(parseFloat(event.target.value) || 0);}
    //const onChangeNum2 = event => {setnumero2(parseFloat(event.target.value) || 0);}

    const iniciar = () =>{
        suma()
        resta()
        multiplicacion()
        division()  
    }
    const suma = () => {        
        const resultadoSuma = parseFloat(numero1) + parseFloat(numero2)
        setresultadoSuma(resultadoSuma)
    }
    const resta = () => {
        const resultadoResta = parseFloat(numero1) - parseFloat(numero2)
        setresultadoResta(resultadoResta)
    }
    const multiplicacion = () => {
        const resultado = parseFloat(numero1) * parseFloat(numero2)
        setresultadoMultiplicacion(resultado)
    }
    const division = () => {
        const resultado = numero2 !== 0 ? parseFloat(numero1) / parseFloat(numero2) : 'Error'        
        setresultadoDivision(resultado)
    }

    return(
        <>
            <h2>Caluladora</h2>
            <input type="text" id="num1" onChange={onChangeNum1} />
            <input type="text" id="num2" onChange={onChangeNum2} />

            <button onClick={iniciar}>Calcula</button>
            <h3> {numero1} + {numero2} = {resultadoSuma}</h3>
            <h3> {numero1} - {numero2} = {resultadoResta}</h3>
            <h3> {numero1} * {numero2} = {resultadoMultipicacion}</h3>
            <h3> {numero1} / {numero2} = {resultadoDivision}</h3>
        </>
    )
}

export default Calculadora;