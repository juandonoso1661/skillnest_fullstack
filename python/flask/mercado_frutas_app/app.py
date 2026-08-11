from flask import Flask, render_template, request

app = Flask(__name__)


# ==========================================
# Lista de frutas
# ==========================================

frutas = [
    {
        "nombre": "Manzana",
        "precio": 1500,
        "imagen": "manzana.png",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },
    {
        "nombre": "Plátano",
        "precio": 1800,
        "imagen": "platano.png",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },
    {
        "nombre": "Naranja",
        "precio": 3000,
        "imagen": "naranja.png",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },
    {
        "nombre": "Fresa",
        "precio": 4500,
        "imagen": "fresa.png",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },
    {
        "nombre": "Uva",
        "precio": 3800,
        "imagen": "uva.png",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },
    {
        "nombre": "Piña",
        "precio": 5000,
        "imagen": "pina.png",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },
    {
        "nombre": "Sandía",
        "precio": 4200,
        "imagen": "sandia.png",
        "descripcion": "Fruta refrescante, ideal para el verano."
    },
    {
        "nombre": "Mango",
        "precio": 3500,
        "imagen": "mango.png",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }
]


# ==========================================
# Página principal
# ==========================================

@app.route("/")
def index():
    return render_template("index.html", frutas=frutas)


# ==========================================
# Catálogo de frutas
# ==========================================

@app.route("/frutas")
def catalogo():
    return render_template("frutas.html", frutas=frutas)


# ==========================================
# Procesar compra
# ==========================================

@app.route("/checkout", methods=["POST"])
def checkout():

    # Datos del cliente
    nombre = request.form["nombre"]
    email = request.form["email"]
    direccion = request.form["direccion"]

    # Variables para calcular la compra
    pedido = []
    total = 0
    total_frutas = 0

    # Recorrer las frutas
    for fruta in frutas:

        cantidad = int(request.form[fruta["nombre"]])

        if cantidad > 0:

            subtotal = cantidad * fruta["precio"]

            pedido.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": fruta["imagen"]
            })

            total += subtotal
            total_frutas += cantidad

    # Mostrar resumen
    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        pedido=pedido,
        total=total,
        total_frutas=total_frutas
    )


# ==========================================
# Ejecutar aplicación
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)