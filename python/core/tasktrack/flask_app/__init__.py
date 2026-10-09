import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave_secreta_default")

bcrypt = Bcrypt(app)