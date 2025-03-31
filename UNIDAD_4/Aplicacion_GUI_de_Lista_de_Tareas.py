import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Por favor, ingrese una tarea.")

# Función para marcar tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"{task} - Completada")
    except IndexError:
        messagebox.showwarning("Selección Error", "Por favor, seleccione una tarea.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selección Error", "Por favor, seleccione una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Crear el campo de entrada
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Crear botones
add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

mark_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
mark_button.grid(row=1, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Crear Listbox para mostrar tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, padx=10, pady=10)

# Permitir que se añadan tareas presionando Enter
task_entry.bind("<Return>", lambda event: add_task())

# Ejecutar la aplicación
root.mainloop()
