from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from app import app, bcrypt

from models.usuario import Usuario



# ==========================
# MOSTRAR LOGIN / REGISTRO
# ==========================

@app.route("/")
def index():

    return render_template("login.html")



# ==========================
# REGISTRO
# ==========================

@app.route("/registro", methods=["POST"])
def registro():

    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(
            request.form["password"]
        ).decode("utf-8")
    }


    # validar correo repetido

    usuario_existente = Usuario.buscar_por_email(
        data["email"]
    )

    if usuario_existente:

        flash(
            "El correo ya está registrado",
            "error"
        )

        return redirect(url_for("index"))



    Usuario.crear_usuario(data)


    flash(
        "Registro exitoso, ahora puedes iniciar sesión",
        "success"
    )


    return redirect(url_for("index"))




# ==========================
# LOGIN
# ==========================

@app.route("/login", methods=["POST"])
def login():


    usuario = Usuario.buscar_por_email(
        request.form["email"]
    )


    if not usuario:

        flash(
            "Usuario no encontrado",
            "error"
        )

        return redirect(url_for("index"))



    if not bcrypt.check_password_hash(
        usuario.password,
        request.form["password"]
    ):

        flash(
            "Contraseña incorrecta",
            "error"
        )

        return redirect(url_for("index"))



    session["id_usuario"] = usuario.id_usuario
    session["nombre"] = usuario.nombre



    return redirect(url_for("home"))




# ==========================
# HOME PROTEGIDO
# ==========================

@app.route("/home")
def home():

    if "id_usuario" not in session:

        return redirect(
            url_for("index")
        )


    return f"""
    <h1>
    Bienvenido {session["nombre"]}
    </h1>

    <p>
    Login correcto 🎉
    </p>

    <a href="/logout">
    Cerrar sesión
    </a>
    """




# ==========================
# LOGOUT
# ==========================

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Sesión cerrada correctamente",
        "success"
    )


    return redirect(url_for("index"))