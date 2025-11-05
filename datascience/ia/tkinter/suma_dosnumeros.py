import tkinter as tk

def suma():
    valor_uno = float(entrada_uno.get())
    valor_dos = float(entrada_dos.get())
    resultado = valor_uno + valor_dos
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

ventana = tk.Tk()
ventana.title("+")
ventana.geometry("200x200")

etiqueta = tk.Label(ventana, text="Primer valor: ")
etiqueta.pack(pady=5)

entrada_uno = tk.Entry(ventana)
entrada_uno.pack(pady=5)

etiqueta = tk.Label(ventana, text="Segundo valor: ")
etiqueta.pack(pady=5)

entrada_dos = tk.Entry(ventana)
entrada_dos.pack(pady=5)

boton = tk.Button(ventana, text="Sumar", command=suma)
boton.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()
