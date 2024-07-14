def beta1_fc(res_concreto):
    if res_concreto >= '175' and res_concreto <= '280':
        beta1 = 0.85
    elif res_concreto == '350':
        beta1 = 0.8
    elif res_concreto == '420':
        beta1 = 0.75
    elif res_concreto == '490':
        beta1 = 0.7
    elif res_concreto >= '560' and res_concreto <= '230':
        beta1 = 0.65
    return beta1

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


