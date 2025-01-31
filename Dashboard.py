import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD_1/SEMANA2/Ejercicio_clase_carro.py',
        '2': 'UNIDAD_1/SEMANA2/Ejercicio_herencia_polimorfismo_clases.py',
        '3': 'UNIDAD_1/SEMANA3/Ejemplo_programacion_orientada_a_objetos.py',
        '4': 'UNIDAD_1/SEMANA3/Ejemplo_programacion_tradicional_temperaturas.py',
        '5': 'UNIDAD_1/SEMANA4/Sistema_de_reservas_de_hotel.py',
        '6': 'UNIDAD_1/SEMANA5/Area_de_una_figura.py',
        '7': 'UNIDAD_1/SEMANA6/Aplicacion_de_conceptos_POO.py',
        '8': 'UNIDAD_1/SEMANA7/Constructores_y_destructores.py',
        '9': 'UNIDAD_1/SEMANA7/ejemplo.txt',
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()