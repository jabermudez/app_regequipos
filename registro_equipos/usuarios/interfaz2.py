import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import Style
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
        
        
        
        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n        \n          Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle='light', anchor='center')
        self.label.configure(background='#1464f6', width='69')        
        self.label.grid(row=0, column=0, columnspan=4, padx=0, pady=0, ipady=30)
        
        
        self.img = tk.PhotoImage(file="./img/logo1.png")
        self.img = self.img.subsample(4,4)
        self.lbl_img = tb.Label(root,  image = self.img)
        self.lbl_img.configure(background='#1464f6')                
        self.lbl_img.grid(row=0, column=0, padx=20, pady=0, ipadx=10, sticky='w')
                    
         
        self.label = tb.Label(root, text='Préstamo Equipos',font=('Arial', 20, 'bold'), anchor='center')
        self.label.configure(foreground='#1464f6')
        self.label.grid(row=1, column=0, columnspan=4,  padx=20, pady=20, ipadx=10, sticky='w')
           
      
        self.label = tb.Label(root, padding=10, text='Código Usuario',font=('Arial', 14,'bold'), bootstyle="dark",  anchor='center')
        self.label.grid(row=2, column=0, padx=0, pady=0)
                   
        self.label = tb.Label(root, padding=10, text='# Equipos',font=('Arial', 14,'bold'), bootstyle="dark",  anchor='center')
        self.label.grid(row=2, column=2, padx=0, pady=0)           
        
        self.label_informacion = tb.Label(root, text="", font=('Roboto', 12,'bold'), anchor='center')
        self.label_informacion.configure(foreground='#1464f6')
        self.label_informacion.grid(row=4, column=0, rowspan=2, columnspan=2, padx=10, pady=10, ipadx=90, ipady=90)
      
        
      
      
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
        self.button_verificar.grid(row=3, column=0,columnspan=2, ipadx=5, ipady=15,padx=20, pady=20)   
        
        self.boton_prestar = tb.Button(root, text="Prestar", 
            bootstyle='info',
            style="info.Tbutton",
            width=12)
        self.boton_prestar.grid(row=3, column=2, columnspan=2, ipadx=5, ipady=15, padx=20, pady=20)

        
        self.boton_cerrar = tb.Button(root, text="Cerrar", 
            bootstyle='danger',
            style="danger.Tbutton",
            width=12)
        self.boton_cerrar.grid(row=4, column=2, columnspan=2, ipadx=5, ipady=15, padx=10, pady=10)
        
        #Entradas
        
        self.entry_codigo = tb.Entry(root, font=('Arial', 11), bootstyle='secondary')
        self.entry_codigo.grid(row=2, column=1, padx=5, pady=5)
        
        self.entry_equipo = tb.Entry(root, font=('Arial', 11), bootstyle='secondary')
        self.entry_equipo.grid(row=2, column=3, padx=5, pady=5)
       
       
       
        #Campos de entrada
        
    
    def buscar_datos(self):
        
        codigo = self.entry_codigo.get()            
        self.codigo = ""              
        usuario = buscar(codigo)        
                
        if usuario is not None:
        
            self.codigo = usuario[1]
            self.nombre = usuario[2]
            self.apellidos = usuario[3]
            self.documento = usuario[4]
            self.ficha = usuario[5]
            self.correo = usuario[6]
            self.celular = usuario[7]
                          
    # Mostrar la información del usuario
        
            self.label_informacion.config (text="Código: %s\nNombre: %s  %s\nDocumento: %s\nFicha: %s\nCorreo Electrónico: %s\nCelular: %s" % (self.codigo, self.nombre, self.apellidos, self.documento,self.ficha,self.correo,self.celular))
        else: 
            self.label_informacion.config(text="El usuario no se encuentra en la base de datos")
            
            
        
        
        
              
        
        
        
        
       

        