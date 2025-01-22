import random


def MetodoIterativo(ancho, peralte, recubrimiento, res_concreto, res_acero, momento_ultimo):
    """
    Params:
        los parámetros se estan especificando en el archivo utils.datos con la función  parametros_iterativo
    Description: 
        En esta funcion se desarrollara el procedo iterativo, con los parametros ya proporcionados 
    EMPEZAMOS A DETALLAR AL FORUMULA DE ITERACIÓN 
    """
    error = 2
    a_tanteado = random.uniform(0.0, peralte)
    peralte_efectivo = peralte - recubrimiento
    print(peralte_efectivo)
    while error > 1:
        As = (momento_ultimo * 10**5)/(0.9 * res_acero *
                                       (peralte_efectivo - (a_tanteado/2)))
        a_calculado = (As * res_acero)/(0.85 * res_concreto * ancho)
        # AHORA CALCULAREMOS EL PORCENTAJE DE ERROR
        error = abs(((a_tanteado - a_calculado) / a_tanteado) * 100)
        print(f"error: {error}")
        if error > 1:
            print("se esta volviendo a tentear")
            a_tanteado = a_calculado
        else:
            print("tanteaste bien mi king XD")
            print(a_calculado)
            print(As)
            return As


if '__main__' == __name__:
    MetodoIterativo(ancho=1, peralte=1, recubrimiento=1,
                    res_acero=1, res_concreto=1, momento_ultimo=1)
