class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def actualizar_año(self, nuevo_año):
        self.año = nuevo_año
        print(f"El año del coche se ha actualizado a {self.año}")


# Ejemplo de uso
coche1 = Coche("Toyota", "Corolla", 2020)
print(coche1.descripcion())
coche1.actualizar_año(2023)
print(coche1.descripcion())
