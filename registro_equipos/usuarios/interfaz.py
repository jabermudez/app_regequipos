import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk, messagebox
from model.usuario_dao import Usuario, guardar, listar, editar, eliminar


class Frame(tb.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()        
        self.id_usuario = None

        self.label_tituloinst = tb.Label(self, text='REGISTRO DE USUARIOS',  font=('Arial', 16, 'bold'),bootstyle="success")
        self.label_tituloinst.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


        self.img = tk.PhotoImage(file="./img/logo.png")
        self.img = self.img.subsample(3,3)
        lbl_img = tk.Label(self, bg='#FFA030', image = self.img)        
        lbl_img.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

        self.label_nominst = tb.Label(self, text='Servicio Nacional\n de Aprendizaje ',font=('Arial', 12,'bold'), bootstyle="dark")
        self.label_nominst.grid(row=3, column=0, padx=10, pady=10)

        self.campos_usuarios()
        self.deshabilitar_campos()
        self.tabla_usuarios()
    
    def campos_usuarios(self):
        #label de cada campo
        self.label_nombre = tb.Label(self, text='Nombres: ', font=('Arial', 12), bootstyle="dark")
        self.label_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_apellido = tb.Label(self, text='Apellidos: ',font=('Arial', 12), bootstyle="dark")
        self.label_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_documento = tb.Label(self, text='Identificación: ', font=('Arial', 12), bootstyle="dark")
        self.label_documento.grid(row=3, column=1, padx=10, pady=10, sticky="w")

         #Campos de entrada
        self.mi_nombre = tb.StringVar()
        self.entry_nombre = tb.Entry(self, textvariable=self.mi_nombre, width=70)
        self.entry_nombre.grid(row=1, column=2, padx=10, pady=10, columnspan=2, sticky="w")

        self.mi_apellido = tb.StringVar()
        self.entry_apellido = tb.Entry(self, textvariable=self.mi_apellido, width=70)
        self.entry_apellido.grid(row=2, column=2, padx=10, pady=10, columnspan=2, sticky="w")

        self.mi_documento = tb.StringVar()
        self.entry_documento = tb.Entry(self, textvariable=self.mi_documento, width=70)
        self.entry_documento.grid(row=3, column=2, padx=10, pady=10, columnspan=2, sticky="w")

        #Botones

        self.boton_nuevo = tb.Button(self, text="Nuevo", width=15, bootstyle='primary', command=self.habilitar_campos)
        self.boton_nuevo.grid(row=4, column=0, padx=5, pady=5)

        self.boton_guardar = tb.Button(self, text="Guardar", width=15, bootstyle='info', command=self.guardar_datos)
        self.boton_guardar.grid(row=5, column=0, padx=5, pady=5)

        self.boton_cancelar = tb.Button(self, text="Cancelar", width=15, bootstyle='danger', command=self.deshabilitar_campos)
        self.boton_cancelar.grid(row=6, column=0, padx=5, pady=5)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_documento.set('')
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_documento.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

        pass

    def deshabilitar_campos(self):
        self.id_usuario = None

        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_documento.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_documento.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        usuario = Usuario(
            self.mi_nombre.get(),
            self.mi_apellido.get(),
            self.mi_documento.get(),
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
        self.tabla.grid(row=4, column=1, columnspan=7, rowspan=2, padx=20, pady=20, sticky='nsew')

        
        #Scrollbar para la tabla si exede 10 registros
        self.scroll = tk.Scrollbar(self,
        orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row = 4, column=7, rowspan=2, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.column('#0', width=50)
        self.tabla.column('#1', width=50) 
        self.tabla.column('#2', width=100)
        self.tabla.column('#3', width=100)
        self.tabla.column('#4', width=100)
        self.tabla.column('#5', width=50)
        self.tabla.column('#6', width=100)
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
        self.boton_editar = tb.Button(self, text="Editar", width=20, bootstyle='warning', command= self.editar_datos)
        self.boton_editar.grid(row=6, column=2, rowspan=2, padx=10, pady=20)

        #Botón Eliminar
        self.boton_eliminar = tb.Button(self, text="Eliminar", width=20, bootstyle='danger', command=self.eliminar_datos)
        self.boton_eliminar.grid(row=6, column=3, rowspan=2, padx=5, pady=15)

    def editar_datos(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']
            self.codigo_usuario =self.tabla.item(self.tabla.selection())['values'][0]
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

   