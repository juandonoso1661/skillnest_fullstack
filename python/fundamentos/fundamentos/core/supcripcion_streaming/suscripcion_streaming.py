class SuscripcionStreaming:

    costos_suscripcion = {
        "Gratis": 0,
        "Estándar": 5.99,
        "Premium": 10.99
    }

    def __init__(self, usuario, tipo_suscripcion="Gratis"):

        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""

        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"{self.usuario} realizó un pago de ${monto}")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción."""

        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = self.costos_suscripcion[nuevo_tipo]

        print(f"{self.usuario} cambió a {nuevo_tipo}")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo."""

        if self.tipo_suscripcion == "Gratis":
            print("No tiene acceso a contenido exclusivo")

        else:
            print("Puede ver contenido exclusivo")

    def mostrar_info_suscripcion(self):
        """Muestra información del usuario."""

        print("\n------ INFORMACIÓN ------")
        print("Usuario:", self.usuario)
        print("Suscripción:", self.tipo_suscripcion)
        print("Costo mensual:", self.costo_mensual)
        print("Saldo pendiente:", self.saldo_pendiente)


#REGISTRO DE LOS USUARIOS

usuarios = []

for i in range(3):

    print(f"\nRegistro usuario {i+1}")

    nombre = input("Ingrese nombre: ")

    tipo = input("Ingrese tipo de suscripción (Gratis, Estándar, Premium): ")

    usuario = SuscripcionStreaming(nombre, tipo)

    usuarios.append(usuario)


#MENU WHILE

while True:

    print("\n====== MENÚ STREAMING ======")
    print("1. Ver contenido exclusivo")
    print("2. Cambiar suscripción")
    print("3. Realizar pago")
    print("4. Mostrar información")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break

    numero_usuario = int(input("Seleccione usuario (1-3): ")) - 1

    if numero_usuario < 0 or numero_usuario >= len(usuarios):
        print("Usuario inválido")
        continue

    usuario = usuarios[numero_usuario]

    if opcion == "1":

        usuario.ver_contenido_exclusivo()

    elif opcion == "2":

        nueva = input("Nueva suscripción: ")

        usuario.cambiar_suscripcion(nueva)

    elif opcion == "3":

        monto = float(input("Ingrese monto a pagar: "))

        usuario.realizar_pago(monto)

    elif opcion == "4":

        usuario.mostrar_info_suscripcion()

    else:
        print("Opción inválida")