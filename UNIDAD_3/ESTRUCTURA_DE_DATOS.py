class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    # Getters y setters
    def get_producto_id(self):
        return self.producto_id

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for prod in self.productos:
            if prod.get_producto_id() == producto.get_producto_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    def eliminar_producto(self, producto_id):
        for prod in self.productos:
            if prod.get_producto_id() == producto_id:
                self.productos.remove(prod)
                print(f"Producto {prod.get_nombre()} eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_producto_id() == producto_id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print(f"Producto {prod.get_nombre()} actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            print(f"Productos encontrados con nombre '{nombre}':")
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for prod in self.productos:
                print(prod)


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            try:
                producto_id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Por favor ingrese valores válidos para los campos.")

        elif opcion == 2:
            try:
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(producto_id)
            except ValueError:
                print("Error: Por favor ingrese un ID válido.")

        elif opcion == 3:
            try:
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad del producto (deje vacío para no cambiar): ")
                precio = input("Ingrese el nuevo precio del producto (deje vacío para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(producto_id, cantidad, precio)
            except ValueError:
                print("Error: Por favor ingrese valores válidos.")

        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == 5:
            inventario.mostrar_inventario()

        elif opcion == 6:
            print("Gracias por usar el sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()
    5