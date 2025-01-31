# Definición de la clase base
class Animal:
    # Atributo encapsulado
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.edad = edad

    # Método para obtener el nombre (encapsulación)
    def get_nombre(self):
        return self.__nombre

    # Método para hacer un sonido
    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza

    # Sobreescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Guau!")

# Definición de otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobreescritura del método hacer_sonido (Polimorfismo)
    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Miau!")

# Creación de instancias de las clases
perro = Perro("Rex", 5, "Pastor Alemán")
gato = Gato("Felix", 3, "Negro")

# Demostración de Polimorfismo
def hacer_sonidos(animal):
    animal.hacer_sonido()

hacer_sonidos(perro)  # El perro hace su sonido
hacer_sonidos(gato)   # El gato hace su sonido
