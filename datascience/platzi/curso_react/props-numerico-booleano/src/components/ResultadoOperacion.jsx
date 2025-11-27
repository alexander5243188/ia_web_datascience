const ResultadoOperacion = ({numero, mostrarDoble}) => {
    return(
        <section>
            {
                mostrarDoble ? (
                <p>El doble de {numero} es {numero * 2}</p>) 
                : (
                <p>El número original es: {numero}</p>)
            }                      
        </section>
    )
}

export default ResultadoOperacion;