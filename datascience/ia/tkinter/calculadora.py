import tkinter as tk


def suma():    
    valor_uno = entrada_1.get()
    valor_dos = entrada_2.get()
    resultado_suma = valor_uno + valor_dos
    etiqueta_resultado.config(text=f"{valor_uno} + {valor_dos} = {resultado_suma}")
    


def resta():    
    valor_uno = entrada_1.get()
    valor_dos = entrada_2.get()
    resultado_resta = valor_uno - valor_dos
    etiqueta_resultado.config(text=f"{valor_uno} - {valor_dos} = {resultado_resta}")

def multiplicacion():
    print("Multiplicacion")
    valor_uno = entrada_1.get()
    valor_dos = entrada_2.get()
    resultado_mutiplicacion = valor_uno * valor_dos
    etiqueta_resultado.config(text=f"{valor_uno} * {valor_dos} = {resultado_mutiplicacion}")


def division():
    print("Division")
    valor_uno = entrada_1.get()
    valor_dos = entrada_2.get()
    resultado_division = valor_uno / valor_dos
    etiqueta_resultado.config(text=f"{valor_uno} / {valor_dos} = {resultado_division}")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x300")

entrada_1 = tk.DoubleVar()
entrada_2 = tk.DoubleVar()

tk.Entry(ventana, textvariable=entrada_1).pack(pady=10)
tk.Entry(ventana, textvariable=entrada_2).pack(pady=10)

boton_suma = tk.Button(ventana, text="Sumar", command=suma)
boton_suma.pack(pady=10)

boton_resta = tk.Button(ventana, text="Resta", command=resta)
boton_resta.pack(pady=10)

boton_multiplicacion = tk.Button(ventana, text="Multiplicacion", command=multiplicacion)
boton_multiplicacion.pack(pady=10)

boton_division = tk.Button(ventana, text="Division", command=division)
boton_division.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", fg="red")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
