#1.-Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def listaNum(listado):
    menor = min(listado)
    mayor = max(listado)


def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit}: "))
        listNum.append(num)
        i += 1
    listaNum(listaNum)

#2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiuoAEIOU"
    return letra in vocales #Devuelve True si la letra está dentro de las vocales, si
   
def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")

def ejercicio_contar_vocales():
    texto = input("Ingrese el texto: ")

#3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
            return resultado
def mostrar():
    nombres = []
    cantidad = int(input("¿Cuantos nombres desea ingresar?"))

    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        print(f"{nombre} agregado con exito a la lista.")
        nombres.append(nombre)

        listaNombres = filtrar(nombres)
        print(f"Los nombres con más de 5 letras son: \n- {("\n- ").join(listaNombres)}")

#4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def listaNotas(nota):
    lista = 0
    for i in range(len(nota)):
        lista += nota[i]
        promedio = lista / (len(nota))

        if promedio >= 4.0 and promedio <= 7.0:
            return f"El estudiante aprueba con {promedio}"
        elif promedio >= 1.0 and promedio <= 3.9:
            return f"El estudiante no aprueba con {promedio}"
        else:
            return"Error"

def ejercicio4():
    largo = int(input("Cuantas notas va a ingresar: "))
    nota = []
    for i in range(largo):
        inp = float(input(f"Ingrese nota {i + 1}: "))
        if inp != "":
            nota.append(inp)
            print(listaNotas(nota))

            ejercicio4()
#5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * 0.1
    precioFinal = precioInicial - descuento
    print(f"El precio inicial del producto es \n{precioInicial} \ny con decuento \n{precioFinal}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quieran:\n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor del producto: \n"))
        listaPrecios.append(valorProducto)
        descuento(listaPrecios)
        valores()
#6.-Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    elif numero % 3 == 0:
        print(f"El numero {numero} es impar")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingrese un número: "))
    parImpar(num)
recibirNum()
#7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num += 1
            return num
def personas():
    edad = []
    inp = int(input("Cuantas personas vas a ingresar vas a ingresar hoy?"))
    for i in range(inp):
        var = int(input(">>"))
        if var != "":
            edad.append(var)
        else:
            print("Por favor ingresar valor valido")
        resultado = edades(edad)
        print(f"Hay {resultado} personas mayores edad")
personas()
#8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def vecesAparece(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesAparece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesAparece += 1
    print(f"La palabra {buscar} aparece {vecesAparece} ne la lista")

def recibirPalabras():
    cantidad = int(input("Ingrese la cantidad de palabras:  "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}.  ")
        listaPalabras.append(palabra)
        vecesAparece(listaPalabras)
#9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
#10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.




continuar = True 

while continuar:
    print("\n---Ejercicios Python---")
    print("---1.-Ejercicio 1 ---")
    print("---2.-Ejercicio 2---")
    print("---3.-Ejercicio 3---")
    print("---4.-Ejercicio 4---")
    print("---5.-Ejercicio 5---")
    opcion = input("\n---Elige una opción: (1-5) (0 para salir) = ")
    if opcion == "1":
        
        print("\nEjecutando ejercicio 1:")
        
    elif opcion == "2":
        print("\nEjecutando ejercicio 2:")
        
    elif opcion == "3":
       print("n\Ejecutando ejercicio 3:")
       
    elif opcion == "4":
       print("n\Ejecutando ejercicio 4:")
       
    elif opcion == "5":
       print("n\Ejecutando ejercicio 5:")
       
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida,intenta otra vez")