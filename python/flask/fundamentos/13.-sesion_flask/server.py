from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# La clave secreta es OBLIGATORIA para usar session (encripta las cookies)
app.secret_key = "clave-secreta-skillnest"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # 1. Capturar los 3 datos del formulario
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    # 2. Guardar los 3 datos en la SESIÓN (Memoria temporal)
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    # 3. Redireccionar
    return redirect("/mostrar_usuario")

@app.route("/mostrar_usuario")
def mostrar_usuario():
    # Aquí la plantilla mostrar.html leerá directamente desde session
    return render_template("mostrar.html")

# ⭐ DESAFÍO ADICIONAL: Ruta /perfil
@app.route("/perfil")
def perfil():
    # Renderizamos la vista del perfil que leerá la información guardada en session
    return render_template("perfil.html")

if __name__ == "__main__":
    app.run(debug=True)