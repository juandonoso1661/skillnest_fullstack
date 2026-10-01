from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)


app.secret_key = os.getenv(
    "SECRET_KEY"
)


bcrypt = Bcrypt(app)



import controllers.usuarios_controller



if __name__ == "__main__":

    app.run(debug=True)