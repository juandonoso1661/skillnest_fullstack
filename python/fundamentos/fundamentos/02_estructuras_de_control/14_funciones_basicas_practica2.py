import os
# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i * 2)
        return[result]

result1 = multiplica_por_2(5)
print(result1)

# Debe retornar: [0, 2, 4, 6, 8, 10]


# Analiza publicaciones
def suma_y_resta(lista):
 suma = lista[0] + list[1]
 resta = lista[0] - lista[1]
 print(f"suma : {suma}")
 return resta

def ejercicio_2():
  resultado = suma_y_resta([120, 115])
# Imprime: 235 y retorna: 5


# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
   total = sum(sumatoria)
   longitud = len(sumatoria)
   resultado = total - longitud
   print(f"Total = {total}, longitud = {longitud}")
   return resultado

def ejercicio(retornar):
   sumatoria_menos_longitud([10, 5, 3, 7])
   print(f"El resultado del retorno es: {retornar}")
# Suma total = 25, longitud = 4, debe retornar: 21


# Ajusta visualizaciones
def valores_multiplicados_segundo(lista):
    print(len(lista))
    if len(lista) < 2:
      return sum(lista) - len(lista)

    valores_multiplicados_segundo([100, 3, 50, 20])
# Imprime: 4 y retorna: [300, 9, 150, 60]

valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


# Genera precio fijo
def valor_multiplicado_longitud(lista):
   print(len(lista))
   if len(lista) < 2:
        return []
   return [x * lista[1] for x in lista]

valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]

def limpiar_consola():
   os.system('cls')


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
        limpiar_consola()
        print("\nEjecutando ejercicio 1:")
        multiplica_por_2()
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