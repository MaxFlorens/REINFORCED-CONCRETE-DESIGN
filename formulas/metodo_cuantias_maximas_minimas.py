import os
import sys

from utils.datos import pedir_parametros, parametros_calculos
from utils.funciones import beta1_fc, tanteo, valor_incial_para_tanteo

def Cuantia_max(Cuantia_bal):
    
    Ro = 0.75 * Cuantia_bal
    print(f"se realizara el proceso del calculo para la cuantia maxima con un Ro de: {Ro}")
    return Ro

def Cuantia_min(res_concreto, res_acero):

    Ro = (0.7 * res_concreto**(1/2))/(res_acero)
    print(f"se realizara el proceso del calculo para la cuantia mínima con un Ro de: {Ro}")
    return Ro

def menu():
    print("Elige la cuantia que deseas calcular")
    print("1. Cuantia maxima")
    print("2. Cuantia minima")
    print("3. Salir")

def CuantiasMaximasMinimas(recubrimiento):
    """
    Params:
        Los parametros necesarios para realizar la función vienen de la función parametros_calculos
    """
    
    res_concreto, res_acero, momento_ultimo = parametros_calculos()
    beta1 = beta1_fc(res_concreto)
    print(f"Valor de beta 1: {beta1}")
    #Calculamos la cuantía balanceada usando los parametros anteriores
    Cuantia_bal = (0.85 * res_concreto * beta1 * 6000)/(res_acero * (6000 + res_acero))
    #Generamos un menú para poder elegir si se desea la cuanti máxima o mínima
    while True:
        menu()
        opc = input("Elige una opción (1 o 2 o 3): ")

        if opc == '1':
            Ro = Cuantia_max(Cuantia_bal)
            valor_prueba2 = valor_incial_para_tanteo(res_concreto, res_acero, momento_ultimo, Ro)
            ancho, peralte_efectivo = tanteo(valor_prueba=valor_prueba2, ancho=0, peralte=0, recubrimiento=recubrimiento)
            print(f"El valor aproximado con los valores tanteados es: {ancho*peralte_efectivo**2}")
            As = Ro * ancho * peralte_efectivo
            print(f"El area de acero calculado es: {As}")
            print(f"El ancho tanteado es de: {ancho}")
            print(f"El peralte tanteado es de: {peralte_efectivo}")
            return As
        elif opc == '2':
            Ro = Cuantia_min(res_concreto, res_acero)
            valor_prueba2 = valor_incial_para_tanteo(res_concreto, res_acero, momento_ultimo, Ro)
            ancho, peralte_efectivo = tanteo(valor_prueba=valor_prueba2, ancho=0, peralte=0, recubrimiento=recubrimiento)
            print(f"El valor aproximado con los valores tanteados es: {ancho*peralte_efectivo**2}")
            As = Ro * ancho * peralte_efectivo
            print(f"El area de acero calculado es: {As}")
            print(f"El ancho tanteado es de: {ancho}")
            print(f"El peralte tanteado es de: {peralte_efectivo}")
            return As
        elif opc == '3':
            print("Sigue estudiando noma")
            break
        else:
            print("Opcion no valida")
            
if '__main__' == __name__:
    print(f"AREA DE ACERO: {CuantiasMaximasMinimas(recubrimiento=1)}")
    
