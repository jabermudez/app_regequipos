import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from model.usuario_dao import buscar, buscareq, asignar_equipo_a_usuario_db, registrar_entrega, contar_equipos_prestados
from model.usuario_dao import Usuario, Equipo




class Frame1(tb.Frame):
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
                    
         
        self.label = tb.Label(root, text='Préstamo Equipos',font=('Arial', 20, 'bold'))
        self.label.configure(foreground='#1464f6')
        self.label.grid(row=1, column=0, columnspan=2, padx=20, pady=20, ipadx=10, sticky='w')
           
      
        self.label = tb.Label(root, text='Código Usuario',font=('Arial', 12,'bold'), bootstyle="dark")
        self.label.grid(row=2, column=0,  padx=30,  pady=30,  sticky='e')
        
                   
        self.label = tb.Label(root, text='# Equipo',font=('Arial', 12,'bold'), bootstyle="dark")
        self.label.grid(row=2, column=2, padx=20, pady=30, sticky='e')           
              
         
        
        #self.label_informacion = tb.Label(root, text="", font=('Roboto', 12, 'bold'),  anchor='center')
        #self.label_informacion.configure(foreground='#1464f6', width='29')
        #self.label_informacion.grid(row=4, column=0, columnspan=2, padx=20, pady=20, ipady=10, sticky='nsew')
        
        # Utiliza Frame para agrupar elementos relacionados
        self.info_frame = tb.Frame(root,  padding=(1, 1, 1, 1), relief='raised',border=5, bootstyle="primary")
        
        
        # En este marco puedes colocar toda la información del usuario
        self.label_informacion = tb.Label(self.info_frame, text="", font=('Roboto', 12),anchor='center')
        self.label_informacion.configure(foreground='#1464f6', width='45')
        self.label_informacion.grid(row=4, column=1, sticky='w')    
        
        
        self.img1 = tk.PhotoImage(file="./img/user.png")
        self.img1 = self.img1.subsample(3,3)
        self.lbl_img1 = tb.Label(root,  image = self.img1)                    
        self.lbl_img1.grid(row=4, column=0, columnspan=2, padx=120, pady=5)
        
        
        #self.label_informacion1 = tb.Label(root, text="", font=('Roboto', 12, 'bold'),  anchor='center')
        #self.label_informacion1.configure(foreground='#1464f6', width='29')
        #self.label_informacion1.grid(row=4, column=2, columnspan=2, padx=20, pady=20, ipady=10)
        
        self.img2 = tk.PhotoImage(file="./img/equipo.png")
        self.img2 = self.img2.subsample(2,2)
        self.lbl_img2 = tb.Label(root,  image = self.img2)                    
        self.lbl_img2.grid(row=4, column=2, columnspan=2, padx=0, pady=5)

        

        #Botones
        #style botones
        
        my_style = tb.Style()        
        my_style.configure('primary.TButton', font=("Roboto",16))        
        my_style.configure('info.TButton', font=("Roboto",16))
        my_style.configure('danger.TButton', font=("Roboto",16))
        
       
        self.button_verificar = tb.Button(root, text="Verificar",                                          
            style="primary.Tbutton",            
            width=15, 
            command=self.buscar_equipo)
        self.button_verificar.grid(row=3, column=0, columnspan=2, pady=10, ipady=15)   
        
        self.boton_prestar = tb.Button(root, text="Asignar",             
            style="info.Tbutton",
            width=15,
            command=self.asignar_equipo)
        self.boton_prestar.grid(row=3, column=1, columnspan=2, pady=10, ipadx=15, ipady=15)

        
        self.boton_recibir = tb.Button(root, text="Recibir",             
            style="danger.Tbutton",
            width=15,
            command=self.entrega_equipo)
        self.boton_recibir.grid(row=3, column=2, columnspan=2,  ipadx=15, ipady=15)
        
        #Entradas
        
        self.entry_codigo = tb.Entry(root, font=('Roboto', 11), bootstyle='secondary')
        self.entry_codigo.grid(row=2, column=1, padx=0, pady=20, ipadx=0, sticky='w')
        
        self.entry_codigo_equipo = tb.Entry(root, font=('Roboto', 11), bootstyle='secondary')
        self.entry_codigo_equipo.grid(row=2, column=3,  padx=(0, 20), pady=5, sticky='w')
       
             
        my_style.configure('TLabel', font=('Roboto', 12))
        my_style.configure('TButton', font=('Roboto', 12, 'bold'))
        my_style.configure('TEntry', font=('Roboto', 12), padding=5)
        
        #Muestra la cantidad de equipos prestados                  
        self.label_equipos_prestados = tb.Label(root, text="", font=('Roboto', 14, 'bold'), bootstyle='secondary')
        self.label_equipos_prestados.configure(foreground='#1464f6')
        self.label_equipos_prestados.grid(row=5, column=1, columnspan=2)

        self.actualizar_cantidad_equipos_prestados()
        
    
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
    # Después de obtener los datos, muestra la información y oculta las imágenes
            self.info_frame.grid()  # Muestra el frame de información
            self.lbl_img.grid_remove()  # Oculta la imagen inicial del usuario
            self.lbl_img2.grid_remove()  # Oculta la imagen inicial del equipo
                    
    def mostrar_info_frame(self):         
        self.info_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=20, ) 
        
    def ocultar_info_mostrar_imagenes(self):
        # Oculta el frame con la información del usuario y del equipo
        self.info_frame.grid_remove()  # O .grid_forget() si quieres que se olvide la configuración de la grilla
        # Muestra las imágenes iniciales
        self.lbl_img1.grid()  # Muestra la imagen del logo si estaba oculta
        self.lbl_img2.grid()  # Muestra la imagen del usuario si estaba oculta
        # Puedes llamar a .grid() para cualquier otra imagen que necesites mostrar de nuevo

        
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
        
            self.label_informacion.config (text="Código: %s\nMarca: %s  \nSerial: %s\nPlaca: %s" %(self.codigo_equipo, self.marca_equipo, self.serial_equipo, self.placa_equipo),
            
                image=''  # Esto elimina la imagen del label
            )
            self.lbl_img2.grid_remove()  # Esto oculta la imagen sin eliminarla del layout
        
        else: 
            
            # Si no hay datos para el usuario, mostramos el mensaje y volvemos a mostrar la imagen
            self.label_informacion.config(text="El Equipo no se encuentra \nen la base de datos", image='')
            self.lbl_img2.grid_remove()  # Esto vuelve a mostrar la imagen
        
        self.buscar_datos()
        self.mostrar_info_frame()
        
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

        self.entry_codigo.delete(0, tk.END)
        self.entry_codigo_equipo.delete(0, tk.END)
        
        if resultado:  # Si el equipo fue asignado exitosamente
            self.equipo_asignado = True
            self.mostrar_imagenes_iniciales()
        else:
            pass

    def mostrar_imagenes_iniciales(self):
        # Si un equipo fue asignado, oculta el frame de información y muestra las imágenes iniciales
        if self.equipo_asignado or self.equipo_entregado:
            self.info_frame.grid_remove()  # Oculta la información
            self.lbl_img1.grid()  # Muestra la imagen inicial del usuario
            self.lbl_img2.grid()  # Muestra la imagen inicial del equipo
            self.equipo_asignado = False  # Restablece la variable para la próxima verificación
            self.equipo_entregado = False
            
    def entrega_equipo(self):
        codigo_usuario = self.entry_codigo.get()
        codigo_equipo = self.entry_codigo_equipo.get()
        if codigo_usuario and codigo_equipo:
            entregado, mensaje = registrar_entrega(codigo_usuario, codigo_equipo)
            messagebox.showinfo('Resultado', mensaje)
            if entregado:
                self.equipo_entregado = True
                self.mostrar_imagenes_iniciales()
                
        else:
            messagebox.showwarning('Advertencia', 'Debes ingresar el código de usuario y el de equipo para registrar la entrega.')

        self.entry_codigo.delete(0, tk.END)
        self.entry_codigo_equipo.delete(0, tk.END)
        
    def actualizar_cantidad_equipos_prestados(self):
        cantidad = contar_equipos_prestados()
        self.label_equipos_prestados.config(text=f"Equipos prestados actualmente: {cantidad}")
        # Programar la siguiente actualización en 60 segundos (60000 milisegundos)
        self.after(1,self.actualizar_cantidad_equipos_prestados)    