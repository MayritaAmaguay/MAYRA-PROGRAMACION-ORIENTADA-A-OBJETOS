import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nueva tarea
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Funcionalidades de atajos de teclado
        self.root.bind("<Return>", self.add_task_shortcut)
        self.root.bind("<C>", self.complete_task_shortcut)
        self.root.bind("<Delete>", self.delete_task_shortcut)
        self.root.bind("<Escape>", self.close_app)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

    def add_task_shortcut(self, event):
        self.add_task()

    def complete_task(self):
        selected_task = self.get_selected_task()
        if selected_task is not None:
            self.tasks[selected_task]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Seleccionar tarea", "Por favor, seleccione una tarea.")

    def complete_task_shortcut(self, event):
        self.complete_task()

    def delete_task(self):
        selected_task = self.get_selected_task()
        if selected_task is not None:
            del self.tasks[selected_task]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Seleccionar tarea", "Por favor, seleccione una tarea.")

    def delete_task_shortcut(self, event):
        self.delete_task()

    def close_app(self, event):
        self.root.quit()

    def get_selected_task(self):
        try:
            return self.task_listbox.curselection()[0]
        except IndexError:
            return None

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_display = task["task"]
            if task["completed"]:
                task_display = f"[Completada] {task_display}"
            self.task_listbox.insert(tk.END, task_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
