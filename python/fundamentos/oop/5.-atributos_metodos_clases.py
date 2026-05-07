## Atributos,métodos de clase,métodos estáticos
#DEFINICION DE LA CLASE
class Estudiantes:
    ## Función de repaso
    colegio = "liceo vate vicente huidobro"

    ##Lista en donde esten todos los estudiantes
    estudiantes = []

    ##Método constructor
    def __init__(self,nombre,nota):

        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota

        #Agregar elmentos a lista Estudiante (objeto)
        Estudiantes.estudiantes.append(self)

    #Métodos de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    #Método de clase
    #Usa "CLS" por que trabaja con la información de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre

    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)
    
    #Método estático
    #Este no usa cls ni self, solo parámetros.
    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False

#Creacion de Objetos (Instancias)
e1 = Estudiantes("Donovan" , 4.0)
e2 = Estudiantes("Randy", 6.7)

#Uso de métodos de instancia 
print("== MÉTODO DE INSTANCIA ==")

#Mostrar datos de estudiantes
e1.mostrar_info()
print()
e2.mostrar_info
print()





## Crear una función que valide usuario y contraseña 

def validador(usuario,password):
    if usuario == "matias123" and password == "matias123":
        print(f"Bienvenido, {usuario}!")
        return True
    else:
        print("Acceso denegado")
    return False

def enviarDatos():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    validador(username, password)

enviarDatos()