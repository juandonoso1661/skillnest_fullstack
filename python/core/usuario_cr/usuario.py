from mysqlconnection import connectToMySQL


class Usuario:

    def __init__(self, data):

        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def get_all(cls):

        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id;
        """

        resultados = connectToMySQL(
            "esquema_usuarios"
        ).query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(
                cls(usuario)
            )

        return usuarios