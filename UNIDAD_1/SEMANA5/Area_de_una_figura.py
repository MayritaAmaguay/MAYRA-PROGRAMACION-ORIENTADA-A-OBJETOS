"""
Calculadora de Áreas de Figuras Geométricas
-------------------------------------------
Este programa permite al usuario calcular el área de diferentes figuras geométricas:
círculo, cuadrado y triángulo. Solicita al usuario ingresar los datos necesarios
para la figura seleccionada y muestra el resultado del cálculo.

El programa utiliza funciones específicas para cada tipo de cálculo y maneja errores
como valores negativos o entradas no válidas.
"""

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (debe ser un número positivo).
    :return: Área del círculo o un mensaje de error si el radio no es válido.
    """
    if radio <= 0:
        return "El radio debe ser un número positivo."  # Validación de entrada
    return math.pi * radio ** 2  # Fórmula: π * radio^2


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el tamaño de su lado.
    :param lado: Longitud del lado del cuadrado (debe ser un número positivo).
    :return: Área del cuadrado o un mensaje de error si el lado no es válido.
    """
    if lado <= 0:
        return "El lado debe ser un número positivo."  # Validación de entrada
    return lado ** 2  # Fórmula: lado^2


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (debe ser un número positivo).
    :param altura: Altura del triángulo (debe ser un número positivo).
    :return: Área del triángulo o un mensaje de error si los valores no son válidos.
    """
    if base <= 0 or altura <= 0:
        return "La base y la altura deben ser números positivos."  # Validación de entrada
    return (base * altura) / 2  # Fórmula: (base * altura) / 2


def obtener_tipo_figura():
    """
    Solicita al usuario que ingrese el tipo de figura geométrica deseada.
    :return: El nombre de la figura ingresado por el usuario en minúsculas.
    """
    tipo_figura = input("Ingrese el tipo de figura (círculo, cuadrado, triángulo): ").lower()
    return tipo_figura  # Retorna la figura en minúsculas para evitar errores de formato


def main():
    """
    Función principal que gestiona la interacción con el usuario.
    Solicita el tipo de figura, obtiene los datos requeridos, y calcula el área.
    """
    print("Bienvenido a la calculadora de áreas.")  # Mensaje de bienvenida

    tipo_figura = obtener_tipo_figura()  # Solicita el tipo de figura al usuario

    # Verifica el tipo de figura y realiza el cálculo correspondiente
    if tipo_figura == "círculo":
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)

    elif tipo_figura == "cuadrado":
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)

    elif tipo_figura == "triángulo":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)

    else:
        # Mensaje de error si el usuario ingresa un tipo de figura no válido
        area = "Figura no válida."

    # Muestra el resultado del cálculo o el mensaje de error
    print(f"El área de la figura es: {area}")


# Ejecuta el programa si se ejecuta directamente este archivo
if __name__ == "__main__":
    main()
