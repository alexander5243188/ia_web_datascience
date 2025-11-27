const TarjetaUsuario = ({usuario}) => {
    const {nombre, edad, email} = usuario
    const dias = ["1","2"];
    return(
        <section >
            <ul>
                <li>{nombre}</li>
                <li>{edad}</li>
                <li>{email}</li>
            </ul>            
        </section>
    )
}

export default TarjetaUsuario;

