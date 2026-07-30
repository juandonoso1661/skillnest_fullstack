from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
   {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "icono":"spotify.png"},
   {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "icono":"netflix.png"},
   {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "icono":"youtube.png"},
   {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "icono":"twich.png"},
   {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "icono":"tiktok.png"},
   {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "icono":"instagram.png"},
   {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "icono":"discord.png"},
]

# Ruta para mostrar la tabla con datos
@app.route("/")
def tablas_plataformas():
   return render_template("tablas.html", plataformas=datos)

if __name__ == "__main__":
   app.run(debug=True)