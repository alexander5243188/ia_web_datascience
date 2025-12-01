// BotonEstado.jsx (CORREGIDO)
// 1. Aceptamos el prop 'estaActivo'
// 2. Opcionalmente, aceptamos 'children' si queremos que el botón tenga contenido dinámico
const BotonEstado = ({ estaActivo, children }) => {
  
    // Usamos el prop 'estaActivo' para definir el color de fondo
    const estilosBoton = {
      // Si estaActivo es true, color verde. Si es false, color gris.
      backgroundColor: estaActivo ? '#4CAF50' : '#9E9E9E',
      color: 'white',
      padding: '10px 20px',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
      margin: '5px'
    };    
    return (
      // Aplicamos el objeto de estilo usando el atributo 'style'
      <button style={estilosBoton}>
          {/* Si se pasa contenido 'children', lo usamos. Si no, usamos un texto por defecto. */}
          {children || (estaActivo ? 'Botón ACTIVO' : 'Botón INACTIVO')}
      </button>
    );
}
export default BotonEstado;