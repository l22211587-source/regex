import re
import tkinter as tk
from tkinter import messagebox

def analizar():
    texto = entrada.get().strip()

    # patron de correo
    patron_correo = r"^[\w\.-]+@[\w-]+(\.[\w-]{2,}){1,2}$"


    # patron web
    patron_web = r"^(https?://)?(www\.)?([\w-]+\.){1,3}[\w-]{2,}(/.*)?$"

    if re.fullmatch(patron_correo, texto):
        messagebox.showinfo("Resultado", "La entrada es un CORREO ELECTRÓNICO válido.")
    elif re.fullmatch(patron_web, texto):
        messagebox.showinfo("Resultado", "La entrada es una DIRECCIÓN WEB válida.")
    else:
        messagebox.showinfo("Resultado", "La entrada NO es ni correo ni dirección web.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Validador de entradas")

tk.Label(ventana, text="Escribe un correo o una dirección web:").pack(pady=5)

entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

tk.Button(ventana, text="Analizar", command=analizar).pack(pady=5)

ventana.mainloop()
