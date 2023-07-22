def countRange (datos , mn , mx):
    count = 0
    for e in datos :
        # Comprobar cada elemento
        if mn <= e and e < mx:
            count = count + 1
            
    # Devolver el resultado
    return count

# Demostrar la funcion de rango de conteo
def rango_de_conteo() :
    datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Probemos un caso en el que algunos elementos esten dentro del rango
    print("Contando los elementos en [1,2...,10] que estan entre 5 y 7...")
    print("Resultado: %d Esperado: 0" % countRange(datos, 5, 7))
    
    # Probemos un caso en el que todos los elementos esten dentro del rango
    print("Contando los elementos en [1,2...,10] que estan entre -5 y 77...")
    print("Resultado: %d Esperado: 10" % countRange(datos, -5, 77))
    
    # Probemos un caso en que no haya elementos dentro de un rango
    print("Contando los elementos en [1,2...,10] que estan entre 12 y 17...")
    print("Resultado: %d Esperado: 0" % countRange(datos, 12, 17))
    
    # Probemos un caso en el que la lista esta vacia
    print("Contando los elementos en [] que estan entre 0 y 100...")
    print("Resultado: %d Esperado: 10" % countRange([], 0, 100))
    
    # Probemos un caso con valores duplicados
    datos = [1,2,3,4,1,2,3,4]
    print("Contando los elementos en [1,2,3,4,1,2,3,4] que estan entre 2 y 4...")
    print("Resultado: %d Esperado: 4 " % countRange(datos, 2, 4))
    
# Llamemos a la funcion especial
rango_de_conteo()
