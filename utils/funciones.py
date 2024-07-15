import random

def beta1_fc(res_concreto):
    if res_concreto >= 175 and res_concreto <= 280:
        beta1 = 0.85
    elif res_concreto == 350:
        beta1 = 0.8
    elif res_concreto == 420:
        beta1 = 0.75
    elif res_concreto == 490:
        beta1 = 0.7
    elif res_concreto >= 560 and res_concreto <= 230:
        beta1 = 0.65
    return beta1

def valor_incial_para_tanteo(res_concreto, res_acero, momento_ultimo, Ro):
    valor_calculado = (momento_ultimo * 10**5)/(0.9 * res_acero * Ro * (1-(0.59 * Ro * (res_acero/res_concreto))))
    print(f"valor inicial para tanteo: {valor_calculado}")
    return valor_calculado

def validartanteo(ancho, peralte_efectivo):
    return ancho < peralte_efectivo

def tanteo(valor_prueba, ancho, peralte, recubrimiento):
    """
    POSIBLE LOGICA PARA REALIZAR EL TANTEO
    error = 21
    while error > 10:
        ancho = random.randint(5, 10) * 5
        peralte_efectivo = random.randint(5,20) * 5
        a = validartanteo(ancho, peralte_efectivo)
        if a == True:
            val_tan = ancho * peralte_efectivo**2
            error = abs(((val_tan-valor_prueba)/(val_tan)) * 100)      
        else:
            error = 21
    return ancho, peralte_efectivo
    """
    valores_ancho = list(range(25,51,5))
    valores_peralte_efectivo = list(range(25,101,5))

    ancho_previo = 0
    peralte_efectivo_previo = 0
    error_= 100

    for ancho in valores_ancho:
        for peralte_efectivo in valores_peralte_efectivo:
            if validartanteo(ancho, peralte_efectivo):
                val_tan = ancho * peralte_efectivo**2
                error = abs(((val_tan-valor_prueba)/(val_tan)) * 100)
                if error < 1 and peralte_efectivo > peralte_efectivo_previo:
                    ancho_previo = ancho
                    peralte_efectivo_previo = peralte_efectivo
                    error_ = error
    print(f"El error mas mínimo es: {error_}")
    return ancho_previo, peralte_efectivo_previo

def CalcularNumeroVarillas():
    """
    Add documentation
    """
    numero_varillas = 0
    area_acero_real = 0
    return numero_varillas, area_acero_real

def VerificarMaximosMinimos():
    """
    Add documentation
    """
    pass

def MostrarConfiguracionVarillas():
    """
    Add documentation
    """
    print(f"Mostrando resultados: \n")

if '__main__' == __name__:
    print("loading utils.funciones.py file\n")


