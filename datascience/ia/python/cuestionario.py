def ejecutar_cuestionario():
    preguntas_data = [
        {
            "titulo": "🧠 1. Diferencia entre 'Investigación Profunda' y búsqueda web",
            "pregunta": "¿Qué distingue a la 'función agéntica' de la 'Investigación Profunda' de una simple búsqueda web realizada por ChatGPT?",
            "opciones": {
                "A": "Accede a bases de datos académicas exclusivas que no están disponibles en búsqueda web normal.",
                "B": "Combina búsqueda, un modelo de razonamiento iterativo para planificar y analizar, y la generación de un documento estructurado.",        
                "C": "Permite al usuario chatear con el modelo en tiempo real para ajustar la investigación mientras está en curso.",  
                "D": "Garantiza que toda la información del reporte es 100% precisa y no requiere validación del usuario."
            },
            "respuesta_correcta": "B"
        },
        {
            "titulo": "🗣️ 2. Interrupción en modo avanzado de voz",
            "pregunta": "Durante una conversación en el 'modo avanzado de voz', un usuario interrumpe a ChatGPT para pedirle que adopte un acento diferente. ¿Qué demuestra principalmente esta capacidad de interrupción mencionada en la clase?",            
            "opciones": {
                "A": "Que la inteligencia artificial tiene una capacidad de procesamiento limitada y debe ser interrumpida para poder asimilar nuevas instrucciones como un cambio de rol.",
                "B": "Que la inteligencia artificial, al igual que los humanos, puede responder en tiempo real.",
                "C": "Que la transcripción automática sólo es fluida y se puede registrar en tiempo real si los humanos hablan con ritmo constante.",
                "D": "Que la interrupción automática sólo es importante cuando se le quiere enviar un turno de respuesta en tiempo real a la IA para evitar errores futuros.",
                "E": "Que existe una función exclusiva para corregir errores de transcripción en tiempo real mientras la inteligencia artificial está respondiendo.",                
                },
            "respuesta_correcta": "B"
        },
        {
            "titulo": "📄 3. Propósito de la transcripción automática en voz",
            "pregunta": "¿Cuál es el propósito principal de la función de transcripción automática que se activa durante las conversaciones de voz en la aplicación móvil de ChatGPT?",
            "opciones": {
                "A": "Mejorar la capacidad de la inteligencia artificial para entender diferentes acentos.",
                "B": "Permitir la edición en tiempo real de los prompts que se le dan a la IA.",
                "C": "Guardar un registro escrito de toda la conversación para poder revisarla o utilizarla más tarde.",
                "D": "Traducir la conversación a otros idiomas de forma automática."
            },
            "respuesta_correcta": "C"
        },
        {
            "titulo": "🧩 4. Diferencia entre instrucciones personalizadas y memoria.",
            "pregunta": "¿Cuál es la diferencia fundamental entre las Instrucciones personalizadas y la función Memoria en ChatGPT, según lo explicado en la clase?",
            "opciones":{
                "A": "Las instrucciones personalizadas son directrices globales y estáticas para el comportamiento de la IA en todos los chats, mientras que la memoria guarda dinámicamente información específica sobre el usuario que surge durante las conversaciones.",
                "B": "La memoria actualiza permanentemente el modelo base de conocimiento de GPT, mientras que las instrucciones personalizadas solo cambian el tono de la respuesta.",
                "C": "La memoria se gestiona automáticamente y no se puede editar, mientras que las instrucciones personalizadas deben ser modificadas manualmente por el usuario.",
                "D": "Las instrucciones personalizadas son para guardar datos personales como el nombre, y la memoria es para guardar comandos complejos o hacks."
            },
            "respuesta_correcta": "A"
        },
        {
            "titulo": "🔐 5. Propósito de la autenticación multifactor (MFA)",
            "pregunta": "¿Para qué sirve principalmente la autenticación multifactor (MFA) en el menú de 'Seguridad' de ChatGPT?",
            "opciones":{
                "A": "Para proteger tus dispositivos si se ha iniciado sesión y cerrar sesiones de forma remota.",
                "B": "Para encriptar las conversaciones y que solo el usuario pueda leerlas.",
                "C": "Para autorizar a ChatGPT a aprender de las conversaciones y mejorar el modelo para todos.",
                "D": "Para añadir una capa de seguridad adicional al iniciar sesión, validando la identidad del usuario a través de un segundo método."        
            },
            "respuesta_correcta": "D"
        },
        {
            "titulo": "🧩 6. Verificación al instalar extensión de ChatGPT",
            "pregunta": "Al instalar una extensión para usar ChatGPT como buscador desde la tienda de Google Chrome, ¿cuál es el paso crucial de verificación mencionado en la clase para evitar la instalación de clones potencialmente maliciosos?",
            "opciones":{
                "A": "Elegir la extensión que aparece en primer lugar en los resultados de búsqueda.",
                "B": "Verificar que el desarrollador de la extensión sea 'chatgpt.com'.",
                "C": "Asegurarse de que la extensión tenga el mayor cantidad de descargas y las mejores reseñas.",
                "D": "Comprobar que la extensión sea compatible tanto con la cuenta gratuita como con la de pago."
            },
            "respuesta_correcta": "B"
        },
        {
            "titulo": "📝 7. Adaptar informe para dos audiencias con Canvas",
            "pregunta": "Un usuario está adaptando un informe complejo para dos audiencias distintas: un grupo de ejecutivos y un grupo de estudiantes de preparatoria. ¿Qué combinación de funciones de Canvas le permitiría realizar esta tarea de la manera más efectiva y directa?",
            "opciones":{
                "A": "Cambiar el Nivel de lectura a 'universidad' para los ejecutivos y a 'escuela preparatoria' para los estudiantes.",
                "B": "Usar Ajustar la longitud para la versión de los ejecutivos y Agregar emojis para la de los estudiantes.",
                "C": "Utilizar Mostrar cambios para ver diferencias entre versiones y Resumir para simplificar el contenido.",
                "D": "Expandir el contenido con Preguntar a ChatGPT si los ejecutivos solicitan información adicional, y resumirlo para los estudiantes."
            },
            "respuesta_correcta": "D"
        },
        {
            "titulo": "🎨 8. Diferencia entre generación con referencia y desde cero",
            "pregunta": "Un diseñador genera una imagen de su gato al estilo 'Studio Ghibli' usando una foto real como referencia. Según lo explicado en la clase, ¿qué característica principal diferencia este proceso de una generación de imagen desde cero?",
            "opciones":{
                "A": "La generación con referencia ignora el prompt de texto y se basa únicamente en los píxeles de la imagen de entrada.",
                "B": "El modelo utiliza la composición y los elementos clave de la imagen de entrada como base, pero además necesita mirar el nuevo estilo.",
                "C": "La imagen generada con referencia es más fácil de editar posteriormente con la herramienta 'Seleccionar'.",
                "D": "El proceso es más rápido porque el modelo solo cambia los colores de la imagen original sin reinterpretar la escena."
            },
            "respuesta_correcta": "B"
        },
        {
            "titulo": "🧠 9. Diferencia entre GPTs personalizados y proyectos básicos",
            "pregunta": "Según lo explicado en la clase, ¿cuál es una capacidad de control fundamental que diferencia a los GPTs personalizados de los proyectos básicos en ChatGPT?",
            "opciones":{
                "A": "La capacidad de activar o desactivar herramientas específicas como la búsqueda web o el intérprete de código.",
                "B": "La habilidad de mantener una conversación continua y recordar el contexto anterior.",
                "C": "El uso de instrucciones elaboradas que definen el rol, tarea y contexto.",
                "D": "La posibilidad de cargarle archivos para crear una base de conocimiento."
            },   
            "respuesta_correcta": "A"
        },
        {
            "titulo": "🧑‍🏫 10. Crear asistente con cuenta gratuita",
            "pregunta": "Si un usuario con una cuenta gratuita de ChatGPT quisiera crear un asistente similar al 'Estratega de Cursos Corporativos', ¿qué herramienta o función debería utilizar según lo mencionado en la clase?",
            "opciones":{
                "A": "La función 'Canvas' para simular la estructura del asistente.",
                "B": "La función de 'proyectos', que permite crear instrucciones y archivos.",
                "C": "La función 'Deep Research' para generar un prompt lo suficientemente detallado.",
                "D": "Debe crear el asistente 'Estratega de Cursos Corporativos' de la misma forma, ya que se encuentra en ambas cuentas."
            },   
            "respuesta_correcta": "B"
        },
        {
            "titulo": "📚 11. Análisis de documentos extensos",
            "pregunta": "De acuerdo con la clase, ¿cuál es la razón principal para analizar documentos muy extensos en conversaciones separadas antes de combinar los resultados en un nuevo chat?",
            "opciones":{
                "A": "Porque ChatGPT tiene un límite técnico de un solo archivo por conversación.",
                "B": "Para prevenir que los archivos se fusionen de forma incorrecta y se corrompan los datos.",
                "C": "Para evitar que la IA olvide información de los primeros archivos debido a la limitación de la ventana de contexto.",
                "D": "Porque el análisis de documentos separados permite a la IA concretar a fuentes de datos externas para validación."
            },
            "respuesta_correcta": "C"
        },
        {
            "titulo": "🌐 12. Transversalidad de los usos de ChatGPT",
            "pregunta": "¿Qué implica el concepto de 'transversalidad' de los usos de ChatGPT, según lo expuesto en la presentación?",
            "opciones":{
                "A": "Que sus aplicaciones son útiles y relevantes independientemente del rol profesional o la industria de la persona.",
                "B": "Que la herramienta puede transferir conocimientos de un área a otra, por ejemplo, entre conceptos de biología a finanzas.",
                "C": "Que ChatGPT puede realizar múltiples tareas simultáneamente, como analizar datos y escribir un correo al mismo tiempo.",
                "D": "Que el uso de ChatGPT se extiende a través de todas las clases sociales y niveles educativos, no solo en el profesional.",
                "E": "Clase: Cómo usar ChatGPT como copiloto para acelerar tu productividad."
            },   
            "respuesta_correcta": "A"
        },
        {
            "titulo": "📈 13. Nuevas herramientas de IA y estudiantes",
            "pregunta": "Según el instructor, ¿por qué los estudiantes no deberían preocuparse por la constante aparición de nuevas herramientas de IA?",
            "opciones":{
                "A": "Porque la mayoría de las nuevas herramientas de IA no son relevantes para el campo profesional.",
                "B": "Porque el curso les ha proporcionado las técnicas fundamentales que son aplicables a cualquier nueva tecnología de IA.",
                "C": "Porque las nuevas herramientas de IA son generalmente versiones mejoradas de las antiguas y funcionan de la misma manera.",
                "D": "Porque el instructor les proporcionará un listado actualizado de todas las herramientas más relevantes a través de LinkedIn."
            },   
            "respuesta_correcta": "B"

        },
        {
            "titulo": "📊 14. Capacidad clave en análisis conversacional",
            "pregunta": "Un analista le pide a ChatGPT el 'top diez de productos más vendidos' y la herramienta le ofrece una lista numerada de posibles análisis adicionales. Si el analista responde 'hagamos el dos', ¿qué capacidad clave de la herramienta está aprovechando?",
            "opciones":{
                "A": "La capacidad de análisis conversacional para entender referencias a interacciones previas.",
                "B": "La generación de reportes completos y automatizados con una sola instrucción.",
                "C": "El uso de código Python en el backend para el desarrollo de cálculos.",
                "D": "La validación de variables para asegurar la comprensión del modelo."
            },
            "respuesta_correcta": "A"
        },
        {
            "titulo": "🧠 15. Diferencia funcional entre instrucciones personalizadas y base de conocimiento",
            "pregunta": "¿Cuál es la diferencia funcional clave entre usar las Instrucciones personalizadas y cargar archivos en la Base de conocimiento dentro de un proyecto?",
            "opciones":{
                "A": "Las instrucciones solo se aplican a cuentas de pago, mientras que la base de conocimiento está disponible para todas.",
                "B": "Las instrucciones personalizadas son para organizar los chats, mientras que la base de conocimiento organiza los archivos.",
                "C": "Las instrucciones son permanentes para el proyecto, mientras que las respuestas de la base de conocimiento deben cargarse en cada sesión.",
                "D": "Las instrucciones definen el rol y comportamiento del asistente, mientras que la base de conocimiento le proporciona información y contexto específico."
            },
            "respuesta_correcta": "D"
        }       
    ]

    # Inicializa contadores
    respuestas_correctas = 0
    total_preguntas = len(preguntas_data)

    print("--- 🧠 ¡Bienvenido al Cuestionario! 🧠 ---")
    print(f"Responde a las {total_preguntas} preguntas. Ingresa A, B, C o D.")
    print("-" * 40)

    # 2. Itera sobre cada pregunta
    for i, q in enumerate(preguntas_data):
        print(f"\n✅ Pregunta {i + 1} de {total_preguntas}:")
        print(q["titulo"])
        print(q["pregunta"])
        
        
        # Muestra las opciones
        for opcion, texto in q["opciones"].items():
            print(f"  [{opcion}] {texto}")

        # Solicita la respuesta del usuario y valida
        while True:
            respuesta_usuario = input("Tu respuesta (A/B/C/D): ").upper()
            if respuesta_usuario in ["A", "B", "C", "D"]:
                break
            print("❌ Opción no válida. Por favor, ingresa solo A, B, C o D.")

        # 3. Comprueba la respuesta
        if respuesta_usuario == q["respuesta_correcta"]:
            print("👍 ¡Correcto!")
            respuestas_correctas += 1
        else:
            print(f"👎 Incorrecto. La respuesta correcta era: [{q['respuesta_correcta']}] {q['opciones'][q['respuesta_correcta']]}")
            
        print("-" * 40)


    # 4. Muestra el resultado final
    respuestas_incorrectas = total_preguntas - respuestas_correctas
    
    print("\n\n=============== RESULTADOS FINALES ===============")
    print(f"✨ Total de preguntas: **{total_preguntas}**")
    print(f"🟢 Respuestas correctas: **{respuestas_correctas}**")
    print(f"🔴 Respuestas incorrectas: **{respuestas_incorrectas}**")
    
    # Mensaje de ánimo o felicitación
    if respuestas_correctas == total_preguntas:
        print("🎉 ¡Felicidades! ¡Respondiste todas correctamente! Eres un genio.")
    elif respuestas_correctas >= total_preguntas / 2:
        print("👏 ¡Buen trabajo! Más de la mitad fueron correctas.")
    else:
        print("🧐 Sigue practicando. ¡La práctica hace al maestro!")
    
    print("==================================================")


# Ejecuta la función principal
if __name__ == "__main__":
    ejecutar_cuestionario()
