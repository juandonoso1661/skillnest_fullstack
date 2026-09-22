from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)


# Listado de usuarios
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)


# Mostrar formulario
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


# Crear usuario mediante POST
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(data)
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)