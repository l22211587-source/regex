import re
import tkinter as tk
from tkinter import messagebox

# Definimos los patrones regex
patterns = {
    "variable": re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$'),
    "entero": re.compile(r'^-?\d+$'),
    "decimal": re.compile(r'^-?\d+\.\d+$'),
    "correo": re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'),
    "url": re.compile(
        r'^(https?:\/\/)?'        # http o https opcional
        r'(www\.)?'               # www opcional
        r'[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'  # dominio
        r'(\.[a-zA-Z]{2,})*'             # subdominios opcionales
        r'(\/\S*)?$'              # ruta opcional
    )
}

def validar_entrada(entrada: str) -> str:
    for tipo, patron in patterns.items():
        if patron.match(entrada):
            return tipo
    return "ninguno"

# Función que se ejecuta al presionar el botón
def verificar():
    texto = entrada.get()
    resultado = validar_entrada(texto)
    messagebox.showinfo("Resultado", f"Tipo detectado: {resultado}")

# Crear ventana principal
root = tk.Tk()
root.title("Validador con Regex")
root.geometry("400x200")

# Etiqueta
label = tk.Label(root, text="Ingrese un valor:")
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(root, width=40)
entrada.pack(pady=5)

# Botón
boton = tk.Button(root, text="Verificar", command=verificar)
boton.pack(pady=20)

# Iniciar loop de la ventana
root.mainloop()
