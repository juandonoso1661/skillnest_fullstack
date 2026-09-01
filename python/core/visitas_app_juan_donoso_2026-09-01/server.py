from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

# Clave secreta necesaria para utilizar sesiones
app.secret_key = "clave-secreta-visitas"


# Ruta principal
@app.route("/")
def index():

    # Comprobar si existe el contador de visitas
    if "visitas" in session:
        session["visitas"] += 1
    else:
        session["visitas"] = 1

    # Comprobar si existe el contador de reinicios
    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


# Agregar 2 visitas
@app.route("/agregar_dos")
def agregar_dos():

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += 2

    return redirect("/")


# Reiniciar contador
@app.route("/reiniciar")
def reiniciar():

    if "visitas" not in session:
        session["visitas"] = 0

    if "reinicios" not in session:
        session["reinicios"] = 0

    session["visitas"] = 0
    session["reinicios"] += 1

    return redirect("/")


# Agregar una cantidad ingresada por el usuario
@app.route("/agregar", methods=["POST"])
def agregar():

    if "visitas" not in session:
        session["visitas"] = 0

    numero = int(request.form["numero"])

    session["visitas"] += numero

    return redirect("/")


# Destruir completamente la sesión
@app.route("/destruir_sesion")
def destruir_sesion():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)