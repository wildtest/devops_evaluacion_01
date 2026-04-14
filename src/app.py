def saludar(nombre):
    if not nombre.strip():
        return "Hola, Usuario. Bienvenido al curso de GitHub."
    return f"Hola, {nombre}. Bienvenido a la Evaluación Final."

if __name__ == "__main__":
    print(saludar("Wilder"))