import tkinter as tk


def saludar():
    texto = entrada.get()
    etiqueta_resultado.config(text=f"Hola, {texto}")


ventana = tk.Tk()
ventana.title("Varios Widgets en Tkinter")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escibe tu nombre: ")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()
