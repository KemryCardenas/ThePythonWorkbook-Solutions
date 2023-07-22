# %% Ejercicio 126: Generar todas las sublistas de una lista.
def Todaslassublistas(datos):
    # Empezamos con la lista vacia como una sublista de datos
    sublistas = [[]]

    # Generamos toda la sublista de datos desde la longitud 1 hasta la
    # longitud datos
    for longitud in range(1, len(datos) + 1):
        # Generar las sublistas a partir de cada indice
        for i in range(0, len(datos) - longitud + 1):
            # Agregar la sublista actual a la lista de sublistas
            sublistas.append(datos[i: i + longitud])

    # Devolvemos el resultado
    return sublistas


# Demostrar la funcion de todas las sublistas
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


# LLamamos a las funcion principal
mostrar_sublistas()
