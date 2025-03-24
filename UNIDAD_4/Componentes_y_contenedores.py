import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la entrada de datos
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        # Campos de entrada
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)
        self.descripcion_entry = tk.Entry(frame_entrada, width=40)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=5)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        try:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
