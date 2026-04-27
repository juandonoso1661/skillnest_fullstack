#Pasar argumentos 
#Para poder personalizar nuestras instancia 
# vamos a pasar algunos argumentos al método __init__ 
# y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

#Creacion de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
juan = Usuario("Juan", "Donoso", "juanDonoso@gmail.com", 4000, 200)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#--------------------------------
#----Tarea rápida
'''
Crear una clase estudiante, y asignarle los siguientes atributos:
(Rut,nombre,apellido,especialidad,fecha_nac)
-Crear 3 insancias para la clase con distintos estudiantes.
-Imprimir el nombre y apellido concatenado + escialidad.
'''
