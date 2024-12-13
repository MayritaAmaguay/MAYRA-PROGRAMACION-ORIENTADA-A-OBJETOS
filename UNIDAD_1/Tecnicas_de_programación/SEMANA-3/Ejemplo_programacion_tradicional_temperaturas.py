# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Lista con las temperaturas predefinidas para los 7 días de la semana
    temperaturas = [26.5, 28.0, 30.0, 32.0, 29.5, 28.0, 30.5]
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    # Calcula el promedio de las temperaturas
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Función principal que organiza el flujo del programa
def main():
    temperaturas = ingresar_temperaturas()  # Llama a la función para obtener las temperaturas
    promedio = calcular_promedio(temperaturas)  # Llama a la función para calcular el promedio
    print(f"Las temperaturas de la semana son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")  # Muestra el promedio

# Ejecutamos el programa
if __name__ == "__main__":
    main()
