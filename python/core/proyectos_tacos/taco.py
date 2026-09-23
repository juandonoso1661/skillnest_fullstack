from flask_app.config.mysqlconnection import connectToMySQL


class Taco:

    def __init__(self, data):
        self.id = data["id"]
        self.tortilla = data["tortilla"]
        self.guiso = data["guiso"]
        self.salsa = data["salsa"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s);
        """

        return connectToMySQL("esquema_tacos").query_db(query, data)


    @classmethod
    def get_all(cls):
        query = """
            SELECT
                id,
                tortilla,
                guiso,
                salsa,
                created_at,
                updated_at
            FROM tacos
            ORDER BY id;
        """

        resultados = connectToMySQL(
            "esquema_tacos"
        ).query_db(query)

        tacos = []

        for taco in resultados:
            tacos.append(cls(taco))

        return tacos


    @classmethod
    def get_one(cls, taco_id):
        query = """
            SELECT
                id,
                tortilla,
                guiso,
                salsa,
                created_at,
                updated_at
            FROM tacos
            WHERE id = %(id)s;
        """

        data = {
            "id": taco_id
        }

        resultado = connectToMySQL(
            "esquema_tacos"
        ).query_db(query, data)

        if resultado:
            return cls(resultado[0])

        return None


    @classmethod
    def update(cls, data):
        query = """
            UPDATE tacos
            SET tortilla = %(tortilla)s,
                guiso = %(guiso)s,
                salsa = %(salsa)s
            WHERE id = %(id)s;
        """

        return connectToMySQL(
            "esquema_tacos"
        ).query_db(query, data)


    @classmethod
    def delete(cls, taco_id):
        query = """
            DELETE FROM tacos
            WHERE id = %(id)s;
        """

        data = {
            "id": taco_id
        }

        return connectToMySQL(
            "esquema_tacos"
        ).query_db(query, data)