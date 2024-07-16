# import os
# import sys

# from utils.datos import pedir_parametros, parametros_calculos
from utils.funciones import beta1_fc, tanteo, valor_incial_para_tanteo, cuantia_balanceada, menu, Cuantia_max, Cuantia_min

def CuantiasMaximasMinimas(recubrimiento, res_concreto, res_acero, momento_ultimo):
    """
    Params:
        Los parametros necesarios para realizar la función vienen de la función parametros_calculos
    """
    beta1 = beta1_fc(res_concreto)
    print(f"Valor de beta 1: {beta1}")
    #Calculamos la cuantía balanceada usando los parametros anteriores
    Cuantia_bal = cuantia_balanceada(res_concreto, res_acero, beta1)
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
            return As, ancho, peralte_efectivo
        elif opc == '3':
            print("Sigue estudiando noma")
            break
        else:
            print("Opcion no valida")
            
if '__main__' == __name__:
    print(f"AREA DE ACERO: {CuantiasMaximasMinimas(recubrimiento=1, res_acero=1, res_concreto=1, momento_ultimo= 1)}")
    
