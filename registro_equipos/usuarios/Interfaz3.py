import tkinter as tk
import tkinter.font as tkfont
import ttkbootstrap as tb
from tkinter import ttk, messagebox
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import consultar_prestamos



class Frame3(tb.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
                                
        self.id_usuario = None
        self.id_equipo = None
        self.id_prestamo = None                     
        
        
        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n        \n          Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle='light', anchor='center')
        self.label.configure(background='#1464f6', width=93)        
        self.label.grid(row=0, column=0, columnspan=6, padx=0, pady=0, ipady=30)
        
        
        self.img = tk.PhotoImage(file="./img/logo1.png")
        self.img = self.img.subsample(4,4)
        self.lbl_img = tb.Label(root,  image = self.img)
        self.lbl_img.configure(background='#1464f6')                
        self.lbl_img.grid(row=0, column=0, padx=20, pady=0, ipadx=10, sticky='w')

        self.tabla_prestamos()
        
        self.label = tb.Label(root, text='Registro Equipos Prestados',font=('Arial', 16, 'bold'))
        self.label.configure(foreground='#1464f6')
        self.label.grid(row=1, column=0, columnspan=2, padx=50, pady=30,  sticky='w')
# Función para mostrar los préstamos en una tabla
       
        my_style = tb.Style()                      
        my_style.configure('primary.TButton', font=("Roboto",16), anchor='center')        
        #Botón Editar
        self.boton_cerrar = tb.Button(self, text="Cerrar", 
        style="primary.Tbutton",                                   
        width=15,
        command=root.destroy)
        self.boton_cerrar.grid(row=3, column=0, columnspan=6,  ipadx=5, ipady=10)
        
    def tabla_prestamos(self):

        #Recuperar la lista de usuarios
        self.lista_prestamo = consultar_prestamos()
        
        estilo = ttk.Style()
        fuente_grande = tkfont.Font(family="Arial", size=12)
        estilo.configure("Treeview", font=fuente_grande)

        #Definir columnas        
        self.tabla = ttk.Treeview(self, columns=('Código', 'Nombres', 'Apellidos','Codigo equipo', 'Fecha Prestamo', 'Fecha Entrega'), bootstyle="dark")
        self.tabla.grid_columnconfigure(index=1, weight=2) 
        self.tabla.grid(row=0, column=0, columnspan=6, padx=10, pady=20, sticky='w')

        self.tabla.column('#0', width=0, stretch=tk.NO)
        self.tabla.column('#1', width=80, anchor=tk.CENTER, stretch=tk.YES) 
        self.tabla.column('#2', width=120, anchor=tk.W, stretch=tk.YES)
        self.tabla.column('#3', width=120, anchor=tk.W, stretch=tk.YES)
        self.tabla.column('#4', width=70, anchor=tk.CENTER, stretch=tk.YES)
        self.tabla.column('#5', width=200, anchor=tk.CENTER, stretch=tk.YES)
        self.tabla.column('#6', width=200, anchor=tk.CENTER, stretch=tk.YES)        

       
        self.tabla.heading('#0', text='', anchor=tk.CENTER)
        self.tabla.heading('#1', text='Codigo', anchor=tk.CENTER)
        self.tabla.heading('#2', text='Nombres', anchor=tk.CENTER)
        self.tabla.heading('#3', text='Apellidos',anchor=tk.CENTER)
        self.tabla.heading('#4', text='Codigo', anchor=tk.CENTER)
        self.tabla.heading('#5', text='Fecha - Préstamo', anchor=tk.CENTER)
        self.tabla.heading('#6', text='Fecha - Entrega', anchor=tk.CENTER)
        

        
        #Iterar la lista de prestamos
        
        for u in self.lista_prestamo:
            self.tabla.insert('', tk.END, values=u)
        
        self.tabla.grid(row=2, column=0, columnspan=6, ipadx=20, ipady=80, sticky='nsew')

       

        
       