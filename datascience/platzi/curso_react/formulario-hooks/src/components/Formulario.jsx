// npm install react-hook-form

import React, {Fragment} from 'react'
import { useForm } from 'react-hook-form'

const Formulario = () => {
    
    // Desestructuración correcta
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        console.log(data)
    }

    return (
        <Fragment>
            <h2>Hooks Forms</h2>
            <form onSubmit={handleSubmit(onSubmit)}>
                
                {/* 1. CORRECCIÓN: Agregar la propiedad 'name' 
                    2. CORRECCIÓN: Llamar y esparcir register() para V7+ */}
                <input 
                    type="text"
                    placeholder="Escribe tu nombre"
                    // Esto es lo que falta y lo que se debe actualizar:
                    {...register("nombreUsuario", {
                        required: {value: true, message: 'Nombre es requerido'}, 
                        maxLength: {value: 5, message: 'No más de 5 carácteres!'},
                        minLength: {value: 2, message: 'Mínimo 2 carácteres'}
                    })}
                />
                
                {/* Mostrar los errores de este campo */}
                <span style={{ color: 'red' }}>
                    {errors.nombreUsuario?.message}
                </span>

                <button type="submit" className="btn btn-primary">
                    Enviar
                </button>
            </form>
        </Fragment>
    );
}
 
export default Formulario;