# Clase para representar la información diaria del clima
class Clima:
    def __init__(self, temperatura):
        self.__temperatura = temperatura  # Atributo privado de temperatura

    # Método para obtener la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Método para mostrar la temperatura
    def mostrar_temperatura(self):
        print(f"Temperatura del día: {self.__temperatura} °C")


# Clase para representar la semana de clima, que usa la clase Clima
class SemanaClima:
    def __init__(self):
        self.dias_clima = []  # Lista para almacenar los objetos Clima

    # Método para ingresar temperaturas predefinidas para cada día
    def ingresar_temperaturas(self):
        # Datos predefinidos de temperaturas para 7 días de la semana
        temperaturas = [26.5, 28.0, 30.0, 32.0, 29.5, 28.0, 30.5]

        # Crear los objetos Clima para cada día y agregarlos a la lista
        for temp in temperaturas:
            clima_dia = Clima(temp)  # Crear un objeto de tipo Clima
            self.dias_clima.append(clima_dia)  # Agregarlo a la lista

    # Método para calcular el promedio semanal de temperaturas
    def calcular_promedio(self):
        total_temperaturas = sum([clima.obtener_temperatura() for clima in self.dias_clima])
        promedio = total_temperaturas / len(self.dias_clima)
        return promedio

    # Método para mostrar todas las temperaturas ingresadas
    def mostrar_temperaturas(self):
        for i, clima in enumerate(self.dias_clima):
            print(f"Día {i + 1}: ", end="")
            clima.mostrar_temperatura()

    # Método para mostrar el promedio semanal
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")


# Función principal que organiza el flujo del programa
def main():
    semana_clima = SemanaClima()  # Crear un objeto de tipo SemanaClima
    semana_clima.ingresar_temperaturas()  # Llamar a la función para ingresar las temperaturas
    semana_clima.mostrar_temperaturas()  # Mostrar todas las temperaturas
    semana_clima.mostrar_promedio()  # Mostrar el promedio semanal


# Ejecutamos el programa
if __name__ == "__main__":
    main()
