from flask import Flask, render_template
from usuario import Usuario

app = Flask(__name__)


@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()

    return render_template(
        "usuarios.html",
        usuarios=todos_los_usuarios
    )


if __name__ == "__main__":
    app.run(debug=True)