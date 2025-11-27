const ListaItems = ({items}) => {
    return(
        <section>
            <ol>
                {items.map((item, index) => (<li key={index}>{item}</li>))}
            </ol>
        </section>
    )
}

export default ListaItems;