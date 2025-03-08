class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = (titulo,)  # Tupla para hacer el título inmutable
        self.autor = (autor,)  # Tupla para hacer el autor inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo[0]} - {self.autor[0]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join([str(libro) for libro in self.libros_prestados])


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = {}  # Diccionario de usuarios con ID como clave

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"⚠️ El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro '{libro.titulo[0]}' agregado correctamente.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"✅ Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"⚠️ No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"⚠️ El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"✅ Usuario '{usuario.nombre}' registrado correctamente.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"✅ Usuario con ID {id_usuario} eliminado correctamente.")
        else:
            print(f"⚠️ No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"⚠️ El libro con ISBN {isbn} no está disponible en la biblioteca.")
            return
        if id_usuario not in self.usuarios:
            print(f"⚠️ El usuario con ID {id_usuario} no está registrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro in usuario.libros_prestados:
            print(f"⚠️ El usuario {usuario.nombre} ya tiene el libro '{libro.titulo[0]}' prestado.")
        else:
            usuario.libros_prestados.append(libro)
            print(f"✅ Libro '{libro.titulo[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"⚠️ El usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                print(f"✅ Libro '{libro.titulo[0]}' devuelto por {usuario.nombre}.")
                return

        print(f"⚠️ El usuario {usuario.nombre} no tiene prestado un libro con ISBN {isbn}.")

    def buscar_libro(self, termino):
        resultados = [
            libro for libro in self.libros.values()
            if termino.lower() in libro.titulo[0].lower() or
               termino.lower() in libro.autor[0].lower() or
               termino.lower() in libro.categoria.lower()
        ]
        if resultados:
            print("\n🔍 Libros encontrados:")
            for libro in resultados:
                print(f"📖 {libro}")
        else:
            print("⚠️ No se encontraron libros con ese término.")

    def listar_libros_prestados(self):
        print("\n📚 Libros actualmente prestados:")
        for usuario in self.usuarios.values():
            if usuario.libros_prestados:
                print(f"\n👤 {usuario.nombre} ({usuario.id_usuario}):")
                print(usuario.listar_libros_prestados())
        print("✅ Fin de la lista.")


# =========================
# 🚀 PRUEBAS DEL SISTEMA
# =========================

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "123456")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "234567")
libro3 = Libro("1984", "George Orwell", "Distopía", "345678")

# Crear usuarios
usuario1 = Usuario("Mayra", "U001")
usuario2 = Usuario("Luciana", "U002")

# Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("123456", "U001")
biblioteca.prestar_libro("234567", "U002")

# Listar libros prestados
biblioteca.listar_libros_prestados()

# Buscar un libro
biblioteca.buscar_libro("Orwell")

# Devolver libros
biblioteca.devolver_libro("123456", "U001")

# Listar libros después de la devolución
biblioteca.listar_libros_prestados()
