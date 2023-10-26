import tkinter as tk
from tkinter import ttk, messagebox

from model.usuario_dao import crear_tabla, borrar_tabla
from model.usuario_dao import Usuario, guardar, listar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='configuración')
    barra_menu.add_cascade(label='Ayudas')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config( bg='green')

        self.campos_usuarios()
        self.deshabilitar_campos()
        self.tabla_usuarios()
    
    def campos_usuarios(self):
        #label de cada campo
        self.label_nombre = tk.Label(self, text='Nombres: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido = tk.Label(self, text='Apellidos: ')
        self.label_apellido.config(font=('Arial', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)

        self.label_documento = tk.Label(self, text='Identificación: ')
        self.label_documento.config(font=('Arial', 12, 'bold'))
        self.label_documento.grid(row=2, column=0, padx=10, pady=10)

         #Campos de entrada
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.mi_apellido)
        self.entry_apellido.config(width=50,font=('Arial', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_documento = tk.StringVar()
        self.entry_documento = tk.Entry(self, textvariable=self.mi_documento)
        self.entry_documento.config(width=50, font=('Arial', 12))
        self.entry_documento.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #Botones

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='green', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='#1658A2', cursor='hand2', activebackground='#35BD6F')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='#BD122E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

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

        guardar(usuario)
        self.tabla_usuarios()

        #Deshabilitar campos
        self.deshabilitar_campos()
    
    def tabla_usuarios(self):

        #Recuperar la lista de peliculas
        self.lista_usuarios =listar()
        self.lista_usuarios.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        #Scrollbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self,
        orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row = 4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellidos')
        self.tabla.heading('#3', text='Identificación')


        #Iterar la lista de usuarios

        for u in self.lista_usuarios:
            self.tabla.insert('',0, text=u[0], values=(u[1], u[2], u[3]))


        #Botón Editar
        self.boton_editar = tk.Button(self, text="Editar")
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='green', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        #Botón Eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar")
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='#BD122E', cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_usuario = self.tabla.item(self.tabla.selection())['text']
            self.nombre_usuario =self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_usuario =self.tabla.item(self.tabla.selection())['values'][1]
            self.documento_usuario =self.tabla.item(self.tabla.selection())['values'][0]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_usuario)
            self.entry_apellido.insert(0, self.apellido_usuario)
            self.entry_documento.insert(0, self.documento_usuario)
        
        except:
            titulo = 'Edició de datos'
            mensaje = 'No se ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)