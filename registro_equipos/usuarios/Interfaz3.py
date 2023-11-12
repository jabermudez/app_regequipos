def asignar_equipo_a_usuario_db(codigo_usuario, codigo_equipo):
    # ... tu código existente ...

    if estado[0] == 'disponible':
        # El equipo está disponible, procede con la asignación
        conexion.cursor.execute("UPDATE equipos SET estado = 'asignado', id_usuario = ?, fecha_asignacion = ? WHERE id_equipo = ?", (id_usuario, fecha_asignacion, id_equipo))
        conexion.conn.commit()  # Guarda los cambios en la base de datos
        return True, "Equipo asignado correctamente al usuario."
    else:
        return False, "El equipo no está disponible o ya está asignado."
    # ... tu código existente ...


def registrar_entrega(codigo_equipo):
    # ... tu código existente ...

    if id_usuario:
        # Registra la fecha y hora de la entrega y actualiza el estado del equipo
        conexion.cursor.execute("UPDATE usuarios SET id_equipo = NULL, fecha_entrega = ? WHERE id_usuario = ?", (fecha_entrega, id_usuario[0]))
        conexion.cursor.execute("UPDATE equipos SET estado = 'disponible', id_usuario = NULL, fecha_entrega = ? WHERE id_equipo = ?", (fecha_entrega, id_equipo,))
        conexion.conn.commit()  # Guarda los cambios en la base de datos
        return True, "Entrega registrada y equipo disponible para asignación."
    else:
        return False, "Este equipo no está asignado a ningún usuario y ya está disponible."
    # ... tu código existente ...
