from mysqlconnection import connectToMySQL


class Estudiante:
    """
    Representa un registro de la tabla estudiante.
    """

    def __init__(self, data):
        """
        Mapea los datos provenientes de la base de datos.
        """
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.correo = data["correo"]
        self.created_at = data["created_at"]

    # ======================================================
    # READ - OBTENER TODOS LOS ESTUDIANTES
    # ======================================================
    @classmethod
    def get_all(cls):
        query = """
            SELECT id_estudiante, nombre, correo, created_at
            FROM estudiante
            ORDER BY id_estudiante;
        """
        resultados = connectToMySQL("esquema_estudiantes").query_db(query)

        estudiantes = []
        if resultados:
            for estudiante in resultados:
                estudiantes.append(cls(estudiante))

        return estudiantes

    # ======================================================
    # READ - OBTENER UN ESTUDIANTE POR ID
    # ======================================================
    @classmethod
    def get_by_id(cls, id_estudiante):
        query = """
            SELECT id_estudiante, nombre, correo, created_at
            FROM estudiante
            WHERE id_estudiante = %(id_estudiante)s;
        """
        data = {"id_estudiante": id_estudiante}

        resultados = connectToMySQL("esquema_estudiantes").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None

    # ======================================================
    # UPDATE - ACTUALIZAR ESTUDIANTE
    # ======================================================
    @classmethod
    def actualizar(cls, data):
        """
        Recibe un diccionario con: id_estudiante, nombre y correo.
        """
        query = """
            UPDATE estudiante
            SET nombre = %(nombre)s,
                correo = %(correo)s
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)

    # ======================================================
    # DELETE - ELIMINAR ESTUDIANTE
    # ======================================================
    @classmethod
    def eliminar(cls, data):
        """
        Recibe un diccionario con: id_estudiante.
        """
        query = """
            DELETE FROM estudiante
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)