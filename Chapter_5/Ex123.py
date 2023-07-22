#%% Ejercicio 123: De infijo a postfijo
# tokenizar la expresion matematica
# usar el algoritmo descrito para pasar de la forma infija a la postfija
# implementar un codigo que tome expresion infija, devuelva la expresion postfija como unico resultado
# finalmente  desmotrar que la expresion infija y postfija son equivalentes
from pythonds.basic import Stack
from me_5 import infija_a_Postfija

infija=input("Escriba la expresion matematica infija ")
print("La expresion matematica postfija correspondiente es ",infija_a_Postfija(infija))
