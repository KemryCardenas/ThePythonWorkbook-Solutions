# %% Ejercicio 113: Formatear/Formateando una lista.
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
    # Maneja listas de 0 y 1 elementos como casos especiales.
    if len(elementos) == 0:
        return "<vacio>"
    if len(elementos) == 1:
        return str(elementos[0])

    # Recorre todos los elementos de las listas excepto los dos últimos.
    resultado = ""
    for i in range(0, len(elementos) - 2):
        resultado = resultado + str(elementos[i]) + ", "

    # Añade el penúltimo y el último elemento al resultado, separados por "y".
    resultado = resultado + str(elementos[len(elementos) - 2]) + " y "
    resultado = resultado + str(elementos[len(elementos) - 1])

    # Devuelve el resultado.
    return resultado

# Leer varios elementos introducidos por el usuario y mostrarlos con un
# bonito formato.

def leer_los_elementos_del_usuario():
    """
    Leer varios elementos introducidos por el usuario y darles formato.

    Returns
    -------
    None.

    """
    # Leer los elementos del usuario hasta que se introduzca una línea en
    # blanco.
    elementos = []
    linea = input("Introduce un elemento (línea en blanco para salir): ")
    while linea != "":
        elementos.append(linea)
        linea = input("Introduce un elemento (línea en blanco para salir): ")

    # Formatea y muestra los elementos.
    print("Los elementos son %s." % lista_con_formato(elementos))


# Llama a la función principal.
leer_los_elementos_del_usuario()
