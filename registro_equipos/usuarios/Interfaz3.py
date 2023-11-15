import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap import *
from ttkbootstrap import Style  # Asegúrate de que ttkbootstrap está instalado y configurado

from model.usuario_dao import consultar_prestamos


#barra de neby
def barra_menu(root):
    barra_menu = tb.Menu(root)
    root.config(menu = barra_menu)

    menu_inicio = tb.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro')
    menu_inicio.add_command(label='Eliminar Registro')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='configuración')
    barra_menu.add_cascade(label='Ayudas')






class Frame3(tb.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root                        
        self.id_usuario = None
        self.id_equipo = None
        self.equipo_asignado = False
        
        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n        \n          Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle='light', anchor='center')
        self.label.configure(background='#1464f6', width=93)        
        self.label.grid(row=0, column=0, columnspan=6, padx=0, pady=0, ipady=30)
        
        
        self.img = tk.PhotoImage(file="./img/logo1.png")
        self.img = self.img.subsample(4,4)
        self.lbl_img = tb.Label(root,  image = self.img)
        self.lbl_img.configure(background='#1464f6')                
        self.lbl_img.grid(row=0, column=0, padx=20, pady=0, ipadx=10, sticky='w')

# Función para mostrar los préstamos en una tabla
    def mostrar_tabla_prestamos():
        root = tk.Tk()
        style = Style(theme='darkly')  # O el tema que prefieras de ttkbootstrap
        
        tree = ttk.Treeview(root, columns=('Codigo', 'Nombre', 'Apellidos', 'Fecha Prestamo',  'Fecha Entrega'), show='headings')
        
        tree.heading('Codigo', text='Código')
        tree.heading('Nombre', text='Nombre')
        tree.heading('Apellidos', text='Apellidos')
        tree.heading('Fecha Prestamo', text='Fecha Préstamo')    
        tree.heading('Fecha Entrega', text='Fecha Entrega')
        
        
        for prestamo in consultar_prestamos():
            tree.insert('', tk.END, values=prestamo)
        
        tree.pack(expand=True, fill='both')
        root.mainloop()

    # Llama a esta función donde necesites para mostrar los préstamos
    mostrar_tabla_prestamos()
