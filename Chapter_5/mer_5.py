"""
Created on Wed Nov 24 01:17:31 2021

@author: kemry
"""
if __name__ == "mer_5.py":
    print("Este es el archivo de mer_5.py")
    print(__name__)
print(__name__)


# Ejercicio 106:Eliminar Valores Atípicos.
def eliminar_valores(lista_de_valores, n=2):
    """
    Ordena la lista de valores en forma ascendente y elimina los dos valores
    mas pequeños y los dos valores más grandes.

    Parameters
    ----------
    lista_de_valores : list
        Almacena los valores ingresados por el usuario.
    n : int
        Numero de valores mas pequeños y mas grandes para eliminar.

    Returns
    -------
    lista_ordenada : list
        Nos devuelve la lista ordenada.

    """

    lista_ordenada = sorted(lista_de_valores)
    for i in range(n):  # Elimina los dos valores más grandes
        lista_ordenada.pop()
    for i in range(n):  # Elimina los dos valores mas pequeños
        lista_ordenada.pop(0)
    return lista_ordenada


def ingresa_valores():
    """
    Pide al usuario ingresar sus valores para eliminar los valores más grandes
    y más pequeños y mostrar la lista con los valores restantes.

    Returns
    -------
    Muestra la lista con los valores eliminados

    """
    valores = []
    s = input("Ingresa un valor (linea en blanco para salir): ")
    while s != "":
        numero = float(s)
        valores.append(numero)
        s = input("Ingresa un valor (linea en blanco para salir): ")
    if len(valores) < 4:
        print("No ingresaste suficientes valores")
    else:
        print("La lista con los dos valores más grandes y pequeños eliminados es:",
              eliminar_valores(valores, 2))
        print("La lista original es: ", valores)


# Ejercicio 109: Lista de Divisores Propios
def divisores_propios(n):
    """
    Está función nos determinará los divisores propios de un número "n" que
    el usuario ingresará. Los divisores propios son aquellos que dividen
    uniformemente a n.

    Parameters
    ----------
    n : Número.
        DESCRIPTION. Este número es ingresado por el usuario, puede ser de
        tipo flotante, entero, etc.

    Returns
    -------
    None.

    """
    lista_divisores = []
    for divisor in range(1, n):
        if n % divisor == 0:
            divisores = divisor
            lista_divisores.append(divisores)

    return lista_divisores


def valor_del_usuario():
    """
    Leer el valor de "n" introducido por el usuario.

    Returns
    -------
    None.

    """
    n = int(input("Escribe un número entero positivo: "))
    print("Los divisores propios de", n, "son:", divisores_propios(n))


# Ejercicio 110: Números Perfectos.
def esPerfecto(n):
    """
    Determina si un número es perfecto o no. Un número es perfecto si la
    suma de sus divisores propios es igual al propio número.

    Parameters
    ----------
    n : int
        n es el número a comprobar para la perfección

    Returns
    -------
    bool
        Return True si el número es perfecto, False en caso contrario

    """
    divisores = divisores_propios(n)

    total = 0
    for d in divisores:
        total = total + d

    if total == n:
        return True
    return False


def mostrar_todos_los_numeros_perfectos_entre_1_y_limite():
    """
    Mostrar todos los números perfectos entre 1 y limite

    Returns
    -------
    None.

    """
    print("Los números perfectos entre 1 y", limite, "son:")
    for i in range(1, limite + 1):
        if esPerfecto(i):
            print(" ", i)

