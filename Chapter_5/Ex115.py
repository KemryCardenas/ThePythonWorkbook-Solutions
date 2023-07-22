#%% Ejercicio 115: Pig Latin
# escribir un programa que lea una linea de texto del usuario
# traducir al latin de los cerdos y mostrar el resultado
# se puede suponer que el usuario solo contiene letras minusulas y espacios
import re, string
from me_5 import pig_latin
# se crea una funcion principal para ejecutar la funcion importada
def main():
    cadena=input("Ingrese la cadena a convertir en pig latin ").lower()
    # la candena ingresada por el usuario, es convertida directamente a minusculas a fin de podres ser mejor manejada
    traduccion=pig_latin(cadena)
    print(traduccion)
