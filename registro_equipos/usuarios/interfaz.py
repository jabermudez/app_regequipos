import tkinter as tk


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro')
    menu_inicio.add_command(label='Eliminar Registro')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='configuración')
    barra_menu.add_cascade(label='Ayudas')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        #self.config( bg='green')

        self.campos_usuarios()
    
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
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        self.entry_documento = tk.Entry(self)
        self.entry_documento.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_documento.grid(row=2, column=1, padx=10, pady=10)

        #Botones

        self.boton_nuevo = tk.Button(self, text="Nuevo")
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
        fg='white', bg='green', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)