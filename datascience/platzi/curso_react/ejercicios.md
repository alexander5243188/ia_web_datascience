
## 1\. 📝 Ejercicio de Props Básicos: Mostrar un Mensaje

**Objetivo:** Crear un componente hijo que reciba y muestre un simple string a través de un prop.

1.  **Crea un componente funcional** llamado `Bienvenida`.
2.  Este componente debe aceptar un prop llamado `nombre`.
3.  `Bienvenida` debe renderizar un encabezado (`<h1>`) que diga: "Hola, \[nombre del prop]\! Bienvenido a React."
4.  En el componente padre (`App`), renderiza `Bienvenida` y pásale un nombre.

**Estructura esperada:**

```jsx
// Bienvenida.jsx
import React from 'react';

function Bienvenida(/** Acepta 'props' aquí */) {
  return (
    // Usa el prop 'nombre' aquí
    <h1>Hola, [nombre]! Bienvenido a React.</h1>
  );
}

export default Bienvenida;

// App.jsx
import Bienvenida from './Bienvenida';

function App() {
  return (
    <div className="App">
      {/* Pasa el prop 'nombre' aquí */}
      <Bienvenida nombre="TuNombre" />
    </div>
  );
}
```

-----

## 2\. 🔢 Ejercicio de Props de Tipo Numérico y Booleano

**Objetivo:** Pasar diferentes tipos de datos (número y booleano) y usarlos para realizar un cálculo y aplicar una lógica condicional.

1.  **Crea un componente funcional** llamado `ResultadoOperacion`.
2.  Este componente debe aceptar dos props: `numero` (un número) y `mostrarDoble` (un booleano).
3.  Si `mostrarDoble` es **true**, el componente debe mostrar el doble de `numero`.
4.  Si `mostrarDoble` es **false**, el componente debe mostrar el valor original de `numero`.
5.  En `App`, renderiza `ResultadoOperacion` **dos veces**: una con `mostrarDoble={true}` y otra con `mostrarDoble={false}`.

-----

## 3\. 🎨 Ejercicio de Props como Objetos

**Objetivo:** Pasar un objeto como un solo prop y desestructurar sus propiedades para mostrarlas individualmente.

1.  **Crea un componente funcional** llamado `TarjetaUsuario`.
2.  Este componente debe aceptar un solo prop llamado `datosUsuario`.
3.  El prop `datosUsuario` será un **objeto** con las claves `nombre`, `edad`, e `email`.
4.  `TarjetaUsuario` debe renderizar la información en una lista desordenada (`<ul>`).
5.  En `App`, define el objeto de usuario y pásalo a `TarjetaUsuario`.

**Estructura de datos a usar:**

```javascript
const usuario = {
  nombre: 'Alicia Pérez',
  edad: 28,
  email: 'alicia.perez@ejemplo.com',
};
```

-----

## 4\. 🔀 Ejercicio de Props como Arreglos (Listas)

**Objetivo:** Pasar un arreglo de datos y usar el método `map()` para renderizar una lista dinámica de elementos.

1.  **Crea un componente funcional** llamado `ListaItems`.
2.  Este componente debe aceptar un prop llamado `items` (un arreglo de strings).
3.  `ListaItems` debe usar el método **`.map()`** sobre el arreglo `items` para renderizar una lista ordenada (`<ol>`) de elementos. **Recuerda usar la prop `key`**.
4.  En `App`, define un arreglo de tus cosas favoritas (libros, películas, comidas) y pásalo a `ListaItems`.

-----

## 5\. 🧩 Ejercicio de `children` Prop

**Objetivo:** Usar el prop especial `children` para envolver contenido entre las etiquetas de un componente, permitiendo que el componente hijo renderice ese contenido.

1.  **Crea un componente funcional** llamado `ContenedorConBorde`.
2.  Este componente debe aceptar un prop `titulo` (string) y, lo más importante, el prop **`children`**.
3.  El componente debe renderizar un `div` que contenga:
      * Un encabezado (`<h2>`) que muestre el `titulo`.
      * El contenido de **`children`** envuelto en otro `div` para simular un cuerpo.
4.  En `App`, utiliza `ContenedorConBorde` y coloca **contenido JSX variado** (un párrafo, un botón, etc.) *entre* sus etiquetas de apertura y cierre.

**Ejemplo de uso esperado en `App`:**

```jsx
<ContenedorConBorde titulo="Contenido Importante">
  <p>Este es el contenido pasado como **children**.</p>
  <button>Haz Clic</button>
</ContenedorConBorde>
```

¡Absolutamente\! Como tu experto desarrollador en React, estoy encantado de ayudarte a dominar los **props**. Los props (propiedades) son fundamentales en React, ya que te permiten pasar datos de un componente padre a un componente hijo.

Aquí tienes 5 ejercicios diseñados para reforzar tu comprensión de los props en diferentes escenarios. ¡Vamos a ello\! 🚀

