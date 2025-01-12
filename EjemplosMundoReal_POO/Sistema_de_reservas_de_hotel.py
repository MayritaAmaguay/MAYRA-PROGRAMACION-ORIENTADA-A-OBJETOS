# hotelMAYRAAMAGUAY.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def liberar(self):
        if self.reservada:
            self.reservada = False
            print(f"Habitación {self.numero} liberada.")
        else:
            print(f"Habitación {self.numero} no estaba reservada.")

class Hotel:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            estado = "Reservada" if habitacion.reservada else "Disponible"
            print(f"Habitación {habitacion.numero} - Tipo: {habitacion.tipo} - Precio: {habitacion.precio} - Estado: {estado}")

# Creando un hotel
hotel = Hotel("Hotel Paraíso", "Avenida Principal 123")

# Agregando habitaciones
habitacion1 = Habitacion(101, "Individual", 100)
habitacion2 = Habitacion(102, "Doble", 150)
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Mostrando habitaciones disponibles
hotel.mostrar_habitaciones()

# Reservando una habitación
habitacion1.reservar()

# Mostrando habitaciones después de la reserva
hotel.mostrar_habitaciones()
