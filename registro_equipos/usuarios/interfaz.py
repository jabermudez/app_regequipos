import tkinter as tk
import tkinter.font as tkfont
import ttkbootstrap as tb
from tkinter import ttk, messagebox
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import Usuario, guardar, listar, editar, eliminar


class Frame(tb.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root               
        self.id_usuario = None

        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n        \n          Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle='light', anchor='center')
        self.label.configure(background='#1464f6', width=93)        
        self.label.grid(row=0, column=0, columnspan=6, padx=0, pady=0, ipady=30)
        
        
        self.img = tk.PhotoImage(file="./img/logo1.png")
        self.img = self.img.subsample(4,4)
        self.lbl_img = tb.Label(root,  image = self.img)
        self.lbl_img.configure(background='#1464f6')                
        self.lbl_img.grid(row=0, column=0, padx=20, pady=0, ipadx=10, sticky='w')
       
        
        self.label = tb.Label(root, text='Registro Equipos Prestados',font=('Arial', 16, 'bold'))
        self.label.configure(foreground='#1464f6')
        self.label.grid(row=1, column=0, columnspan=2, padx=55,  pady=20,  sticky='w')

        self.campos_usuarios()
        self.deshabilitar_campos()
        self.tabla_usuarios()
    
    def campos_usuarios(self):
        #label de cada campo
        self.label_nombre = tb.Label(self, text='Nombres: ', font=('Arial', 12), bootstyle="dark")
        self.label_nombre.grid(row=2, column=0,  pady=10, sticky="e")

        self.label_apellido = tb.Label(self, text='Apellidos: ',font=('Arial', 12), bootstyle="dark")
        self.label_apellido.grid(row=3, column=0,  pady=10, sticky="e")

        self.label_documento = tb.Label(self, text='Identificación: ', font=('Arial', 12), bootstyle="dark")
        self.label_documento.grid(row=4, column=0, pady=10, sticky="e")
        
        self.label_ficha = tb.Label(self, text='Ficha: ', font=('Arial', 12), bootstyle="dark")
        self.label_ficha.grid(row=2, column=2,  pady=10, sticky="e")

        self.label_correo = tb.Label(self, text='Correo: ',font=('Arial', 12), bootstyle="dark")
        self.label_correo.grid(row=3, column=2,  pady=10, sticky="e")

        self.label_celular = tb.Label(self, text='Celular: ', font=('Arial', 12), bootstyle="dark")
        self.label_celular.grid(row=4, column=2, pady=10, sticky="e")

         #Campos de entrada
        self.mi_nombre = tb.StringVar()
        self.entry_nombre = tb.Entry(self, textvariable=self.mi_nombre, width=42)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=10 )

        self.mi_apellido = tb.StringVar()
        self.entry_apellido = tb.Entry(self, textvariable=self.mi_apellido, width=42)
        self.entry_apellido.grid(row=3, column=1, padx=10, pady=10)

        self.mi_documento = tb.StringVar()
        self.entry_documento = tb.Entry(self, textvariable=self.mi_documento, width=42)
        self.entry_documento.grid(row=4, column=1, padx=10, pady=10)
        
        self.mi_ficha = tb.StringVar()
        self.entry_ficha = tb.Entry(self, textvariable=self.mi_ficha, width=42)
        self.entry_ficha.grid(row=2, column=3, padx=10, pady=10)

        self.mi_correo = tb.StringVar()
        self.entry_correo = tb.Entry(self, textvariable=self.mi_correo, width=42)
        self.entry_correo.grid(row=3, column=3, padx=10, pady=10)

        self.mi_celular = tb.StringVar()
        self.entry_celular = tb.Entry(self, textvariable=self.mi_celular, width=42)
        self.entry_celular.grid(row=4, column=3, padx=10, pady=10)

        #Botones

        self.boton_nuevo = tb.Button(self, text="Nuevo", width=10, bootstyle='primary', command=self.habilitar_campos)
        self.boton_nuevo.grid(row=5, column=0,  pady=5, sticky='ew')

        self.boton_guardar = tb.Button(self, text="Guardar", width=10, bootstyle='info', command=self.guardar_datos)
        self.boton_guardar.grid(row=6, column=0, pady=5, sticky='ew')

        self.boton_cancelar = tb.Button(self, text="Cancelar", width=10, bootstyle='danger', command=self.deshabilitar_campos)
        self.boton_cancelar.grid(row=7, column=0,  pady=5, sticky='ew')

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_documento.set('')
        self.mi_ficha.set('')
        self.mi_correo.set('')
        self.mi_celular.set('')
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_documento.config(state='normal')
        self.entry_ficha.config(state='normal')
        self.entry_correo.config(state='normal')
        self.entry_celular.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

        pass

    def deshabilitar_campos(self):
        self.id_usuario = None

        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_documento.set('')
        self.mi_ficha.set('')
        self.mi_correo.set('')
        self.mi_celular.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_documento.config(state='disabled')
        self.entry_ficha.config(state='disabled')
        self.entry_correo.config(state='disabled')
        self.entry_celular.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        usuario = Usuario(
            self.mi_nombre.get(),
            self.mi_apellido.get(),
            self.mi_documento.get(),
            self.mi_ficha.get(),
            self.mi_correo.get(),
            self.mi_celular.get(),
        )

        if self.id_usuario == None:
            guardar(usuario)
        else:
            editar(usuario, self.id_usuario)

        
        self.tabla_usuarios()

        #Deshabilitar campos
        self.deshabilitar_campos()
    
    def tabla_usuarios(self):

        #Recuperar la lista de usuarios
        self.lista_usuarios =listar()
        self.lista_usuarios.reverse()
        
             
        #Definir columnas        
        self.tabla = ttk.Treeview(self, columns=('Código','Nombres', 'Apellidos', 'Documento','Ficha','Correo','Celular' ),bootstyle="dark")              
        self.tabla.grid(row=5, column=1, columnspan=8, rowspan=2, padx=10, pady=10, sticky='w')

        
        #Scrollbar para la tabla si exede 10 registros
        self.scroll = tk.Scrollbar(self,
        orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row = 5, column=8, rowspan=2, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.column('#0', width=50)
        self.tabla.column('#1', width=50) 
        self.tabla.column('#2', width=150)
        self.tabla.column('#3', width=120)
        self.tabla.column('#4', width=80)
        self.tabla.column('#5', width=50)
        self.tabla.column('#6', width=200)
        self.tabla.column('#7', width=80)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Codigo')
        self.tabla.heading('#2', text='Nombres')
        self.tabla.heading('#3', text='Apellidos')
        self.tabla.heading('#4', text='Documento')
        self.tabla.heading('#5', text='Ficha')
        self.tabla.heading('#6', text='Correo')
        self.tabla.heading('#7', text='Celular')


        #Iterar la lista de usuarios

        for u in self.lista_usuarios:
            self.tabla.insert('',0, text=u[0], values=(u[1], u[2], u[3],u[4],u[5],u[6],u[7]))


        #Botón Editar
        self.boton_editar = tb.Button(self, text="Editar", width=15, bootstyle='warning', command= self.editar_datos)
        self.boton_editar.grid(row=7, column=1, pady=10)

        #Botón Eliminar
        self.boton_eliminar = tb.Button(self, text="Eliminar", width=15, bootstyle='danger', command=self.eliminar_datos)
        self.boton_eliminar.grid(row=7, column=3,  pady=5)

    def editar_datos(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']            
            self.nombre_usuario =self.tabla.item(self.tabla.selection())['values'][1]            
            self.apellido_usuario =self.tabla.item(self.tabla.selection())['values'][2]
            self.documento_usuario =self.tabla.item(self.tabla.selection())['values'][3]
            self.ficha_usuario =self.tabla.item(self.tabla.selection())['values'][4]
            self.correo_usuario =self.tabla.item(self.tabla.selection())['values'][5]
            self.celular_usuario =self.tabla.item(self.tabla.selection())['values'][6]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_usuario)
            self.entry_apellido.insert(0, self.apellido_usuario)
            self.entry_documento.insert(0, self.documento_usuario)
            self.entry_ficha.insert(0, self.ficha_usuario)
            self.entry_correo.insert(0, self.correo_usuario)
            self.entry_celular.insert(0, self.celular_usuario)
        
        except:
            titulo = 'Edición de datos'
            mensaje = 'No se ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)
    
    def eliminar_datos(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_usuario)
            self.tabla_usuarios()
            self.id_usuario = None
        
            #Deshabilitar campos
            self.deshabilitar_campos()

        except:
            titulo = 'Eliminar un Registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

   