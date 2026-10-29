from config.mysqlconnection import MySQLConnection


class Usuario:

    def __init__(self, data):
        self.id_usuario = data["id_usuario"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data.get("created_at")


    @classmethod
    def crear_usuario(cls, data):

        query = """
        INSERT INTO usuarios
        (nombre, apellido, email, password)
        VALUES
        (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """

        return MySQLConnection.query_db(query, data)



    @classmethod
    def buscar_por_email(cls, email):

        query = """
        SELECT *
        FROM usuarios
        WHERE email = %(email)s;
        """

        resultado = MySQLConnection.query_db(
            query,
            {
                "email": email
            }
        )

        if resultado:
            return cls(resultado[0])

        return None



    @classmethod
    def buscar_por_id(cls, id_usuario):

        query = """
        SELECT *
        FROM usuarios
        WHERE id_usuario = %(id_usuario)s;
        """

        resultado = MySQLConnection.query_db(
            query,
            {
                "id_usuario": id_usuario
            }
        )

        if resultado:
            return cls(resultado[0])

        return None