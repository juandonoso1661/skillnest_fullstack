from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Categoria:
    BASE_DATOS = "tasktrack"

    def __init__(self, datos):
        self.id = datos['id']
        self.nombre_categoria = datos['nombre_categoria']
        self.usuario_id = datos['usuario_id']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        # Campo calculado opcional para la vista de categorías
        self.cantidad_tareas = datos.get('cantidad_tareas', 0)

    @classmethod
    def guardar(cls, datos):
        query = """INSERT INTO categorias (nombre_categoria, usuario_id) 
                   VALUES (%(nombre_categoria)s, %(usuario_id)s);"""
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_por_usuario(cls, datos):
        query = "SELECT * FROM categorias WHERE usuario_id = %(usuario_id)s ORDER BY nombre_categoria ASC;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        return [cls(fila) for fila in resultados] if resultados else []

    @classmethod
    def obtener_por_usuario_con_conteo(cls, datos):
        query = """SELECT categorias.*, COUNT(tareas.id) AS cantidad_tareas 
                   FROM categorias 
                   LEFT JOIN tareas ON categorias.id = tareas.categoria_id 
                   WHERE categorias.usuario_id = %(usuario_id)s 
                   GROUP BY categorias.id;"""
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        return [cls(fila) for fila in resultados] if resultados else []

    @staticmethod
    def validar_categoria(datos):
        es_valido = True
        if len(datos['nombre_categoria'].strip()) < 3:
            flash("El nombre de la categoría debe tener al menos 3 caracteres.", "categoria")
            es_valido = False

        # Verificar que el usuario no repita el nombre de una categoría
        query = "SELECT * FROM categorias WHERE nombre_categoria = %(nombre_categoria)s AND usuario_id = %(usuario_id)s;"
        resultados = connectToMySQL(Categoria.BASE_DATOS).query_db(query, datos)
        if resultados:
            flash("Ya tienes una categoría con ese nombre.", "categoria")
            es_valido = False

        return es_valido