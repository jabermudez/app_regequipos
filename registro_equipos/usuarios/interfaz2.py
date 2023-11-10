import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import crear_tabla, borrar_tabla,buscar, buscareq, asignar_equipo_a_usuario_db, registrar_entrega
from model.usuario_dao import Usuario, Equipo



#Barra Menù Superior 
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
        self.id_equipo = None
        
           
        self.label = tb.Label(root, text='Servicio Nacional de Aprendizaje\n        \n          Centro Agroindustrial',font=('Arial', 18,'bold'), bootstyle='light', anchor='center')
        self.label.configure(background='#1464f6', width=93)        
        self.label.grid(row=0, column=0, columnspan=6, padx=0, pady=0, ipady=30)
        
        
        self.img = tk.PhotoImage(file="./img/logo1.png")
        self.img = self.img.subsample(4,4)
        self.lbl_img = tb.Label(root,  image = self.img)
        self.lbl_img.configure(background='#1464f6')                
        self.lbl_img.grid(row=0, column=0, padx=20, pady=0, ipadx=10, sticky='w')
                    
         
        self.label = tb.Label(root, text='Préstamo Equipos',font=('Arial', 20, 'bold'))
        self.label.configure(foreground='#1464f6')
        self.label.grid(row=1, column=0, columnspan=2, padx=20, pady=20, ipadx=10, sticky='w')
           
      
        self.label = tb.Label(root, text='Código Usuario',font=('Arial', 12,'bold'), bootstyle="dark")
        self.label.grid(row=2, column=0,  padx=30,  pady=30,  sticky='e')
        
                   
        self.label = tb.Label(root, text='# Equipo',font=('Arial', 12,'bold'), bootstyle="dark")
        self.label.grid(row=2, column=2, padx=20, pady=30, sticky='e')           
        
        
        self.label_informacion = tb.Label(root, text="", font=('Roboto', 12, 'bold'),  anchor='center')
        self.label_informacion.configure(foreground='#1464f6', width='29')
        self.label_informacion.grid(row=4, column=0, columnspan=2, padx=20, pady=20, ipady=10, sticky='nsew')
        
        self.img1 = tk.PhotoImage(file="./img/user.png")
        self.img1 = self.img1.subsample(3,3)
        self.lbl_img1 = tb.Label(root,  image = self.img1)                    
        self.lbl_img1.grid(row=4, column=0, columnspan=2, padx=120, pady=15)
        
        
        self.label_informacion1 = tb.Label(root, text="", font=('Roboto', 12, 'bold'),  anchor='center')
        self.label_informacion1.configure(foreground='#1464f6', width='29')
        self.label_informacion1.grid(row=4, column=2, columnspan=2, padx=20, pady=20, ipady=10)
        
        self.img2 = tk.PhotoImage(file="./img/equipo.png")
        self.img2 = self.img2.subsample(2,2)
        self.lbl_img2 = tb.Label(root,  image = self.img2)                    
        self.lbl_img2.grid(row=4, column=2, columnspan=2, padx=0, pady=15)


        #Botones
        #style botones
        
        my_style = tb.Style()        
        my_style.configure('primary.TButton', font=("Roboto",16))
        my_style.configure('info.TButton', font=("Roboto",16))
        my_style.configure('danger.TButton', font=("Roboto",16))
        
       
        self.button_verificar = tb.Button(root, text="Verificar", 
            bootstyle='primary',
            style="primary.Tbutton",
            width=20, 
            command=self.buscar_equipo)
        self.button_verificar.grid(row=3, column=0, columnspan=2, pady=15, ipady=15)   
        
        self.boton_prestar = tb.Button(root, text="Asignar", 
            bootstyle='info',
            style="info.Tbutton",
            width=20,
            command=self.asignar_equipo)
        self.boton_prestar.grid(row=3, column=2, columnspan=2, pady=15, ipadx=15, ipady=15)

        
        self.boton_recibir = tb.Button(root, text="Recibir", 
            bootstyle='danger',
            style="danger.Tbutton",
            width=20,
            command=self.entrega_equipo)
        self.boton_recibir.grid(row=4, column=1, columnspan=2, ipadx=15, ipady=15)
        
        #Entradas
        
        self.entry_codigo = tb.Entry(root, font=('Arial', 11), bootstyle='secondary')
        self.entry_codigo.grid(row=2, column=1, padx=0, pady=20, ipadx=0, sticky='w')
        
        self.entry_codigo_equipo = tb.Entry(root, font=('Arial', 11), bootstyle='secondary')
        self.entry_codigo_equipo.grid(row=2, column=3,  padx=(0, 20), pady=5, sticky='w')
       
             
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
        
            self.label_informacion.config (text="Código: %s\nNombre: %s  %s\nDocumento: %s\nFicha: %s\nCorreo Electrónico: %s\nCelular: %s" % (self.codigo, self.nombre, self.apellidos, self.documento,self.ficha,self.correo,self.celular),
            
                image=''  # Esto elimina la imagen del label
            )
            self.lbl_img1.grid_remove()  # Esto oculta la imagen sin eliminarla del layout
        
        else: 
            
            # Si no hay datos para el usuario, mostramos el mensaje y volvemos a mostrar la imagen
            self.label_informacion.config(text="El usuario no se encuentra \nen la base de datos", image='')
            self.lbl_img1.grid_remove()  # Esto vuelve a mostrar la imagen
    

    #Datos del Equipo
            
    def buscar_equipo(self):
        
        codigo_equipo = self.entry_codigo_equipo.get()            
        self.codigo_equipo = ""              
        equipo = buscareq(codigo_equipo)        
                
        if equipo is not None:
        
            self.codigo_equipo = equipo[1]
            self.marca_equipo = equipo[2]
            self.serial_equipo = equipo[3]
            self.placa_equipo = equipo[4]
                                      
            # Mostrar la información del usuario
        
            self.label_informacion1.config (text="Código: %s\nMarca: %s  \nSerial: %s\nPlaca: %s" %(self.codigo_equipo, self.marca_equipo, self.serial_equipo, self.placa_equipo),
            
                image=''  # Esto elimina la imagen del label
            )
            self.lbl_img2.grid_remove()  # Esto oculta la imagen sin eliminarla del layout
        
        else: 
            
            # Si no hay datos para el usuario, mostramos el mensaje y volvemos a mostrar la imagen
            self.label_informacion1.config(text="El Equipo no se encuentra \nen la base de datos", image='')
            self.lbl_img2.grid_remove()  # Esto vuelve a mostrar la imagen
        
        self.buscar_datos()
        
    def asignar_equipo(self):
        codigo_usuario = self.entry_codigo.get()
        codigo_equipo = self.entry_codigo_equipo.get()
        
        # Verifica si ambos códigos están presentes
        if codigo_usuario and codigo_equipo:
            # Llama a la función del módulo database_manager
            resultado, mensaje = asignar_equipo_a_usuario_db(codigo_usuario, codigo_equipo)
            messagebox.showinfo('Resultado', mensaje)
        else:
            messagebox.showwarning('Advertencia', 'Debes ingresar tanto el código de usuario como el de equipo.')

       
    def entrega_equipo(self):
        codigo_usuario = self.entry_codigo.get()
        if  codigo_usuario:
            entregado, mensaje = registrar_entrega(codigo_usuario)
            messagebox.showinfo('Resultado', mensaje)
        else:
            messagebox.showwarning('Advertencia', 'Debes ingresar el código de usuario para registrar la entrega.')