import tkinter as tk
from tkinter import messagebox

# Función para agregar el elemento a la lista
def agregar_elemento():
    elemento = entrada.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")

# Función para limpiar el elemento seleccionado o toda la lista
def limpiar_lista():
    seleccion = lista.curselection()
    if seleccion:
        for index in seleccion[::-1]:  # Eliminar desde el último seleccionado hacia el primero
            lista.delete(index)
    else:
        lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Etiqueta de título
label_titulo = tk.Label(ventana, text="Hola, Soy Mayra Amaguay tu asistente", font=("Arial", 16))
label_titulo.pack(pady=10)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón para agregar el elemento
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
btn_agregar.pack(pady=5)

# Lista para mostrar los elementos agregados
lista = tk.Listbox(ventana, width=50, height=10, selectmode=tk.SINGLE)
lista.pack(pady=5)

# Botón para limpiar la lista o el elemento seleccionado
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()
