import React, {useState} from "react";

const Contador = () => {
    const [count, setconunt] = useState(0)
    return(
        <>
            <p>You clicked {count} times</p>
            <button onClick={()=>{setconunt(count+1)}}>Click me</button>
        </>
    )
}
export default Contador;