# I. Interacción y Condicionales (Básico)

#1. Números Pares Dinámicos
#Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
 ingresar = int(input("¿Cuantos numero desea ver?"))

 for i in range (1, ingresar+2):
    resultado = i*2
    print(resultado)

#2. Verificador de Edad y Acceso
#Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificarEdad():
 campo = input("Ingrese su año de nacimiento: ")
 edad = 2026 - int(campo)
 if campo == "":
  print("Error")


#3. Calculadora de Descuentos
#Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuento():
 cantidad = int(input("Ingrese la cantidad de productos: "))
 precio = float(input("Ingrese el precio del producto: "))

# Calcular subtotal
def aplicarDescuento():
 precio = float(input("Ingrese el precio solicitado del producto: "))
 cantidad = int(input("Ingrese la cantidad de productos que compró: "))
 producto = precio * cantidad

 if producto >= 100:
   descuento = producto * 0.15
 else:
   descuento = 0
   total = producto - descuento
   print(f"El subtotal es: ${producto}. el descuento aplicado es: ${descuento} y el total final es: ${total}")

#Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
def clasificadorNum():
   num = int(input("Ingrese un número"))
   if num > 0:
      if num % 2 == 0:
         print("Positivo-par")
      elif num % 2 == 1:
         print("Positivo-Impar")
      elif num < 0:
         if num % 2 == 0:
            print("Negativo-par")
         elif num % 2 == 1:
            print("Negativo-impar")
         else:
            print("Es 0")

    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#II. Iteraciones y Bucles (Intermedio)

#5. Tabla de Multiplicar Personalizada
#Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3.
def tablaMultiplicar():
   num = int(input("Ingresar Numero a trabajar: "))
   for i in range (1, 13):
      resultado = num * i
      if resultado % 3 == 0:
         print(f"Del {num} solo estos numeros son divisibles por 3 : {resultado}")

#6. Sumatoria con Centinela
#Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).

def sumaCentinela():
   suma_total = 0
   while True:
      n = (input("Ingresa un número: (negativo para salir)"))
      if n < 0:
         break
      suma_total += n
print(f"La suma total es: ")

#7. Contador de Vocales
#Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.

def contadorVocales():
   texto = input("Ingresa una palabra o frase:").lower()
   vocales = 0
   for i in range(len(texto)):
      #Repetir ls condicion con cada vocal
      if texto[i] == "a" or texto[i] == "e" or texto[i] == "o" or texto[i] == "u":
         vocales += 1
      #Mismo de arriba pero con las vovales con tilde
      elif texto[i] == "á" or texto[i] == "e" or texto[i] == "i" or texto[i] == "u":
         vocales += 1
      print(f"La cadena '{texto}' tiene {vocales} vocales en total")

#8. Validación de Contraseña
#Define una contraseña en una variable. Pide al usuario que la intente adivinar. Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
def validacion():
   con = 123456
   intentos = 0
   while True:
      ingresa = (input("ingresa la contraseña:"))
      if ingresa == con:
         print("acceso concedido")
         break
      else:
         intentos += 1
         if intentos > 3:
            print("Acceso denegado")
            break
         else:
            print(f"números de intentos: {intentos}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#III. Manejo de Arreglos / Listas (Avanzado)

#9. Registro de Nombres
#Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.

#10. Promedio de Notas
#Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.

#11. Filtro de Arreglos
#Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.

#12. Buscador de Elementos
#Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#IV. Retos de Lógica Combinada

#13. Simulación de Inventario
#Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].

#14. Generador de Lista de Compras
#Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente.

#15. Análisis de Temperaturas
#Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
#El promedio semanal.
#Cuántos días la temperatura fue superior a 25 grados.
#El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).
continuar = True 

while continuar:
    print("\n---Ejercicios Python---")
    print("---1.-Ejercicio 1 ---")
    print("---2.-Ejercicio 2---")
    print("---3.-Ejercicio 3---")
    print("---4.-Ejercicio 4---")
    print("---5.-Ejercicio 5---")
    print("---6.-Ejercicio 6---")
    print("---7.-Ejercicio 7---")
    print("---8.-Ejercicio 8---")
    print("---9.-Ejercicio 9---")
    print("---10.-Ejercicio 10---")
    print("---11.-Ejercicio 11---")
    print("---12.-Ejercicio 12---")
    print("---13.-Ejercicio 13---")
    print("---14.-Ejercicio 14---")
    print("---15.-Ejercicio 15---")
    opcion = input("\n---Elige una opción: (1-15) (0 para salir) = ")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2:")
        print(verificarEdad())
    elif opcion == "3":
       print("n\Ejecutando ejercicio 3:")
       print(aplicarDescuento())
    elif opcion == "4":
       print("n\Ejecutando ejercicio 4:")
       print(clasificadorNum())
    elif opcion == "5":
       print("n\Ejecutando ejercicio 5:")
       print(tablaMultiplicar())
    elif opcion == "6":
       print("n\Ejecutando ejercicio 6:")
       print(sumaCentinela())
    elif opcion == "7":
       print("n\Ejecutando ejercicio 7:")
       print(contadorVocales())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opcion no valida,intenta otra vez")