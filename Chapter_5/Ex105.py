#%% Ejercicio 105: Orden en reversa
# realizar un programa que lea datos del usuario
# los almacene en una lista y despues de ingresar un 0 termine con la entrada y los despliegue de forma inversa
# mostrando un valor por cada linea
# variables independientes
numeros=[]
n=int(input("Ingrese un nuemro entero "))
# se crea una lista vacia, se crea un input con numero entero que el usuario introducira
while n!=0:
    # se crea un bucle con el que mientres el numero ingresado no sea 0 sigue añadiendolos a la lista numeros
    numeros.append(n)
    n=int(input("Ingrese un nuemro entero "))
numeros.reverse()
# finalmente invierte la lista de numeros y la despliega con otrobucle de tipo for
for x in numeros:
    print(x)
