import os
import json


class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["codigo"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto
        self.guardar_en_archivo()
        print(f"Producto '{producto.nombre}' agregado exitosamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo in self.productos:
            if cantidad is not None:
                self.productos[codigo].cantidad = cantidad
            if precio is not None:
                self.productos[codigo].precio = precio
            self.guardar_en_archivo()
            print(f"Producto '{self.productos[codigo].nombre}' actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(
                    f"Código: {producto.codigo}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                json.dump([p.to_dict() for p in self.productos.values()], archivo)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            return
        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                data = json.load(archivo)
                self.productos = {p["codigo"]: Producto.from_dict(p) for p in data}
        except FileNotFoundError:
            print("El archivo de inventario no fue encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al leer el archivo. Puede estar corrupto.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")


# Interfaz de usuario simple en consola
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Mostrar Inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(codigo, nombre, cantidad, precio))
        elif opcion == "2":
            codigo = input("Código del producto a actualizar: ")
            cantidad = input("Nueva cantidad (presione Enter para omitir): ")
            precio = input("Nuevo precio (presione Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, cantidad, precio)
        elif opcion == "3":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente de nuevo.")
