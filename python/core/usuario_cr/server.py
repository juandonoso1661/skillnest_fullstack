from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)


# Redirección de la raíz al listado
@app.route("/")
def index():
    return redirect(url_for("usuarios"))


# Listado de usuarios
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)


# Mostrar formulario de creación
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


# Mostrar un usuario por ID
@app.route("/usuarios/<int:id>")
def mostrar_usuario(id):
    usuario_encontrado = Usuario.get_by_id({"id": id})
    return render_template("usuario.html", usuario=usuario_encontrado)


# Mostrar formulario para editar
@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario_encontrado = Usuario.get_by_id({"id": id})
    return render_template("editar_usuario.html", usuario=usuario_encontrado)


# Actualizar usuario mediante POST
@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar_usuario(id):
    data = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update(data)
    return redirect(url_for("usuarios"))


# Borrar usuario mediante POST
@app.route("/usuarios/borrar/<int:id>", methods=["GET", "POST"])
def borrar_usuario(id):
    Usuario.delete({"id": id})
    return redirect(url_for("usuarios"))



if __name__ == "__main__":
    app.run(debug=True)