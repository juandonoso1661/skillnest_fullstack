from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

import os
import re

from usuario import Usuario


load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

bcrypt = Bcrypt(app)


# -----------------------------------
# VALIDACIONES
# -----------------------------------

def validar_nombre(nombre):
    return bool(
        nombre
        and len(nombre) >= 2
        and nombre.isalpha()
    )


def validar_email(email):
    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(patron, email))


def validar_password(password):

    if not password or len(password) < 8:
        return False

    # Bonus plata: al menos una mayúscula
    if not re.search(r"[A-Z]", password):
        return False

    # Bonus plata: al menos un número
    if not re.search(r"\d", password):
        return False

    return True


# -----------------------------------
# PÁGINA PRINCIPAL
# -----------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------------
# REGISTRO
# -----------------------------------

@app.route("/register", methods=["POST"])
def register():

    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    errores = []

    # Validar nombre
    if not validar_nombre(nombre):
        errores.append(
            "El nombre debe contener solo letras y tener al menos 2 caracteres."
        )

    # Validar apellido
    if not validar_nombre(apellido):
        errores.append(
            "El apellido debe contener solo letras y tener al menos 2 caracteres."
        )

    # Validar email
    if not validar_email(email):
        errores.append(
            "El correo electrónico no tiene un formato válido."
        )

    # Revisar si el email ya existe
    if validar_email(email):

        usuario_existente = Usuario.get_by_email(email)

        if usuario_existente:
            errores.append(
                "El correo electrónico ya está registrado."
            )

    # Validar contraseña
    if not validar_password(password):
        errores.append(
            "La contraseña debe tener al menos 8 caracteres, "
            "una mayúscula y un número."
        )

    # Confirmar contraseña
    if password != confirm_password:
        errores.append(
            "Las contraseñas no coinciden."
        )

    # Si existen errores
    if errores:

        return render_template(
            "index.html",
            errores_registro=errores,
            registro={
                "nombre": nombre,
                "apellido": apellido,
                "email": email
            }
        )

    # -----------------------------------
    # HASHEAR CONTRASEÑA
    # -----------------------------------

    password_hash = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    # -----------------------------------
    # DATOS PARA GUARDAR
    # -----------------------------------

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contrasena": password_hash
    }

    usuario_id = Usuario.save(data)

    # -----------------------------------
    # ERROR AL GUARDAR
    # -----------------------------------

    if not usuario_id:

        return render_template(
            "index.html",
            errores_registro=[
                "Ocurrió un error al registrar el usuario."
            ],
            registro={
                "nombre": nombre,
                "apellido": apellido,
                "email": email
            }
        )

    # -----------------------------------
    # GUARDAR ID EN SESIÓN
    # -----------------------------------

    session["usuario_id"] = usuario_id

    return redirect(url_for("success"))


# -----------------------------------
# INICIO DE SESIÓN
# -----------------------------------

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    errores_login = []

    usuario = Usuario.get_by_email(email)

    # Verificar usuario
    if not usuario:

        errores_login.append(
            "El correo electrónico o la contraseña son incorrectos."
        )

    # Verificar contraseña
    elif not bcrypt.check_password_hash(
        usuario.password,
        password
    ):

        errores_login.append(
            "El correo electrónico o la contraseña son incorrectos."
        )

    # Si hay errores
    if errores_login:

        return render_template(
            "index.html",
            errores_login=errores_login
        )

    # Crear sesión
    session["usuario_id"] = usuario.id

    return redirect(url_for("success"))


# -----------------------------------
# PÁGINA DE ÉXITO
# -----------------------------------

@app.route("/success")
def success():

    # Comprobar sesión
    if "usuario_id" not in session:
        return redirect(url_for("index"))

    usuario = Usuario.get_by_id(
        session["usuario_id"]
    )

    # Si el usuario no existe
    if not usuario:

        session.clear()

        return redirect(url_for("index"))

    return render_template(
        "success.html",
        usuario=usuario
    )


# -----------------------------------
# CERRAR SESIÓN
# -----------------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


# -----------------------------------
# EJECUTAR
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)