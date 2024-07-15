def validar_numero(numero):
    if numero == '':
        return float(0)
    return float(numero)

def pedir_parametros():
    ancho = input("Ingrese el ancho (cm): ")
    peralte = input("Ingrese el peralte (cm): ")
    recubrimiento = input("Ingrese el recubrimiento (cm): ")
    
    ancho = validar_numero(ancho)
    peralte = validar_numero(peralte)
    recubrimiento = validar_numero(recubrimiento)

    return ancho, peralte, recubrimiento

def tiene_seccion(ancho: float|None, peralte: float|None) -> bool:
    """
    Valida que el ancho y el peralte tengan valores validos para formar una seccion:
    Especificar que es un valor valido: 
    """
    def valido(dimension):
        if dimension != None and dimension > 0:
          return True
        return False
    #Tambien se puede escribir asi
    #def valido(dimension):
    #return dimension != None and dimension > 0
    #TAMBIEN DE ESTA FORMA
    #valido = lambda dimension: (dimension != None) and (dimension > 0)
    
    if (not valido(ancho) or not valido(peralte)):
        return False
    return True
def parametros_calculos():
    res_concreto = input("Ingrese la resistencia del concreto, f'c (Kg/cm2): ")
    res_acero = input("Ingrese la resistencia de fluencia del acero, Fy (Kg/cm2): ")
    momento_ultimo = input("Ingrese el momento ultimo que debe resistir la viga, Mu (Tn-m): ")

    res_concreto = validar_numero(res_concreto)
    res_acero = validar_numero(res_acero)
    momento_ultimo = validar_numero(momento_ultimo)

    return res_concreto, res_acero, momento_ultimo
