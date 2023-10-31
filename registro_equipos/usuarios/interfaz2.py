import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import crear_tabla, borrar_tabla
from model.usuario_dao import Usuario, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu = tb.Menu(root)
    root.config(menu = barra_menu)

    menu_inicio = tb.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='configuración')
    barra_menu.add_cascade(label='Ayudas')

class Frame1(tb.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root                        
        self.id_usuario = None

        self.img = tk.PhotoImage(file="./img/logo.png")
        self.img = self.img.subsample(4,4)
        lbl_img = tb.Label(root, padding=18, background="#FFE4B5",   image = self.img)        
        lbl_img.grid(row=0, column=0, padx=0, pady=0)
        
        self.label = tb.Label(root, padding=43, text='Servicio Nacional de Aprendizaje\n          Préstamo Equipos',font=('Arial', 18,'bold'), bootstyle="success", background="#FFE4B5", width='44', anchor='center')
        self.label.grid(row=0, column=1, padx=0, pady=0)
        
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=1, column=0,padx=0, pady=0)
        
        
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=2, column=0)
               
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=3, column=0)
        
        self.boton_guardar = tb.Button(root, text="Prestar", width=15, bootstyle='info')
        self.boton_guardar.grid(row=3, column=0, padx=5, pady=5)

        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=2, column=0)
        
        self.boton_guardar = tb.Button(root, text="Verificar", width=15, bootstyle='secondary')
        self.boton_guardar.grid(row=2, column=0, padx=5, pady=5)
        
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=4, column=0)
        
        self.boton_guardar = tb.Button(root, text="cerrar", width=15, bootstyle='danger')
        self.boton_guardar.grid(row=4, column=0, padx=5, pady=5)
              
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=5, column=0,padx=0, pady=0)
        
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=6, column=0,padx=0, pady=0)
        
        self.label = tb.Label(root, padding=20, text='',font=('Arial', 12,'bold'), bootstyle="dark", background="#FFE4B5", width='12', anchor='center')
        self.label.grid(row=7, column=0,padx=0, pady=0)
        
        
        
    
        
        
        
        
        
        
              
        
        
        
        
       

        