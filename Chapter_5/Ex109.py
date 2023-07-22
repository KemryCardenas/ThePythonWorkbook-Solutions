# escribe una funcion que calcule todos los divisores propios de un entero positivo
# el entero será pasado a la función como unico parámetro
# la funcion devolvera una lsita con todos los divisores propios como unico resultad
from me_5 import divisores_propios
# definimos la funcion principal que llama a la ubicada en el archivo de funciones
def main():
    # genera la variable independiente n para ingresarla como parametro a la funciones divisores_propios()
    n=int(input("Ingrese el numeor del cual quiere conocer sus divisores "))
    divisores=divisores_propios(n)
    # se corre la funcion y posteriormente se imprime la lista resultante
    print(divisores)
# se hace la validacion de que el programa principal no sea importado a otro archivo
if __name__=='__main__':
    main()
