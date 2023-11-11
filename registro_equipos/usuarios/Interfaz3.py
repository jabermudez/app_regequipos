def registrar_entrega(codigo_usuario):
    conexion = ConexionDB()
    try:
        id_usuario = obtener_id_usuario_por_codigo(codigo_usuario, conexion)
        if id_usuario:
            # Actualiza la fecha de entrega y marca el equipo como disponible
            fecha_entrega = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "UPDATE usuarios SET fecha_entrega = ?, id_equipo = NULL WHERE id_usuario = ?"
            conexion.cursor.execute(sql, (fecha_entrega, id_usuario))
            # Debes obtener el id_equipo que se va a actualizar a 'disponible'
            # Asumiendo que se almacena en la tabla de usuarios
            conexion.cursor.execute("SELECT id_equipo FROM usuarios WHERE id_usuario = ?", (id_usuario,))
            id_equipo = conexion.cursor.fetchone()[0]
            if id_equipo:
                conexion.cursor.execute("UPDATE equipos SET estado = 'disponible' WHERE id_equipo = ?", (id_equipo,))
            conexion.conn.commit()
            return True, "Entrega registrada correctamente."
        else:
            return False, "No se encontró el usuario con ese código."
    except sqlite3.Error as e:
        return False, f"Error al registrar la entrega del equipo: {e}"
    finally:
        conexion.cerrar()
