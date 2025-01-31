class Archivo:
    """
    Clase que representa un archivo y su manejo básico.
    Utiliza un constructor para inicializar y un destructor para cerrar el archivo.
    """

    def __init__(self, nombre_archivo, modo):
        """
        Constructor de la clase Archivo.
        Abre el archivo en el modo especificado y prepara el objeto para su uso.

        :param nombre_archivo: Nombre del archivo a manejar.
        :param modo: Modo en el que se abrirá el archivo (por ejemplo, 'r', 'w').
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        try:
            self.archivo = open(nombre_archivo, modo)
            print(f"Archivo '{nombre_archivo}' abierto en modo '{modo}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None

    def escribir(self, contenido):
        """
        Escribe contenido en el archivo si está abierto en modo escritura.

        :param contenido: Texto a escribir en el archivo.
        """
        if self.archivo and self.modo in ('w', 'a'):
            self.archivo.write(contenido + '\n')
            print("Contenido escrito en el archivo.")
        else:
            print("No se puede escribir en este archivo.")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se asegura de cerrar el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")

# Programa principal para demostrar el uso de la clase Archivo
if __name__ == "__main__":
    # Crear un objeto de la clase Archivo
    archivo = Archivo("ejemplo.txt", "w")

    # Escribir algo en el archivo
    archivo.escribir("Este es un ejemplo de uso de constructores y destructores en Python.")

    # El destructor se activará automáticamente cuando termine el programa o se elimine el objeto

