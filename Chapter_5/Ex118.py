# %% Ejercicio 118: Barajar una Baraja de Cartas.
from random import randrange

# Construye una baraja estándar con 4 palos y 13 valores por palo.
# @return una lista de cartas, con cada carta representada por dos caracteres.
def crearbaraja():
    """
    Esta función crea una baraja estándar con 4 palos y 13 valores por cada uno.

    Returns
    -------
    cartas : TYPE
        DESCRIPTION.

    """
    # Crear una lista para almacenar las cartas.
    cartas = []

    # Para cada palo y cada valor.
    for palos in ["s", "h", "d", "c"]:
        for valor in ["2", "3", "4", "5", "6", "7", "8", "9",
                      "T", "J", "Q", "K", "A"]:
            # Construye la carta y añádela a la lista.
            cartas.append(valor + palos)

    # Devuelve la baraja completa.
    return cartas

# Barajear un mazo de cartas, modificando el mazo de cartas pasado como
# parámetro.
# @param cards la lista de cartas a barajar.
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
    # Por cada carta.
    for i in range(0, len(cartas)):
        # Elige un índice aleatorio.
        otra_posicion = randrange(0, len(cartas))

        # Intercambiar la carta actual con la que está en la posición aleatoria.
        temp = cartas[i]
        cartas[i] = cartas[otra_posicion]
        cartas[otra_posicion] = temp

# Mostrar una baraja antes y después de ser barajada.
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

# Llamar al programa principal solo si este archivo no ha sido importado.
if __name__ == "__main__":
    baraja_inicial_y_baraja_final()