-----

## 1\. 📝 Ejercicio de Props Básicos: Mostrar un Mensaje

**Objetivo:** Crear un componente hijo que reciba y muestre un simple string a través de un prop.

1.  **Crea un componente funcional** llamado `Bienvenida`.
2.  Este componente debe aceptar un prop llamado `nombre`.
3.  `Bienvenida` debe renderizar un encabezado (`<h1>`) que diga: "Hola, \[nombre del prop]\! Bienvenido a React."
4.  En el componente padre (`App`), renderiza `Bienvenida` y pásale un nombre.

**Estructura esperada:**

```jsx
// Bienvenida.jsx
import React from 'react';

function Bienvenida(/** Acepta 'props' aquí */) {
  return (
    // Usa el prop 'nombre' aquí
    <h1>Hola, [nombre]! Bienvenido a React.</h1>
  );
}

export default Bienvenida;

// App.jsx
import Bienvenida from './Bienvenida';

function App() {
  return (
    <div className="App">
      {/* Pasa el prop 'nombre' aquí */}
      <Bienvenida nombre="TuNombre" />
    </div>
  );
}
```

-----

## 2\. 🔢 Ejercicio de Props de Tipo Numérico y Booleano

**Objetivo:** Pasar diferentes tipos de datos (número y booleano) y usarlos para realizar un cálculo y aplicar una lógica condicional.

1.  **Crea un componente funcional** llamado `ResultadoOperacion`.
2.  Este componente debe aceptar dos props: `numero` (un número) y `mostrarDoble` (un booleano).
3.  Si `mostrarDoble` es **true**, el componente debe mostrar el doble de `numero`.
4.  Si `mostrarDoble` es **false**, el componente debe mostrar el valor original de `numero`.
5.  En `App`, renderiza `ResultadoOperacion` **dos veces**: una con `mostrarDoble={true}` y otra con `mostrarDoble={false}`.

-----

## 3\. 🎨 Ejercicio de Props como Objetos

**Objetivo:** Pasar un objeto como un solo prop y desestructurar sus propiedades para mostrarlas individualmente.

1.  **Crea un componente funcional** llamado `TarjetaUsuario`.
2.  Este componente debe aceptar un solo prop llamado `datosUsuario`.
3.  El prop `datosUsuario` será un **objeto** con las claves `nombre`, `edad`, e `email`.
4.  `TarjetaUsuario` debe renderizar la información en una lista desordenada (`<ul>`).
5.  En `App`, define el objeto de usuario y pásalo a `TarjetaUsuario`.

**Estructura de datos a usar:**

```javascript
const usuario = {
  nombre: 'Alicia Pérez',
  edad: 28,
  email: 'alicia.perez@ejemplo.com',
};
```

-----

## 4\. 🔀 Ejercicio de Props como Arreglos (Listas)

**Objetivo:** Pasar un arreglo de datos y usar el método `map()` para renderizar una lista dinámica de elementos.

1.  **Crea un componente funcional** llamado `ListaItems`.
2.  Este componente debe aceptar un prop llamado `items` (un arreglo de strings).
3.  `ListaItems` debe usar el método **`.map()`** sobre el arreglo `items` para renderizar una lista ordenada (`<ol>`) de elementos. **Recuerda usar la prop `key`**.
4.  En `App`, define un arreglo de tus cosas favoritas (libros, películas, comidas) y pásalo a `ListaItems`.

-----

## 5\. 🧩 Ejercicio de `children` Prop

**Objetivo:** Usar el prop especial `children` para envolver contenido entre las etiquetas de un componente, permitiendo que el componente hijo renderice ese contenido.

1.  **Crea un componente funcional** llamado `ContenedorConBorde`.
2.  Este componente debe aceptar un prop `titulo` (string) y, lo más importante, el prop **`children`**.
3.  El componente debe renderizar un `div` que contenga:
      * Un encabezado (`<h2>`) que muestre el `titulo`.
      * El contenido de **`children`** envuelto en otro `div` para simular un cuerpo.
4.  En `App`, utiliza `ContenedorConBorde` y coloca **contenido JSX variado** (un párrafo, un botón, etc.) *entre* sus etiquetas de apertura y cierre.

**Ejemplo de uso esperado en `App`:**

```jsx
<ContenedorConBorde titulo="Contenido Importante">
  <p>Este es el contenido pasado como **children**.</p>
  <button>Haz Clic</button>
</ContenedorConBorde>
```
¡Me alegra escuchar que sigues aprendiendo y con esa energía\! 🚀

Entendiendo que el enfoque es en **props**, y manteniendo la estructura de los ejercicios anteriores (tipos de datos, estructuras, y el flujo padre-hijo), aquí tienes 6 nuevos desafíos para consolidar aún más tu dominio de las propiedades en React.

-----

## 6\. 🚦 Ejercicio de Props de Estado (Styling Condicional)

