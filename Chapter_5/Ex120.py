#%% Ejercicio 120: ¿Está una lista ya ordenada?
from me_5 import en_orden

# variables independientes
n=input("Ingrese una lista de enteros separados por comas ").split(',')
n=list(map(int, n))
en_orden(n)
