from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# REGISTRAR EL PRODUCTO
@app.route("/registrar", methods=["POST"])
def registrar():

    #DATOS
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    #MOSTRAR LOS DATOS
    print("====================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoria: {categoria}")
    print("====================")

    #REDIRECCIONAR EL RESULTADO
    return redirect("/resultado")

#RESULTADO
@app.route("/resultado")
def resultado():
    return render_template("resultado.html")

#AYUDA
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)