from .conexion_db import ConexionDB
from tkinter import messagebox

#Crea la tabla usuarios desde el aplicativo

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE usuarios(
        id_usuario INTEGER,
        codigo INTEGER,
        nombre VARCHAR(100),
        apellidos VARCHAR(100),
        documento INTEGER,
        ficha VARCHAR(50),
        correo VARCHAR(100),
        celular INTEGER,
        PRIMARY KEY(id_usuario AUTOINCREMENT)
    )'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de daos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya existe'
        messagebox.showwarning(titulo, mensaje)

#Permite borrar la tabla usuarios desde el aplicativo
def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE usuarios'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se ha eliminado'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para eliminar'
        messagebox.showerror(titulo, mensaje)

#Se crea la clase usuario, a travès de esta se generaràn las diferentes funciones del CRUD
class Usuario:
    def __init__(self, codigo, nombre, apellidos, documento, ficha,correo,celular):
        self.id_usuario = None
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellidos
        self.documento = documento
        self.ficha = ficha
        self.correo = correo
        self.celular = celular
    
    def __str__(self):
        return f'Usuario[{self.codigo},{self.nombre}, {self.apellido}, {self.documento},{self.ficha},{self.correo},{self.celular}]'

def guardar(usuario):
    conexion = ConexionDB()

    sql =f"""INSERT INTO usuarios (codigo, nombre, apellidos, documento, ficha, correo, celular)
    VALUES({usuario.codigo},'{usuario.nombre}','{usuario.apellido}', {usuario.documento}, '{usuario.ficha}','{usuario.correo}',{usuario.celular},)"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexiòn al Registro'
        mensaje = 'La tabla usuario no se encuentra registrada'
        messagebox.showerror(titulo, mensaje)

def listar():

    conexion = ConexionDB()

    lista_usuarios = []
    sql = 'SELECT * FROM usuarios'

    try:
        conexion.cursor.execute(sql)
        lista_usuarios = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexiòn al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_usuarios

def editar(usuario, id_usuario):
    conexion = ConexionDB()

    sql = f"""UPDATE usuarios 
    SET codigo = {usuario.codigo}, nombre ='{usuario.nombre}', apellidos ='{usuario.apellido}', documento = {usuario.documento},  ficha ='{usuario.ficha}', correo ='{usuario.correo}', celular ={usuario.celular}, WHERE id_usuario = {id_usuario}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_usuario):
    conexion = ConexionDB()
    sql = f'DELETE FROM usuarios WHERE id_usuario = {id_usuario}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se pudo eliminar este registro'
        messagebox.showerror(titulo, mensaje)

def buscar(codigo):
    conexion = ConexionDB()    
        
    # Consultar la base de datos
    conexion.cursor.execute("SELECT * FROM usuarios WHERE codigo = ?", (codigo,))
    
    usuario = conexion.cursor.fetchone()    
    conexion.cerrar()
    
    return usuario
    
    
   
    
    
    
    
    
        
    

    