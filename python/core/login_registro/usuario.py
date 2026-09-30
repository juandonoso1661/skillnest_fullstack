from mysqlconnection import MySQLConnection


class Usuario:

    def __init__(self, data):
        self.id = data.get("id_usuario")
        self.nombre = data.get("nombre")
        self.apellido = data.get("apellido")
        self.email = data.get("email")
        self.password = data.get("contrasena")

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios
            (nombre, apellido, email, contrasena)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s);
        """

        return MySQLConnection.query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = """
            SELECT *
            FROM usuarios
            WHERE email = %(email)s;
        """

        results = MySQLConnection.query_db(
            query,
            {"email": email}
        )

        if results:
            return cls(results[0])

        return None

    @classmethod
    def get_by_id(cls, id):
        query = """
            SELECT *
            FROM usuarios
            WHERE id_usuario = %(id)s;
        """

        results = MySQLConnection.query_db(
            query,
            {"id": id}
        )

        if results:
            return cls(results[0])

        return None