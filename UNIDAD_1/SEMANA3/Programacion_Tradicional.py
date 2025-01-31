# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
