from .conexion_db import ConexionDB
from tkinter import messagebox
from datetime import datetime

#Crea la tabla usuarios desde el aplicativo

def crear_tabla():
    conexion = ConexionDB()
    
    sql_equipos = '''
    CREATE TABLE IF NOT EXISTS equipos(
        id_equipo INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_equipo INTEGER,
        marca_equipo VARCHAR(100),
        serial_equipo VARCHAR(100),
        placa_equipo INTERGER
        
    )'''

    sql_usuarios = '''
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo INTEGER,
        nombre VARCHAR(100),
        apellidos VARCHAR(100),
        documento INTEGER,
        ficha VARCHAR(50),
        correo VARCHAR(100),
        celular INTEGER
    )'''

    try:
        # Crear la tabla equipos
        conexion.cursor.execute(sql_equipos)

        # Crear la tabla usuarios
        conexion.cursor.execute(sql_usuarios)

        # Confirmar cambios
        conexion.cerrar()

        titulo = 'Crear Registro'
        mensaje = 'Se crearon las tablas en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except Exception as e:
        titulo = 'Crear Registro'
        mensaje = 'Error al crear las tablas: ' + str(e)
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
    def __init__(self, codigo, nombre, apellidos, documento, ficha,correo,celular, id_equipo):
        self.id_usuario = None
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellidos
        self.documento = documento
        self.ficha = ficha
        self.correo = correo
        self.celular = celular
        self.id_equipo = id_equipo
    
    def __str__(self):
        return f'Usuario[{self.codigo},{self.nombre}, {self.apellido}, {self.documento},{self.ficha},{self.correo},{self.celular},{self.id_equipo}]'

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


# Función para consultar los préstamos
def consultar_prestamos():
    conexion = ConexionDB()   
    
    
    conexion.cursor.execute("""
        SELECT u.codigo, u.nombre, u.apellidos, p.fecha_asignacion, p.fecha_entrega
        FROM usuarios u
        JOIN prestamos p ON u.id_usuario = p.id_usuario
    """)
    
    prestamos = conexion.cursor.fetchall()
    conexion.cerrar()
    return prestamos







#Se crea la clase equipo

class Equipo:
    def __init__(self, codigo_equipo, marca_equipo, serial_equipo, placa_equipo):
        self.id_equipo = None
        self.codigo_equipo = codigo_equipo
        self.marca = marca_equipo
        self.serial_equipo = serial_equipo
        self.placa_equipo = placa_equipo
        
    def __str__(self):
        return f'Usuario[{self.codigo_equipo},{self.marca}, {self.serial_equipo}, {self.placa_equipo}]'

def guardar_equipo(equipo):
    conexion = ConexionDB()

    sql =f"""INSERT INTO equipos (codigo_equipo, marca, serial_equipo, placa_equipo)
    VALUES({equipo.codigo},'{equipo.marca}','{equipo.serial_equipo}', {equipo.placa_equipo})"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexiòn al Registro'
        mensaje = 'La tabla equipos no se encuentra registrada'
        messagebox.showerror(titulo, mensaje)

def listar_equipo():

    conexion = ConexionDB()

    lista_equipos = []
    sql = 'SELECT * FROM equipos'

    try:
        conexion.cursor.execute(sql)
        lista_equipos = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexiòn al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_equipos

def editar_equipo(equipo, id_equipo):
    conexion = ConexionDB()

    sql = f"""UPDATE usuarios 
    SET codigo_equipo = {equipo.codigo}, marca ='{equipo.marca_equipo}', serial_equipo ='{equipo.serial_equipo}', placa_equipo = {equipo.placa} WHERE id_equipo = {id_equipo}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar_equipo(id_equipo):
    conexion = ConexionDB()
    sql = f'DELETE FROM equipos WHERE id_equipo = {id_equipo}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se pudo eliminar este registro'
        messagebox.showerror(titulo, mensaje)

def buscareq(codigo_equipo):
    conexion = ConexionDB()    
        
    # Consultar la base de datos
    conexion.cursor.execute("SELECT * FROM equipos WHERE codigo_equipo = ?", (codigo_equipo,))
    
    equipo = conexion.cursor.fetchone()    
    conexion.cerrar()     
    return equipo


    
import sqlite3


