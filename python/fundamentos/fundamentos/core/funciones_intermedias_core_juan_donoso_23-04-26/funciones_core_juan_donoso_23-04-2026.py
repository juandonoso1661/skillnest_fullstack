# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]

puntajes[1][0] = 600
print(puntajes[1][0])


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]

streamers[0]["nombre"] = "EliteGamerX"
print(streamers[0])


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}

eventos["Estados Unidos"][2] = "San francisco"
print(eventos)


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

ubicacion[0]["Latitud"] = 40.712776
print(ubicacion)

def iterar_diccionario(lista):
    def iterar_diccionario(lista):
     for diccionario in lista:
         salida = ", ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
         print(salida)
iterar_diccionario(streamers)


# Obtener valores de un diccionario creando la función obtener_valores(clave, lista)
def obtener_valores(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])
obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)


# Mostrar información de un diccionario con listas:
# Crea la función mostrar_informacion(diccionario)
def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
categorias = {
    "juegos_populares": ["Fortnite", "Minecraft", "Valorant", "GTA V"],
    "ciudades_eventos": ["Nueva York", "Madrid", "Tokio"]}
mostrar_informacion(categorias)