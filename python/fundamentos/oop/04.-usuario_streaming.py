#Define la clase UsuarioStreaming, que debe incluir:

#Atributos:
#nombre
#email
#suscripcion (Gratis, Estándar o Premium)
#lista_reproduccion (lista de títulos agregados por el usuario).
#Métodos:
#agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
#ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
#cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
#mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
#🧪 Realizar las siguientes pruebas con instancias:

#Crea 3 usuarios de la plataforma de streaming.
#Haz que el primer usuario agregue dos títulos a su lista y los vea.
#Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
#Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.

class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       """Agrega un contenido a la lista de reproducción del usuario."""
       self.lista_reproduccion.append(titulo)
       print(f"{titulo} se a agregado a tu lista")
       


   def ver_contenido(self, titulo):
       """Simula que el usuario reproduce un contenido."""
       if titulo in self.lista_reproduccion:
           print(f"El usuario {self.nombre} esta viendo '{titulo}'")
       else:
           print(f"Titulo no encontrado {titulo}")


   def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       susAntigua = self.suscripcion
       self.suscripcion = nueva_suscripcion
       print(f"Suscripción cambió de {susAntigua} a {nueva_suscripcion}")


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripción: {self.suscripcion}")

       if len(self.lista_reproduccion) == 0:
           print("La lista de producción está vacía.")
       else:
           print("Lista de produccion: ")
           for titulo in self.lista_reproduccion:
               print("-", titulo)

usuarios = []

for i in range(3):
    print(f"\nRegistro del usuario {i+1}")

    nombre = input("Ingrese nombre: ")
    email = input("Ingrese su email: ")
    suscripcion = input("Ingrese su tipo de suscripcion: ")

    usuario = UsuarioStreaming(nombre, email, suscripcion)
    usuarios.append(usuario)

#Todos los valores que se deban registrar debe ser con input
#Añadir un menu while para llamar amlos metodos. 
# (Menú de selección)

while True:

    print("\n====== MENÚ STREAMING ======")
    print("1. Agregar contenido")
    print("2. Ver contenido")
    print("3. Cambiar suscripción")
    print("4. Mostrar información")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Saliendo del programa...")
        break

    numero_usuario = int(input("Seleccione usuario (1-3): ")) - 1

    if numero_usuario < 0 or numero_usuario >= len(usuarios):
        print("Usuario inválido.")
        continue

    usuario = usuarios[numero_usuario]

    if opcion == "1":
        titulo = input("Ingrese título: ")
        usuario.agregar_a_lista(titulo)

    elif opcion == "2":
        titulo = input("Ingrese título a reproducir: ")
        usuario.ver_contenido(titulo)

    elif opcion == "3":
        nueva = input("Nueva suscripción: ")
        usuario.cambiar_suscripcion(nueva)

    elif opcion == "4":
        usuario.mostrar_info_usuario()

    else:
        print("Opción inválida.")