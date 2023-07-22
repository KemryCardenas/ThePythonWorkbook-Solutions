# %% Ejercicio 114: Números Aleatorios de la Loteria.
from random import randrange

num_min = 1
num_max = 49
num_nums = 6

# Mantener una lista de los números para el billete
ticket_nums = []

#Generar num_nums números aleatorios pero distintos
for i in range(num_nums):
    #Generar un número que no esté ya en el ticket
    rand = randrange(num_min, num_max + 1)
    while rand in ticket_nums:
        rand = randrange(num_min, num_max + 1)
        
    #Agregar el número distinto al billete
    ticket_nums.append(rand)
        
#Ordenar los números en orden ascendente y mostrarlos
ticket_nums.sort()
print("Sus números son: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()