def obtener_id_usuario_por_codigo(codigo_usuario, conexion):
    conexion = ConexionDB()  
    try:
        sql = "SELECT id_usuario FROM usuarios WHERE codigo = ?"
        conexion.cursor.execute(sql, (codigo_usuario,))
        resultado = conexion.cursor.fetchone()
        return resultado[0] if resultado else None
    except sqlite3.Error as e:
        print(f"Error al obtener id_usuario: {e}")
        return None

def obtener_id_equipo_por_codigo(codigo_equipo, conexion):
    conexion = ConexionDB()  
    try:
        sql = "SELECT id_equipo FROM equipos WHERE codigo_equipo = ?"
        conexion.cursor.execute(sql, (codigo_equipo,))
        resultado = conexion.cursor.fetchone()
        return resultado[0] if resultado else None
    except sqlite3.Error as e:
        print(f"Error al obtener id_equipo: {e}")
        return None



def asignar_equipo_a_usuario_db(codigo_usuario, codigo_equipo):
    conexion = ConexionDB()
    fecha_asignacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Obtiene los ID de usuario y equipo basados en los códigos proporcionados
        id_usuario = obtener_id_usuario_por_codigo(codigo_usuario, conexion)
        id_equipo = obtener_id_equipo_por_codigo(codigo_equipo, conexion)

        if id_usuario is None or id_equipo is None:
            return False, "El código de usuario o equipo no existe."

        # Verifica si el usuario ya tiene un equipo asignado
        sql_verificacion = "SELECT * FROM prestamos WHERE id_usuario = ? AND fecha_entrega IS NULL"
        conexion.cursor.execute(sql_verificacion, (id_usuario,))
        prestamo_activo = conexion.cursor.fetchone()

        if prestamo_activo:
            return False, "Este usuario ya tiene un equipo asignado."

        # Verifica el estado del equipo
        conexion.cursor.execute("SELECT estado FROM equipos WHERE id_equipo = ?", (id_equipo,))
        estado = conexion.cursor.fetchone()
        if estado and estado[0] != 'disponible':
            return False, "El equipo no está disponible."

        # Si está disponible y el usuario no tiene asignaciones previas, procede a asignar el equipo
        sql_prestamo = "INSERT INTO prestamos (id_usuario, id_equipo, fecha_asignacion) VALUES (?, ?, ?)"
        conexion.cursor.execute(sql_prestamo, (id_usuario, id_equipo, fecha_asignacion))
        sql_equipo = "UPDATE equipos SET estado = 'asignado' WHERE id_equipo = ?"
        conexion.cursor.execute(sql_equipo, (id_equipo,))
        
        #conexion.conn.commit()  # Guarda los cambios en la base de datos
        return True, "Equipo asignado correctamente al usuario."
        
    except sqlite3.Error as e:
        return False, f"Error al asignar el equipo: {e}"
    finally:
        conexion.cerrar()


def registrar_entrega(codigo_usuario, codigo_equipo):
    conexion = ConexionDB()
    fecha_entrega = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        id_usuario = obtener_id_usuario_por_codigo(codigo_usuario, conexion)
        id_equipo = obtener_id_equipo_por_codigo(codigo_equipo, conexion)

        if id_usuario is None or id_equipo is None:
            return False, "Usuario o equipo no encontrado."

        # Actualiza la tabla prestamos con la fecha de entrega
        sql_prestamo = """
            UPDATE prestamos
            SET fecha_entrega = ?
            WHERE id_usuario = ? AND id_equipo = ? AND fecha_entrega IS NULL
        """
        conexion.cursor.execute(sql_prestamo, (fecha_entrega, id_usuario, id_equipo))
        
        if conexion.cursor.rowcount == 0:
            return False, "No se encontró un préstamo activo para este usuario y equipo o ya ha sido entregado."

        # Opcional: Actualiza la tabla de equipos para reflejar que el equipo está disponible
        sql_equipo = "UPDATE equipos SET estado = 'disponible' WHERE id_equipo = ?"
        conexion.cursor.execute(sql_equipo, (id_equipo,))
        
       
        return True, "Entrega registrada correctamente y equipo disponible."

    except sqlite3.Error as e:
        return False, f"Error al registrar la entrega: {e}"
    finally:
        conexion.cerrar()

def obtener_conexion():
    return sqlite3.connect('tu_base_de_datos.db')  # Cambia esto por la ruta correcta a tu base de datos


