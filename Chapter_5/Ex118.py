#%% Ejercicio 119 repartir manos de cartas
# usar solicion solucion de 118
# crear un programa principal que cree y barajee una baraja de cartas
# repartir cuatro manos de 5 cartas cada ujna
# mostrar todas las manos  y las cartas que uedan en la baraja despues de repartir las manos
from me_5 import crear_cartas, revolver, repartir
from random import randrange
import random
"""
def crear_cartas():
    tarjetas=[]
    for palo in ["h","s","c","d"]:
        for carta in ["2","3","4","5","6","7","8","9","I","J","K","Q","A"]:
            tarjetas.append(palo+carta)
    return tarjetas
def revolver(tarjetas):
    for i in range (0,len(tarjetas)):
        otra_pos=randrange(0,len(tarjetas))
        n_carta=tarjetas[i]
        tarjetas[i]=tarjetas[otra_pos]
        tarjetas[otra_pos]=n_carta
def repartir(n_manos, n_cartas,tarjetas):
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
"""
def main():
    tarjetas=crear_cartas()
    print("La bajara es \n",tarjetas)
    revolver(tarjetas)
    print("La baraja revuelta es \n",tarjetas)
    repartir(4, 5, tarjetas)

main()
