# %% Ejercicio 127: El tamiz de Eratóstenes.
limite = int(input("Cual es el limite para buscar sus numeros primos previos? "))

# Generar todos los numeros de 0 al limite
nums = []
for i in range(0, limite+1):
    nums.append(i)

# tachar 1 reemplazadolo con 0
nums[1] = 0

# tachar todos los otros numeros multiplos de cada primo que hemos descubierto
p = 2
while p < limite:
    # tachar todos lo smultiplos de p pero no p
    for i in range(p*2, limite+1, p):
        nums[i] = 0
    # encontrar el siguiente numero que no esta tachado
    p = p+1
    while p < limite and nums[p] == 0:
        p = p+1

# desplegar el resultado
print("Los primos antes del ", limite, "son: ")
for i in nums:
    if nums[i] != 0:
        print(i)
