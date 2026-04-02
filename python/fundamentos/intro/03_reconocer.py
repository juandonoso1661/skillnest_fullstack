"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #Importacion de libreria para procesos aleatorios


nombre = "Frida Kahlo" #Se crea una variable tipo string y se asigna valor
print(type(nombre)) #Type() = método de python para mostrar el tipo de una variable
print(len(nombre)) #Len() = Devuelve el largo de una variable.


edad = 25 #Creación de variable tipo númerico(int). 


if edad < 18: #Se establece condicion if.
   print("Eres menor de edad.") #Imprime un mensaje. 
elif edad == 18: #se establece subcondicion elif (else if).
   print("Tienes 18 años.") #Imprime un mensaje 
else: #Cierre de condicion (si no se cumplen condiciones anteriores)
   print("Eres mayor de edad.") #Imprime un mensaje


frutas = ["manzana", "pera", "fresa"] #creación de un array 
print(frutas[0]) #se elige la primera posicion del arreglo
frutas[0] = "banana" #A la posicion 0 de l arreglo se le asigna el valor "Banana"
frutas.append("uva") #Se le agrega "uva" al final del arreglo
frutas.remove("pera") #Se remueve la palabra "pera" del arreglo 


dimensiones = (200, 50) #Creación una variable tipo tupla (variable inmutable)
print(dimensiones[0]) #Imprime la posicion 0 de la variable creada


persona = { #Variable tipo object (object)
   "nombre": "Carlos", #Se establece un item "nombre" y se le asigna el valor
   "edad": 30 #Se crea un item "edad" y se loe asigna el valor 
}
print(persona["nombre"]) #Imprime el valor el item(ej: "Carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor
del persona["ciudad"] #Se elimina un item completo


for i in range(5): #for range: Se crea bucle en rango desde 0 a 5
   if i == 2: #Se establece  condicion if == 2
       continue #continue y ignora el proceso y continua 
   if i == 4: #Se establece condicion if == 4
       break #Si i = 4 se rompe el bucle
   print(i) #Imprime el valor de i en cada interación.(hasta 4)


contador = 0 #Se crea un variable contador tipo numerica(int)
while contador < 3: #Se crea bucle While con una condición
   print(f"while contador es: {contador}") #Imprime el contador en un mensaje concatenado con "f" string 
   contador += 1 #Incrementa el valor en 1 en cada iteración


def saludar_usuario(nombre): #def - Palabra reservada para crear una función
   return f"Hola, {nombre}" #devuelve un valor de la función


print(saludar_usuario("Francisca")) #Se imprime "Hola Francisca" - Return de la función