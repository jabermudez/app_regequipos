import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Dibuja un rectángulo con bordes redondeados en un canvas."""
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Inicializar la ventana principal
root = ttk.Window(themename='litera')

# Crear un canvas y un rectángulo redondeado que actuará como la card
canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Coordenadas y radio del rectángulo redondeado
x1 = 50
y1 = 50
x2 = 250
y2 = 150
radius = 20

# Crear el rectángulo redondeado
rounded_rectangle = create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, fill='lightblue')

# Crear el label y posicionarlo en el canvas encima del rectángulo redondeado
label = tk.Label(canvas, text="Esto es una card con bordes redondeados", bg='lightblue')
label_window = canvas.create_window(x1+10, y1+10, anchor='nw', window=label)

# Ejecutar el loop principal
root.mainloop()
