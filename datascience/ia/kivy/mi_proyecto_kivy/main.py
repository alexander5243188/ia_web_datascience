
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window # Necesario para cambiar el fondo
from kivy.utils import get_color_from_hex # Ayuda a definir colores con código hexadecimal

kivy.require('1.11.1')

class MyFirstKivyApp(App):
    
    def build(self):
        # 1. Establece el color de fondo de la VENTANA a blanco (RGB 1, 1, 1, A 1)
        Window.clearcolor = get_color_from_hex('#FFFFFF') # Alternativa: (1, 1, 1, 1)

        # 2. Crea la etiqueta con el texto "Hello World!" y el color de texto rojo.
        # El color se define como una tupla RGBA (Rojo, Verde, Azul, Alfa/Opacidad).
        # Rojo puro es (1, 0, 0, 1)
        return Label(
            text="Hello World!",
            color=(1, 0, 0, 1) # Rojo puro
        )

MyFirstKivyApp().run()