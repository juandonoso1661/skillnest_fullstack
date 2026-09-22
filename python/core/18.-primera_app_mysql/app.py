from flask import Flask, render_template, request, redirect

from mascota import Mascota


app = Flask(__name__)


@app.route("/")
def index():

    mascotas = Mascota.get_all()

    print(mascotas)

    return render_template(
        "index.html",
        todas_mascotas=mascotas
    )

@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():

    datos = {
        "nombre" : request.form["nombre"],
        "tipo" : request.form["tipo"],
        "color" : request.form["color"]
    }

    Mascota.save(datos)
    return redirect("/")

@app.route("/mascotas/<int:id>")
def get_mascota(id):

    mascota = Mascota.get_by_id(id)

    if mascota is None:
        return "Mascota no encontrada", 404
    
    return render_template(
        "mascota.html", 
        mascota=mascota
    )

if __name__ == "__main__":

    app.run(debug=True)