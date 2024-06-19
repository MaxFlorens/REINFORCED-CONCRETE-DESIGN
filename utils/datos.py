def validar_numero(numero):
    if numero == '':
        return float(0)
    return float(numero)

def pedir_parametros():
    ancho = input("Ingrese el ancho: ")
    peralte = input("Ingrese el peralte: ")
    recubrimiento = input("Ingrese el recubrimiento: ")
    
    ancho = validar_numero(ancho)
    peralte = validar_numero(peralte)
    recubrimiento = validar_numero(recubrimiento)

    return ancho, peralte, recubrimiento

def tiene_seccion(ancho: float|None, peralte: float|None) -> bool:
    """
    Valida que el ancho y el peralte tengan valores validos para formar una seccion:
    Especificar que es un valor valido: 
    """
    valido = lambda dimension: (dimension != None) and (dimension > 0)
    if (not valido(ancho) or not valido(peralte)):
        return False
    return True