**Objetivo:** Usar un prop booleano para cambiar el estilo (apariencia) de un elemento.

1.  **Crea un componente funcional** llamado `BotonEstado`.
2.  Este componente debe aceptar un prop booleano llamado `estaActivo`.
3.  Si `estaActivo` es **`true`**, el botón debe tener un color de fondo verde.
4.  Si `estaActivo` es **`false`**, el botón debe tener un color de fondo gris.
5.  Renderiza el botón en `App` dos veces, una en cada estado. Usa el atributo `style={{...}}` de React para aplicar los estilos condicionales.

-----

## 7\. 🏷️ Ejercicio de Props de Tipo `any` (Prop con Tipo Mixto)

**Objetivo:** Crear un componente flexible que reciba un prop que puede ser un **string** o un **número**, y manejar su renderizado.

1.  **Crea un componente funcional** llamado `Identificador`.
2.  Este componente acepta un prop llamado `valorID`.
3.  El componente debe renderizar un párrafo (`<p>`) que muestre el tipo de dato y el valor del prop.
      * **Pista:** Puedes usar `typeof` en JavaScript para verificar el tipo de `valorID`.
4.  En `App`, renderiza `Identificador` dos veces: una pasándole un **número** (`108`) y otra pasándole un **string** (`"ABC-456"`).

-----

## 8\. 🗺️ Ejercicio de Props de Objeto Anidado

**Objetivo:** Pasar un objeto complejo con propiedades anidadas y acceder a ellas en el componente hijo.

1.  **Crea un componente funcional** llamado `DetalleProducto`.
2.  Este componente acepta un prop llamado `producto`.
3.  El prop `producto` es un objeto que contiene, entre otras cosas, un **objeto anidado** llamado `especificaciones` con las claves `peso` y `dimensiones`.
4.  `DetalleProducto` debe mostrar el nombre del producto, el precio y el valor de `dimensiones` del objeto anidado.
5.  Define el siguiente objeto en `App` y pásalo a `DetalleProducto`.

<!-- end list -->

```javascript
const laptop = {
  nombre: 'Laptop Pro X',
  precio: 1200,
  especificaciones: {
    peso: '1.5 kg',
    dimensiones: '35cm x 22cm', // <-- Necesitas acceder a este valor
  }
};
```

-----

## 9\. 🖼️ Ejercicio de Props de Arreglo de Objetos (Tabla)

**Objetivo:** Pasar un arreglo de objetos y usar `.map()` para generar una tabla estructurada.

1.  **Crea un componente funcional** llamado `TablaEmpleados`.
2.  Este componente debe aceptar un prop llamado `empleados` (un arreglo de objetos).
3.  Utiliza el método **`.map()`** para renderizar una tabla (`<table>`) con encabezados (`<thead>`) y filas (`<tbody>`).
      * Cada objeto en el arreglo debe mapearse a una fila (`<tr>`).
4.  Define el siguiente arreglo en `App` y pásalo a `TablaEmpleados`.

<!-- end list -->

```javascript
const listaEmpleados = [
  { id: 1, nombre: 'Ana', puesto: 'Desarrolladora' },
  { id: 2, nombre: 'Carlos', puesto: 'Diseñador' },
  { id: 3, nombre: 'Sofía', puesto: 'Project Manager' },
];
```

-----

## 10\. 🔄 Ejercicio de Props como Función (Placeholder)

**Objetivo:** Pasar una **función** como un prop para simular una acción que el componente hijo podría realizar (aunque en este caso, solo la mostrará).

1.  **Crea un componente funcional** llamado `BotonAccion`.
2.  Este componente debe aceptar un prop llamado `onClickHandler`.
3.  Renderiza un párrafo (`<p>`) que muestre un texto descriptivo del prop, indicando que se ha pasado una función.
      * **Nota:** No tienes que ejecutar la función, solo demostrar que la recibes. Puedes usar `String(onClickHandler)` para ver su definición.
4.  En `App`, define una función simple (ej: `const miFuncion = () => { console.log('Hice clic'); };`) y pásala como prop a `BotonAccion`.

-----

## 11\. 📦 Ejercicio de Doble `children` (Componente de Layout)

**Objetivo:** Combinar el prop especial **`children`** con un prop normal (`contenidoExtra`) para estructurar un *layout* más complejo.

1.  **Crea un componente funcional** llamado `LayoutDoble`.
2.  Este componente debe aceptar dos props: `children` y `contenidoExtra`.
3.  `LayoutDoble` debe renderizar un contenedor (`<div>`) dividido en dos partes:
      * El lado izquierdo debe renderizar el contenido de **`children`**.
      * El lado derecho debe renderizar el contenido de **`contenidoExtra`** (que también será un elemento JSX).
4.  En `App`, utiliza `LayoutDoble`. Pasa un párrafo y una lista como `children`, y un componente `<img>` o una tarjeta simple como el prop `contenidoExtra`.

-----


