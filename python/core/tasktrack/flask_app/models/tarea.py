from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Tarea:
    BASE_DATOS = "tasktrack"

    def __init__(self, datos):
        self.id = datos['id']
        self.titulo = datos['titulo']
        self.prioridad = datos['prioridad']
        self.fecha_limite = datos['fecha_limite']
        self.estado = datos['estado']
        self.descripcion = datos['descripcion']
        self.usuario_id = datos['usuario_id']
        self.categoria_id = datos['categoria_id']
        self.nombre_categoria = datos.get('nombre_categoria', '')
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

    @classmethod
    def guardar(cls, datos):
        query = """INSERT INTO tareas (titulo, prioridad, fecha_limite, estado, descripcion, usuario_id, categoria_id)
                   VALUES (%(titulo)s, %(prioridad)s, %(fecha_limite)s, %(estado)s, %(descripcion)s, %(usuario_id)s, %(categoria_id)s);"""
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_por_usuario(cls, datos):
        query = """SELECT tareas.*, categorias.nombre_categoria AS nombre_categoria 
                   FROM tareas 
                   JOIN categorias ON tareas.categoria_id = categorias.id 
                   WHERE tareas.usuario_id = %(usuario_id)s 
                   ORDER BY tareas.fecha_limite ASC;"""
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        return [cls(fila) for fila in resultados] if resultados else []

    @classmethod
    def obtener_por_id(cls, datos):
        query = """SELECT tareas.*, categorias.nombre_categoria AS nombre_categoria 
                   FROM tareas 
                   JOIN categorias ON tareas.categoria_id = categorias.id 
                   WHERE tareas.id = %(id)s;"""
        resultado = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        return cls(resultado[0]) if resultado else None

    @classmethod
    def actualizar(cls, datos):
        query = """UPDATE tareas 
                   SET titulo=%(titulo)s, prioridad=%(prioridad)s, fecha_limite=%(fecha_limite)s, 
                       descripcion=%(descripcion)s, categoria_id=%(categoria_id)s 
                   WHERE id=%(id)s AND usuario_id=%(usuario_id)s;"""
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def marcar_completada(cls, datos):
        query = "UPDATE tareas SET estado='Completada' WHERE id=%(id)s AND usuario_id=%(usuario_id)s;"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def eliminar(cls, datos):
        query = "DELETE FROM tareas WHERE id=%(id)s AND usuario_id=%(usuario_id)s;"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @staticmethod
    def validar_tarea(tarea):
        es_valido = True
        if len(tarea['titulo'].strip()) < 3:
            flash("El título debe tener al menos 3 caracteres.", "tarea")
            es_valido = False
        if not tarea.get('categoria_id'):
            flash("Debe seleccionar una categoría.", "tarea")
            es_valido = False
        if not tarea.get('prioridad'):
            flash("Debe seleccionar una prioridad.", "tarea")
            es_valido = False
        if not tarea.get('fecha_limite'):
            flash("Debe ingresar una fecha límite.", "tarea")
            es_valido = False
        else:
            try:
                fecha_seleccionada = datetime.strptime(tarea['fecha_limite'], '%Y-%m-%d').date()
                if fecha_seleccionada < datetime.now().date():
                    flash("La fecha límite no puede ser pasada.", "tarea")
                    es_valido = False
            except ValueError:
                flash("Formato de fecha inválido.", "tarea")
                es_valido = False
        if len(tarea['descripcion'].strip()) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "tarea")
            es_valido = False
        return es_valido