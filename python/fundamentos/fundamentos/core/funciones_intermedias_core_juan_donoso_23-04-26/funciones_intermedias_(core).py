# 1. Cambiar el puntaje de Pedro a 75
datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "María", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 75}
]

print(datos[2]["nombre"])
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def datos_carlos():
    for i in datos:
        print(f"{datos[0]['nombre']} obtuvo {datos[0]['puntaje']} puntos")
        break
datos_carlos()

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

def recibir_datos(nombre):
    ingresar = input("Ingrese el dato: ")
    for i in datos:
     if ingresar == i["nombre"]:
        print(f"{i['nombre']} obtuvo {i['puntaje']} puntos")
recibir_datos("nombre")