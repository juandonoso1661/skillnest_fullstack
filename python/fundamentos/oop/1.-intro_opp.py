#Creacion de la clase usuario - Entidad
class Usuario:
    def __init__(self): #constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase 
miyagi = Usuario()
daniel = Usuario()
juan = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Nariyoshi
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre) #Imprime: Daniel

#Valores nueva instancia
juan.nombre = "Juan"
juan.apellido = "Donoso"
juan.email = "juandonoso@gmail.com"
juan.limite_credito = 300
juan.saldo_pagar = 100

#imprimir nombre
print(juan.nombre)
print(daniel.nombre)
print(daniel.nombre)

