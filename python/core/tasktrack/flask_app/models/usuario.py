from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    BASE_DATOS = "tasktrack"

    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.contrasena = datos['contrasena']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

    @classmethod
    def guardar(cls, datos):
        query = """INSERT INTO usuarios (nombre, apellido, email, contrasena) 
                   VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s);"""
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)
        if not resultados or len(resultados) < 1:
            return False
        return cls(resultados[0])

    @staticmethod
    def validar_registro(usuario):
        es_valido = True
        if len(usuario['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        if len(usuario['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Dirección de correo electrónico inválida.", "registro")
            es_valido = False
        else:
            # Se usa query_db para verificar si el email ya existe
            if Usuario.obtener_por_email({'email': usuario['email']}):
                flash("Este correo ya está registrado.", "registro")
                es_valido = False
        if len(usuario['contrasena']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
        if usuario['contrasena'] != usuario['confirmar_contrasena']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False
        return es_valido