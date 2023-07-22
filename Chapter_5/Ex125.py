#%% Ejercicio 125: ¿La lista contiene una sublista?
# crear una funcion que determina si una lista es o no una sublista de otra
# debe tomar dos listas mayor y menor
# debe devolver True si y solo si smaller es sublista de larger
from me_5 import sublista

def main():
    # se crean un par de variables independientes, se espera que en cada una de ellas se ingrese unaa cadena menor que la anterior 
    larger=input("Ingresar uan lista: ")   
    smaller=input("Ingresar otra lista mas pequeña que la primera: ")
    print(sublista(larger, smaller))  
    # se imprime el valor resultante de ingresar como parableytrod ambas cadenas en la funcion que determian di es o no lista una de la otra
main()   
