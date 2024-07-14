import os
import sys

from utils.datos import pedir_parametros, parametros_calculos
from utils.funciones import beta1_fc

def Cuantia_max():
    print("se realizara el proceso del calculo para la cuantia maxima")

def Cuantia_min():
    print("se realizara el proceso del calculo para la cuantia minima")

def menu():
    print("Elige la cuantia que deseas calcular")
    print("1. Cuantia maxima")
    print("2. Cuantia minima")
    print("3. Salir")

def CuantiasMaximasMinimas():
    """
    Params:
        Los parametros necesarios para realizar la función vienen de la función parametros_calculos
    """
    res_concreto, res_acero, momento_ultimo = parametros_calculos()
    beta1 = beta1_fc(res_concreto)
    print(beta1)
    #Generamos un menú para poder elegir si se desea la cuanti máxima o mínima
    while True:
        menu()
        opc = input("Elige una opción (1 o 2 o 3): ")

        if opc == '1':
            Cuantia_max()
        elif opc == '2':
            Cuantia_min()
        elif opc == '3':
            print("Sigue estudiando noma")
            break
        else:
            print("Opcion no valida")
            
if '__main__' == __name__:
    CuantiasMaximasMinimas()
