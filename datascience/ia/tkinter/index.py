import tkinter as tk

def abrir():
    pass

def salir():
    pass

#-- Creacion de la ventana
ventana = tk.Tk()
ventana.title("Meditaciones")
ventana.geometry("400x600")

#--
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
#-- 
ventana.mainloop()