# Ejercicio 113: Formatear/Formateando una lista.
def lista_con_formato(elementos):
    """
    Formatear una lista y separarla por comas y la palabra "y" entre el
    penúltimo y último elemento (dar formato especifico a una lista).

    Parameters
    ----------
    elementos : TYPE
        DESCRIPTION. El usuario ingresara uno o más elementos.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if len(elementos) == 0:
        return "<vacio>"
    if len(elementos) == 1:
        return str(elementos[0])

    resultado = ""
    for i in range(0, len(elementos) - 2):
        resultado = resultado + str(elementos[i]) + ", "

    resultado = resultado + str(elementos[len(elementos) - 2]) + " y "
    resultado = resultado + str(elementos[len(elementos) - 1])

    return resultado


def leer_los_elementos_del_usuario():
    """
    Leer varios elementos introducidos por el usuario y darles formato.

    Returns
    -------
    None.

    """
    elementos = []
    linea = input("Introduce un elemento (línea en blanco para salir): ")
    while linea != "":
        elementos.append(linea)
        linea = input("Introduce un elemento (línea en blanco para salir): ")

    print("Los elementos son %s." % lista_con_formato(elementos))


# Ejercicio 118: Barajar una Baraja de Cartas
def crearbaraja():
    """
    Esta función crea una baraja estándar con 4 palos y 13 valores por cada uno

    Returns
    -------
    cartas : TYPE
        DESCRIPTION.

    """
    cartas = []

    for palos in ["s", "h", "d", "c"]:
        for valor in ["2", "3", "4", "5", "6", "7", "8", "9",
                      "T", "J", "Q", "K", "A"]:
            cartas.append(valor + palos)

    return cartas


def barajar(cartas):
    """
    Está función modifica la baraja inicial (función crearbaraja) para poder
    crear otra diferente.

    Parameters
    ----------
    cartas : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for i in range(0, len(cartas)):
        otra_posicion = randrange(0, len(cartas)) # Importa randrange from random

        temp = cartas[i]
        cartas[i] = cartas[otra_posicion]
        cartas[otra_posicion] = temp


def baraja_inicial_y_baraja_final():
    """
    Está función nos permite poder imprimir el resultado de las funciones
    previamente definidas (tanto la baraja inicial como la final).

    Returns
    -------
    None.

    """
    cartas = crearbaraja()
    print("La baraja original de cartas es: ")
    print(cartas)
    print()

    barajar(cartas)
    print("La mazo barajado de cartas es: ")
    print(cartas)


# Ejercicio 121: Cuenta los Elementos
def countRange(datos, mn, mx):
    count = 0
    for e in datos:
        if mn <= e and e < mx:
            count = count + 1

    return count


def rango_de_conteo():
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Contando los elementos en [1,2...,10] que estan entre 5 y 7...")
    print("Resultado: %d Esperado: 0" % countRange(datos, 5, 7))
    
    print("Contando los elementos en [1,2...,10] que estan entre -5 y 77...")
    print("Resultado: %d Esperado: 10" % countRange(datos, -5, 77))
    
    print("Contando los elementos en [1,2...,10] que estan entre 12 y 17...")
    print("Resultado: %d Esperado: 0" % countRange(datos, 12, 17))
    
    print("Contando los elementos en [] que estan entre 0 y 100...")
    print("Resultado: %d Esperado: 10" % countRange([], 0, 100))
    
    datos = [1,2,3,4,1,2,3,4]
    print("Contando los elementos en [1,2,3,4,1,2,3,4] que estan entre 2 y 4...")
    print("Resultado: %d Esperado: 4 " % countRange(datos, 2, 4))


# Ejercicio 122: Tokenizando una Cadena.
def tokenList(s):
    s = s.replace(" ", "")
    token = []
    i = 0
    while i < len(s):
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "(" or s[i] == ")":
            token.append(s[i])
            i = i+1
        elif s[i] == "+" or s[i] == "-":
            if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1] == ")"):
                token.append(s[i])
                i = i+1
            else:
                num = s[i]
                i = i+1
                while i < len(s) and s[i] >= "0" and s[i] <= "9":
                    num = num+s[i]
                    i = i+1
                token.append(num)
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num+s[i]
                i = i+1
            token.append(num)
        else:
            return []
    return token


def tokenizar():
    exp = input("Ingrese una expresion matematica : ")
    token = tokenList(exp)
    print("Los tokens son: ", token)


# Ejercicio 126: Generar todas las sublistas de una lista
def Todaslassublistas(datos):
    sublistas = [[]]

    for longitud in range(1, len(datos) + 1):
        for i in range(0, len(datos) - longitud + 1):
            sublistas.append(datos[i: i + longitud])

    return sublistas


def mostrar_sublistas():
    print("Las sublistas de [] son :")
    print(Todaslassublistas([]))

    print("Las sublistas de [1] son :")
    print(Todaslassublistas([1]))

    print("Las sublistas de [1, 2] son :")
    print(Todaslassublistas([1, 2]))

    print("Las sublistas de [1, 2, 3] son :")
    print(Todaslassublistas([1, 2, 3]))

    print("Las sublistas de [1, 2, 3, 4] son :")
    print(Todaslassublistas([1, 2, 3, 4]))
