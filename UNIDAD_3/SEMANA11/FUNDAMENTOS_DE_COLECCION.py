import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self, archivo_datos="inventario.json"):
        self.productos = {}
        self.archivo_datos = archivo_datos
        self.cargar_datos()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_datos()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_datos()
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_datos()
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_datos(self):
        with open(self.archivo_datos, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                for d in datos:
                    self.productos[d["id"]] = Producto(d["id"], d["nombre"], d["cantidad"], d["precio"])
        except FileNotFoundError:
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            print(resultados if resultados else "Producto no encontrado.")
        elif opcion == "5":
            print(inventario.mostrar_productos())
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()