# %% Ejercicio 104: Orden de Clasificación.
x = []
entero = int(input("Ingresa un entero: "))
while not entero == 0:
    x.append(entero)
    entero = int(input("Ingresa un entero: "))
x.sort()
print("Los valores ordenados son: ")
for entero in x:
    print(entero)
