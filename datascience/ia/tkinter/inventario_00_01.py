import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Datos de ejemplo simulados para el gráfico
def obtener_datos_simulados():
    """Genera datos simulados de ventas por categoría para el gráfico."""
    categorias = [f"Cat-{i+1}" for i in range(10)]
    ventas = [random.randint(50, 500) for _ in range(10)]
    return categorias, ventas

class InventarioApp:
    """Clase principal de la aplicación de Registro de Inventario."""

    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Inventario")
        # Establecer un tamaño inicial y centrar la ventana
        ancho_ventana = 1000
        alto_ventana = 700
        pos_x = (master.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        pos_y = (master.winfo_screenheight() // 2) - (alto_ventana // 2)
        master.geometry(f'{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}')
        master.configure(bg="#f4f7f9")

        # 1. Crear la barra de menús
        self.create_menus()

        # 2. Crear la pantalla principal con el gráfico
        self.create_main_screen()

    def create_menus(self):
        """Crea y configura la barra de menús principal."""
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # --- MENÚ REGISTRO ---
        registro_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="REGISTRO", menu=registro_menu)
        registro_menu.add_command(label="Registro de Categoría", command=self.open_category_registration)
        registro_menu.add_command(label="Registro de Producto", command=self.open_product_registration)

        # --- MENÚ VENTA ---
        venta_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="VENTA", menu=venta_menu)
        venta_menu.add_command(label="Registro de Venta", command=self.open_sale_registration)

        # --- MENÚ BÚSQUEDA ---
        busqueda_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="BÚSQUEDA", menu=busqueda_menu)
        busqueda_menu.add_command(label="Buscar Producto", command=self.search_product)

        # --- MENÚ REPORTE ---
        reporte_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="REPORTE", menu=reporte_menu)
        reporte_menu.add_command(label="Generar Reporte en PDF", command=self.generate_pdf_report)
        
        # --- MENÚ AYUDA (Opcional) ---
        ayuda_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="AYUDA", menu=ayuda_menu)
        ayuda_menu.add_command(label="Acerca de...", command=self.show_about)


    def create_main_screen(self):
        """Crea la vista principal que contiene el título y el gráfico."""
        
        # Frame principal para el contenido (ocupa toda la ventana)
        main_frame = tk.Frame(self.master, bg="#f4f7f9", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Título
        title_label = tk.Label(main_frame, 
                               text="Dashboard de Inventario - Top 10 Productos Más Vendidos por Categoría", 
                               font=("Arial", 16, "bold"), 
                               bg="#f4f7f9",
                               fg="#2c3e50")
        title_label.pack(pady=10)

        # Contenedor para el gráfico
        chart_container = tk.Frame(main_frame, bg="white", bd=2, relief=tk.RIDGE)
        chart_container.pack(fill="both", expand=True, padx=50, pady=10)
        
        # Generar y mostrar el gráfico
        self.plot_pie_chart(chart_container)

    def plot_pie_chart(self, container):
        """Genera el gráfico de torta con datos simulados y lo embebe en el contenedor."""
        
        # Configurar la figura de Matplotlib
        fig = Figure(figsize=(6, 5), dpi=100, facecolor="#ffffff")
        ax = fig.add_subplot(111)

        categorias, ventas = obtener_datos_simulados()
        
        # Personalización del gráfico de torta
        wedges, texts, autotexts = ax.pie(
            ventas, 
            labels=categorias, 
            autopct='%1.1f%%', 
            startangle=90, 
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.5},
            textprops={'fontsize': 8}
        )
        
        # Título del gráfico
        ax.set_title("Distribución de Ventas Simuladas por Categoría", fontsize=10)
        
        # Ajustar el padding para evitar recortes
        fig.tight_layout(pad=1.5)

        # Embeber el gráfico en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        
        # Etiqueta de nota (ejemplo de cómo mostrar información adicional)
        note_label = tk.Label(container, 
                              text="*Gráfico basado en datos simulados. Se actualizará con la conexión a la BD.",
                              font=("Arial", 9, "italic"),
                              bg="white",
                              fg="#7f8c8d")
        note_label.pack(pady=(0, 5))


    # --- Métodos de Acción de Menú (Placeholders) ---

    def open_category_registration(self):
        """Acción para abrir la ventana de Registro de Categoría."""
        messagebox.showinfo("Registro", "Abriendo la interfaz para el REGISTRO DE CATEGORÍA.")
        # Aquí se integraría el código del módulo de registro de categoría.
        # Por ejemplo: CategoryRegistrationWindow(self.master)

    def open_product_registration(self):
        """Acción para abrir la ventana de Registro de Producto."""
        messagebox.showinfo("Registro", "Abriendo la interfaz para el REGISTRO DE PRODUCTO.")
        # Aquí se integraría el código del módulo de registro de producto.

    def open_sale_registration(self):
        """Acción para abrir la ventana de Registro de Venta."""
        messagebox.showinfo("Venta", "Abriendo la interfaz para el REGISTRO DE VENTA.")
        # Aquí se integraría el código del módulo de registro de venta.

    def search_product(self):
        """Acción para abrir la ventana de Búsqueda de Producto."""
        messagebox.showinfo("Búsqueda", "Abriendo la interfaz para BUSCAR PRODUCTO.")
        # Aquí se integraría el código del módulo de búsqueda.

    def generate_pdf_report(self):
        """Acción para generar el reporte en PDF."""
        messagebox.showinfo("Reporte", "Generando el REPORTE EN PDF. (Se requiere un módulo como ReportGenerator).")
        # Aquí se integraría el código del módulo de reportes.

    def show_about(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo("Acerca de", "Sistema de Gestión de Inventario\nDesarrollado con Python y Tkinter.")

# --- Inicialización de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()