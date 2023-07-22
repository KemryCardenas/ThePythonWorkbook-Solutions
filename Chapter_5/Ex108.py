# %% Ejercicio 108: Negativos, Ceros y Positivos.
negativos = []
ceros = []
positivos = []

# Leer todos los enteros del usuario, almacenando cada entero en la lista
# correcta.
linea = input("Ingrese un número entero (en blanco para salir): ")
while linea != "":
    num = int(linea)

    if num < 0:
        negativos.append(num)
    elif num > 0:
        positivos.append(num)
    else:
        ceros.append(num)

    # Leer la siguiente línea de entrada del usuario.
    linea = input("Ingrese un número entero (en blanco para salir): ")

# Mostrar todos los negativos, todos los ceros y al final todos los positivos.
print("Los números fueron: ")

for n in negativos:
    print(n)
for n in ceros:
    print(n)
for n in positivos:
    print(n)
