import tkinter as tk
from tkinter import ttk

# Inicializamos el contador a nivel global
valor = [0]

def saludo():
    print("Hola")
    etiqueta_salida.config(text=f"Hola")

def contador():    
    nuevo_valor = valor[0] + 1
    valor[0] = nuevo_valor

    print(valor[0])
    etiqueta_salida.config(text=f"{valor[0]}")

def generar_saludo():
    mensaje = entrada_saludo.get()
    etiqueta_salida.config(text=f'Hola es la palabra que escribiste, "{mensaje}" ')
    print(mensaje)

def suma():
    valor_uno = float(primer_valor.get())
    valor_dos = float(segundo_valor.get())
    suma = valor_uno + valor_dos
    etiqueta_salida.config(text=f"{suma}")

def check_activo():
    estado = activo.get()
    print("Activado: ", estado)
    etiqueta_salida.config(text=f"{estado}")

def semaforo():
    estado = opcion_semaforo.get()
    print(estado)
    etiqueta_salida.config(text=f"{estado}")

def conversor():
    valor_celsius = float(entrada_censius.get())
    fahrenheit = (valor_celsius * 9/5) + 32
    print(fahrenheit)
    etiqueta_salida.config(text=f"{fahrenheit} °f")

def dias_semana(event):
    dia = combobox.get()
    etiqueta_salida.config(text=f"{dia}")
    print(f"{dia}")
    


#-- Creación de la ventana
ventana = tk.Tk()
ventana.title("Varios ejercicis")
ventana.geometry("400x600")

#-- Creacion de variables
activo = tk.IntVar()
opcion_semaforo = tk.StringVar()

#-- Boton de saludo
boton_saludo = tk.Button(ventana, text="Saludo", command=saludo)
boton_saludo.pack(pady=5)

#-- Boton de contador
boton_contador = tk.Button(ventana, text="Contador", command=contador)
boton_contador.pack(pady=5)

# -- Boton de saludo
entrada_saludo = tk.Entry(ventana)
entrada_saludo.pack(pady=5)
boton_entrada_saludo = tk.Button(ventana, text="Genera saludo", command=generar_saludo)
boton_entrada_saludo.pack(pady=5)

# -- Boton de suma
primer_valor = tk.Entry(ventana)
primer_valor.pack(pady=5)

segundo_valor= tk.Entry(ventana)
segundo_valor.pack(pady=5)

boton_suma_primer_segundo_valor = tk.Button(ventana, text="Suma", command=suma)
boton_suma_primer_segundo_valor.pack(pady=5)

# -- Checkbutton activado
verificacion = tk.Checkbutton(ventana, text="Activar", variable=activo, command=check_activo)
verificacion.pack(pady=5)


#-- Radiobuttons emaforo
rojo = tk.Radiobutton(ventana, text="Rojo", variable=opcion_semaforo, value="Rojo", command=semaforo)
rojo.pack(pady=5)

amarillo = tk.Radiobutton(ventana, text="Amarillo", variable=opcion_semaforo, value="Amarillo", command=semaforo)
amarillo.pack(pady=5)

verde = tk.Radiobutton(ventana, text="Verde", variable=opcion_semaforo, value="Verde", command=semaforo)
verde.pack(pady=5)

#-- Conversor de unidades
etiqueta_conversor = tk.Label(ventana, text="Temperatura en celsius")
etiqueta_conversor.pack(pady=5)

entrada_censius = tk.Entry(ventana)
entrada_censius.pack(pady=5)

boton_conversor = tk.Button(ventana, text="Convertir", command=conversor)
boton_conversor.pack(pady=5)

#-- Combobox menu
combobox = ttk.Combobox(ventana, values=["Lunes", "Martes", "Miercoles", "Jueves"])
combobox.pack(pady=5)
combobox.set("Seleccione un día")
combobox.bind("<<ComboboxSelected>>", dias_semana)


etiqueta_salida = tk.Label(ventana, text="")
etiqueta_salida.pack(pady=5)

ventana.mainloop()