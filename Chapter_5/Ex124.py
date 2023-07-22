#%% Ejercicio 124: Evaluar el postfijo
# crear un programa que lea una expresion matematica infija del usuario, la evalue y sea desplegada
from pythonds.basic import Stack
from me_5 import infija_a_Postfija, evaluacion_postfija

infija=input("Escriba la expresion matematica infija ")
postfija=infija_a_Postfija(infija)
# usando el mismo algoritmo, una operacio simple a su forma infija
print(postfija)
print(evaluacion_postfija(postfija))
# despues de esto podemos evaluiar el  valor de la expresion en modo postfijo
