"""
Created on Wed Dec  1 16:16:42 2021

@author: Kemry
"""
# instalar pip install pythonds ingresando "pip install pythonds" en la consola
# fue necesario para los ejercicios 123 y 124
# Ejercicio 109: Lista de divisores propios
def divisores_propios(n):
    """
    

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    divisores : TYPE
        DESCRIPTION.

    """
    divisores=[]
    posibles_divisores=list(range(n+1))
    posibles_divisores.remove(0)
    for x in posibles_divisores:
        if n%x==0:
            divisores.append(x)
    return divisores
# Ejercicio 111: Solo las palabras
import re, string
def limpiar_cadena(cadena):
    """
    

    Parameters
    ----------
    cadena : TYPE
        DESCRIPTION.

    Returns
    -------
    cadena_limpia : TYPE
        DESCRIPTION.

    """
    signos=string.punctuation
    for a in signos:   
        cadena=cadena.replace(a, ' ')
        cadena_limpia=cadena.split()
    return cadena_limpia
# Ejercicio 115: Pig Latin
import re, string
def pig_latin(cadena):
    """
    

    Parameters
    ----------
    cadena : TYPE
        DESCRIPTION.

    Returns
    -------
    traduccion : TYPE
        DESCRIPTION.

    """
    cadena_minuscula_nosignos=cadena.strip(string.punctuation)
    
    traduccion=''
    vocales=['a','e','i','o','u']
    for i in range(len(cadena_minuscula_nosignos)):
        if cadena_minuscula_nosignos[i] in vocales:
            if i==0:
                cadena_minuscula_nosignos +="w"
            traduccion +=cadena_minuscula_nosignos[i:]+cadena_minuscula_nosignos[0:i]+"ay"
            break
    return traduccion
# Ejercicio 116: Pig latin mejorado
def pig_latin2(cadena):
    """
    

    Parameters
    ----------
    cadena : TYPE
        DESCRIPTION.

    Returns
    -------
    traduccion : TYPE
        DESCRIPTION.

    """
    cadena_minuscula_nosignos=cadena.strip()
    
    traduccion=''
    vocales=['a','e','i','o','u']
    for i in range(len(cadena_minuscula_nosignos)):
        if cadena_minuscula_nosignos[i] in vocales:
            if i==0:
                cadena_minuscula_nosignos +="w"
            traduccion +=cadena_minuscula_nosignos[i].upper()+cadena_minuscula_nosignos[i+1:]+cadena_minuscula_nosignos[0:i]+"ay"
            break
    for n in traduccion:
        if n in string.punctuation:
            simbo=n
            traduccion=traduccion.replace(n,"")
            traduccion+=simbo
            
    return traduccion
# Ejercicio 119 repartir manos de cartas
from random import randrange
import random

def crear_cartas():
    """
    

    Returns
    -------
    tarjetas : TYPE
        DESCRIPTION.

    """
    tarjetas=[]
    for palo in ["h","s","c","d"]:
        for carta in ["2","3","4","5","6","7","8","9","I","J","K","Q","A"]:
            tarjetas.append(palo+carta)
    return tarjetas
def revolver(tarjetas):
    """
    

    Parameters
    ----------
    tarjetas : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for i in range (0,len(tarjetas)):
        otra_pos=randrange(0,len(tarjetas))
        n_carta=tarjetas[i]
        tarjetas[i]=tarjetas[otra_pos]
        tarjetas[otra_pos]=n_carta
def repartir(n_manos, n_cartas,tarjetas):
    """
    

    Parameters
    ----------
    n_manos : TYPE
        DESCRIPTION.
    n_cartas : TYPE
        DESCRIPTION.
    tarjetas : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    mano_individual=[]
    manos=[]
    for j in range(n_manos):
        for r in range(n_cartas):
            seleccion=random.choice(tarjetas)
            tarjetas.remove(seleccion)
            mano_individual.append(seleccion)
    dividir= lambda mano_individual, n_manos: [mano_individual[i:i+n_manos] for i in range(0, len(mano_individual), n_manos)]    
    manos=dividir(mano_individual, n_manos)
    print("Las manos generadas son las sigueintes \n",manos)
    print("Las tarjetas restantes \n",tarjetas)
# Ejercicio 120: ¿Está una lista ya ordenada?
def en_orden(lista):
    """
    

    Parameters
    ----------
    lista : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if lista==sorted(lista) or lista==sorted(lista,reverse=True):
        print(True)
    else:
        print(False)
# Ejercicio 123: De infijo a postfijo
from pythonds.basic import Stack

def infija_a_Postfija(expresioninfija):
    """
    

    Parameters
    ----------
    expresioninfija : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    precedente = {}
    precedente["*"] = 3
    precedente["/"] = 3
    precedente["+"] = 2
    precedente["-"] = 2
    precedente["("] = 1
    apilacion = Stack()
    listapostfija = []
    tokenList = expresioninfija.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            listapostfija.append(token)
        elif token == '(':
            apilacion.push(token)
        elif token == ')':
            utlimotoken = apilacion.pop()
            while utlimotoken != '(':
                listapostfija.append(utlimotoken)
                utlimotoken = apilacion.pop()
        else:
            while (not apilacion.isEmpty()) and \
               (precedente[apilacion.peek()] >= precedente[token]):
                  listapostfija.append(apilacion.pop())
            apilacion.push(token)

    while not apilacion.isEmpty():
        listapostfija.append(apilacion.pop())
    return " ".join(listapostfija)
# Ejercicio 124: Evaluar el postfijo
def evaluacion_postfija(expresionpost):
    """
    

    Parameters
    ----------
    expresionpost : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    apilacion = Stack()
    tokenList = expresionpost.split()

    for token in tokenList:
        if token in "0123456789":
            apilacion.push(int(token))
        else:
            operando2 = apilacion.pop()
            operando1 = apilacion.pop()
            result = operacion_post(token,operando1,operando2)
            apilacion.push(result)
    return apilacion.pop()

def operacion_post(op, op1, op2):
    """
    

    Parameters
    ----------
    op :char
        DESCRIPTION.
    op1 : float
        DESCRIPTION.
    op2 : float
        DESCRIPTION.

    Returns
    -------
    TYPE
        float.

    """
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
# Ejercicio 125: ¿La lista contiene una sublista?
def sublista(lar:list,sma:list):
    """
    

    Parameters
    ----------
    lar : list
        DESCRIPTION.
    sma : list
        DESCRIPTION.

    Returns
    -------
    es_o_no : boolean
        DESCRIPTION.

    """
    es_o_no=False
    if sma==[]:
        es_o_no=True
    elif sma==1:
        es_o_no=True
    elif len(sma)>len(lar):
        es_o_no=False
    else:
        for i in range(len(lar)):
            if lar[i]==sma[0]:
                n=1
                while (n<len(sma) and (lar[i+n]==sma[n])):
                    n+=1
                if n==len(sma):
                    es_o_no=True
    return es_o_no
