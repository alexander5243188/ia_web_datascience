import tkinter as tk

ventana = tk.Tk();

ventana.title("Mi primera ventana")
ventana.geometry("400x300")
ventana.configure(bg="lightblue")

etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!", font=("Arial", 16))
etiqueta.pack(pady=50)

ventana.mainloop()