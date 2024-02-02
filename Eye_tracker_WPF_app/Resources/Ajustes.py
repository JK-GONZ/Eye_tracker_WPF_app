import tkinter as tk
from tkinter import messagebox
import json

class JsonEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración")

        # Variables para almacenar los datos del JSON
        self.field1_var = tk.StringVar()
        self.field2_var = tk.StringVar()
        self.field3_var = tk.StringVar()
        self.checkbox_var = tk.BooleanVar()

        # Interfaz gráfica
        tk.Label(root, text="relacion_de_aspecto_pestaneo:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.field1_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="cuadros_consecutivos:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.field2_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="tiempo_ejecucion:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.field3_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Checkbutton(root, text="mostrar_cam", variable=self.checkbox_var).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Guardar", command=self.guardar_json).grid(row=4, column=0, columnspan=2, pady=10)

        # Cargar datos del JSON si existe
        self.cargar_json()

    def cargar_json(self):
        try:
            with open("..\..\..\Resources\config.json", "r") as file:
                data = json.load(file)
                self.field1_var.set(data.get("relacion_de_aspecto_pestaneo", ""))
                self.field2_var.set(data.get("cuadros_consecutivos", ""))
                self.field3_var.set(data.get("tiempo_ejecucion", ""))
                self.checkbox_var.set(data.get("mostrar_cam", True))
        except FileNotFoundError:
            pass

    def guardar_json(self):
        data = {
            "relacion_de_aspecto_pestaneo": self.field1_var.get(),
            "cuadros_consecutivos": self.field2_var.get(),
            "tiempo_ejecucion": self.field3_var.get(),
            "mostrar_cam": self.checkbox_var.get()
        }

        try:
            with open("..\..\..\Resources\config.json", "w") as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar los datos. Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonEditorApp(root)
    root.mainloop()
