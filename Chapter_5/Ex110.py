# %% Ejercicio 110: Números Perfectos.
from mer_5 import divisores_propios
limite = 10000

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
    # Obten una lista de los divisores propios de n
    divisores = divisores_propios(n)

    # Calcular el total de todos los divisores
    total = 0
    for d in divisores:
        total = total + d

    # Devuelve el resultado adecuado
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


# Llamar a la función principal
n = int(input("Escribe un número entero positivo: "))
print("El número", n, "es perfecto: ", esPerfecto(n))
mostrar_todos_los_numeros_perfectos_entre_1_y_limite()
