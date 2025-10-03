import re

# Patrones regex
patterns = {
    "variable": re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$'),
    "entero": re.compile(r'^-?\d+$'),
    "decimal": re.compile(r'^-?\d+\.\d+$'),
    "telefono": re.compile(r'^(\+?\d{1,3})?[-.\s]?\d{2,4}[-.\s]?\d{3,4}[-.\s]?\d{3,4}$'),
    "correo": re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'),
    "url": re.compile(
        r'^(https?:\/\/)?'              # http o https opcional
        r'(www\.)?'                     # www opcional
        r'[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'  # dominio
        r'(\.[a-zA-Z]{2,})*'            # subdominios opcionales
        r'(\/\S*)?$'                    # ruta opcional
    )
}

def validar_entrada(entrada: str) -> str:
    for tipo, patron in patterns.items():
        if patron.match(entrada):
            return tipo
    return "ninguno"

def procesar_archivo(archivo_entrada: str, archivo_salida: str):
    with open(archivo_entrada, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Separar por espacios y saltos de línea
    tokens = contenido.split()

    resultados = []
    for token in tokens:
        tipo = validar_entrada(token)
        resultados.append(f"{token} → {tipo}")

    # Guardar resultados en archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(r + "\n")

    print("✅ Análisis completado. Resultados guardados en:", archivo_salida)

# Ejemplo de uso
if __name__ == "__main__":
    procesar_archivo("entradas.txt", "salida.txt")