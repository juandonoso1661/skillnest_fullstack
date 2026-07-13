from flask import Flask

app = Flask(__name__) 

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "Bienvenido al server de flask"

# Ruta genérica para explorar enrutamiento
@app.route("/hola")
def hola():
    return "Hola,esta es otra ruta"
 
# Rutas dinámicas para personalización
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"

# Ruta que repite un mensaje varias veces
@app.route("/repetir/<mensaje>/<int:veces>")
def mensaje(mensaje, veces):
    return (mensaje + " ") * veces
 
# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente 
@app.errorhandler(404)
def pagina_no_encontrada():
    return "Error 404,pagina no encontrada.", 404

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)
