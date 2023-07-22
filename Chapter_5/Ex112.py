# leer datos del usuario hasta introduccir una linea en blanca
# mostrar el promedio de valores
# nostrar los valores por debajo de la media, los valores medios y los valores por encima de la media
from statistics import mean
# se importa el metodo mean de la biblioteca statistics
n=input("Ingrese un numero ")
# se da n como la variable independiente, se crea tambien la lista de valores
valores=[]
while n!=" " and n!='':
    # se crea un loop while que dejera de ingresar datos en el momento en que se de un espacion o un enter
    valores.append(n)
    # se va agragando cada valor del usuario a la lista
    n=input("Ingrese un numero ")
valores=[float(x) for x in valores]
# se convierten los varores de tipo char a float para asi poder ser manejados con procesos de comparacion numerica
media=mean(valores)
# es usado el modulo importado para sacar la media de lalista de valores
menores_a_media=[x for x in valores if x<media]
mayores_a_media=[x for x in valores if x>media]
# con los valores y la media se hace una comparacion y segun sea el criterio los agrega a la lista de numeros mayores y menores
val_medios=[x for x in valores if x==media]
# se hace una comparacion con el valor medio y en caso de coincidir se añade a la lista
print(" Debajo de la media :",menores_a_media,"\n","Valores medios :",val_medios,"\n","Arriba de la media :",mayores_a_media)
