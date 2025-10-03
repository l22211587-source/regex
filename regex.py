import re
import tkinter as tk
from tkinter import messagebox

def analizar():
    texto = entrada.get()

    if re.fullmatch(r"\d+", texto):   # solo dígitos
        messagebox.showinfo("Resultado", "La entrada contiene SOLO números.")
    elif re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]+", texto):  # solo letras
        messagebox.showinfo("Resultado", "La entrada contiene SOLO letras.")
    else:
        messagebox.showinfo("Resultado", "La entrada contiene una mezcla de números, letras u otros caracteres.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Analizador de entrada")

tk.Label(ventana, text="Escribe algo:").pack(pady=5)

entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

tk.Button(ventana, text="Analizar", command=analizar).pack(pady=5)

ventana.mainloop()
