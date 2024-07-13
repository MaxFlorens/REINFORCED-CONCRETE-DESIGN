import os
import sys
import random

from utils.datos import pedir_parametros 
from utils.datos import parametros_iterativo

def MetodoIterativo(ancho, peralte, recubrimiento):
    """
    Params:
        los parámetros se estan especificando en el archivo utils.datos con la función  parametros_iterativo
    Description: 
        En esta funcion se desarrollara el procedo iterativo, con los parametros ya proporcionados 
    """
    res_concreto, res_acero, momento_ultimo = parametros_iterativo() 
    """
    EMPEZAMOS A DETALLAR AL FORUMULA DE ITERACIÓN 
    """
    error = 2
    a_tanteado = random.uniform(0.0, peralte)
    while error > 1:
        peralte_efectivo = peralte - recubrimiento
        As = momento_ultimo/(res_acero * (peralte_efectivo - (a_tanteado/2)))
        a_calculado = (As * res_acero)/(0.85 * res_concreto * ancho)
        #AHORA CALCULAREMOS EL PORCENTAJE DE ERROR
        error = abs(((a_tanteado - a_calculado)/ a_tanteado ) * 100)
        if error > 1:
            print("se esta volviendo a tentear")
            a_tanteado = a_calculado
        else: 
            print("tanteaste bien mi king XD")
            print(a_calculado)
            print(As)
            return As
            
if '__main__' == __name__:
    MetodoIterativo()
