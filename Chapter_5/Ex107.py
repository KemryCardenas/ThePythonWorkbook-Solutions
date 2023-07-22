# %% Ejercicio 107: Evitando Duplicados.
palabras = []
palabra = input("Ingrese una palabra (línea en blanco para salir): ")
while palabra != "":
    # Solo agregue la palabra en la lista si no está ya presente en ella.
    if palabra not in palabras:
        palabras.append(palabra)

    # Leer la siguiente palabra del usuario.
    palabra = input("Ingrese una palabra (linea en blanco para salir): ")

# Mostrar las palabras únicas.
for palabra in palabras:
    print(palabra)
