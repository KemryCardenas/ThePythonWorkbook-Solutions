#%% Ejercicio 116: Pig latin mejorado
# extender la solucion del ejercicio 115
# hacer que pueda admitir sinos de puntuacion
# al hacer la traduccion debe empezar con mayuscula
import re, string
from me_5 import pig_latin2

def main():
    cadena=input("Ingrese la cadena a convertir en pig latin ").lower()
    # la candena ingresada por el usuario, es convertida directamente a minusculas a fin de podres ser mejor manejada
    traduccion=pig_latin2(cadena)
    print(traduccion)
main()
