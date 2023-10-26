from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE usuarios(
        id_usuario INTEGER,
        nombre VARCHAR(100),
        apellidos VARCHAR(100),
        documento INTEGER,
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

class Usuario:
    def __init__(self, nombre, apellido, documento):
        self.id_usuario = None
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
    
    def __str__(self):
        return f'Usuario[{self.nombre}, {self.apellido}, {self.documento}]'

def guardar(usuario):
    conexion = ConexionDB()

    sql =f"""INSERT INTO usuarios (nombre, apellidos, documento)
    VALUES('{usuario.nombre}','{usuario.apellido}', {usuario.documento})"""

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
    SET nombre ='{usuario.nombre}, apellidos ='{usuario.apellido}, documento ='{usuario.documento}'
    WHERE id_usuario = '{id_usuario}'"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edició de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)
