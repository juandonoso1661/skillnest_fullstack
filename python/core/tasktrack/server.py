from flask_app import app
# Importamos los controladores que estarán dentro de flask_app/controllers/
from flask_app.controllers import usuarios, tareas, categorias

if __name__ == "__main__":
    app.run(debug=True)