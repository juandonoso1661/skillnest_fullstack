from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

password = "123456"

hash_password = bcrypt.generate_password_hash(password).decode("utf-8")

print("Contraseña:", password)
print("Hash:", hash_password)

print(
    "¿Coincide?",
    bcrypt.check_password_hash(hash_password, password)
)