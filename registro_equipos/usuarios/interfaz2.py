import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import crear_tabla, borrar_tabla
from model.usuario_dao import Usuario, buscar

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
        self.img = self.img.subsample(3,3)
        lbl_img = tb.Label(root, padding=18, image = self.img)        
        lbl_img.grid(row=0, column=0, padx=0, pady=0)
        
        
        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n         Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle="success", anchor='center')
        self.label.grid(row=0, column=1, padx=0, pady=0)
        
        #self.label = tb.Label(root, text='Préstamo Equipos',font=('Arial', 14), bootstyle="success", anchor='center')
        #self.label.grid(row=1, column=1, padx=0, pady=0)
        
      
        self.label = tb.Label(root, padding=10, text='Código Usuario',font=('Arial', 14,'bold'), bootstyle="dark",  anchor='center')
        self.label.grid(row=2, column=0, padx=0, pady=0)
                   
        self.label_informacion = tb.Label(root, text="", font=('Roboto', 16,'bold'))
        self.label_informacion.grid(row=4, column=1, padx=10, pady=10)
        
        
        #Botones
        #style botones
        
        my_style = tb.Style()        
        my_style.configure('primary.TButton', font=("Roboto",16))
        my_style.configure('info.TButton', font=("Roboto",16))
        my_style.configure('danger.TButton', font=("Roboto",16))
        
        self.button_verificar = tb.Button(root, text="Verificar", 
            bootstyle='primary',
            style="primary.Tbutton",
            width=12, 
            command=self.buscar_datos)
        self.button_verificar.grid(row=4, column=0, ipadx=5, ipady=15,padx=10, pady=10)   
        
        self.boton_prestar = tb.Button(root, text="Prestar", 
            bootstyle='info',
            style="info.Tbutton",
            width=12)
        self.boton_prestar.grid(row=5, column=0,ipadx=5, ipady=15, padx=10, pady=10)

        
        self.boton_cerrar = tb.Button(root, text="Cerrar", 
            bootstyle='danger',
            style="danger.Tbutton",
            width=12)
        self.boton_cerrar.grid(row=6, column=0,ipadx=5, ipady=15, padx=10, pady=10)
        
        #Entradas
        self.entry_nombre = tb.Entry(root, font=('Arial', 11), bootstyle='secondary')
        self.entry_nombre.grid(row=3, column=0, padx=5, pady=5)
        
        
        #Campos de entrada
        
    
    def buscar_datos(self):
        
        nombre = self.entry_nombre.get()            
        self.nombre = ""              
        usuario = buscar(nombre)        
                
        if usuario is not None:
        
            self.nombre = usuario[1]
            self.apellidos = usuario[2]
            self.documento = usuario[3]
                          
    # Mostrar la información del usuario
        
            self.label_informacion.config (text="Nombre: %s\nApellidos: %s\nDocumento: %s" % (self.nombre, self.apellidos, self.documento))
        else: 
            self.label_informacion.config(text="El usuario no se encuentra en la base de datos")
            
            
        
        
        
              
        
        
        
        
       

        