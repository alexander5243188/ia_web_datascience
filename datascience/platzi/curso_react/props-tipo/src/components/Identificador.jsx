const Identificador = ({valorID}) => {
    const tipo = typeof valorID;    
    return(
        <>         
            <p style={ {border: '1px solid  #ccc', padding:'10px', margin: '10px'} }>
                Tipo de dato: {tipo} | Tipo de valor: {valorID}
            </p>

            <button>
                {tipo == 'string' ? 'Cadena correcta' : 'Número detectado'}
            </button>
        </>
    )
}

export default Identificador;