# %% Ejercicio 106: Eliminar Valores Atípicos.
def eliminar_valores(lista_de_valores, n=2): # n = numero de valores mas
                                             # pequeños y mas grandes para
                                             # eliminar
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
    if len(valores)<4:
        print("No ingresaste suficientes valores")
    else:
        print("La lista con los dos valores más grandes y pequeños eliminados es:",
              eliminar_valores(valores, 2))
        print("La lista original es: ", valores)


ingresa_valores() 
