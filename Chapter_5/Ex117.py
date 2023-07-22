#%% Ejercicio 117: Línea de mejor ajuste
# leer una coleccion de puntos
# escribir la coordenada x y y
# permitir seguir introducciodo coordenadas hasta leer una linea en bllanco
# visualizar la formula de recta de mejor ajuste

x=[]
y=[]
x_cuadrado=[]
xy=[]
# se crean varias variables independientes de tipo lsita
cordenadax=float(input("Ingrese la coordenada X "))
cordenaday=float(input("Ingrese la coordenada Y "))
# se piden un  par de coordenadas iniciales
x.append(cordenadax)
x_cuadrado.append(cordenadax**2)
y.append(cordenaday)
xy.append(cordenadax*cordenaday)
# para cada una de las listas iniciales, se vn añadiendo segun cumplan o se les de distinto aparametro a la funcion
actual=float(input("Ingrese la parte X: "))
# se crea un ciclo que se mantendra activo simepre y cuando no ingrese un espaio el usuario
while actual != '':
    actx=float(actual)
    acty=float(input("Ingrese la parte Y "))
    x.append(actx)
    x_cuadrado.append(actx**2)
    y.append(acty)
    xy.append(actx*acty)
    actual=input("Ingrese la parte X: ")
sumx=sum(x)
sumy=sum(y)
mediax=sum(x)/len(x)
mediay=sum(y)/len(y)
# la linea 266 es la aplicacionde la formula exactamtene como see encuentra en la pagina del libro
m=(sum(xy)-(sumx*sumy/len(x)))/(sum(x_cuadrado)-(sumx**2/len(x)))
b=mediay-m*mediax
print("y =",m,"x+",b)
