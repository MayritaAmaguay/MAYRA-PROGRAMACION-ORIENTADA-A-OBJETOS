class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

def mostrar_sonido(animal):
    print(f"{animal.nombre} hace el sonido: {animal.hacer_sonido()}")

# Ejemplo de uso
perro = Perro("Rex")
gato = Gato("Luna")
mostrar_sonido(perro)
mostrar_sonido(gato)
