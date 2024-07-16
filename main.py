from utils.datos import pedir_parametros, tiene_seccion, parametros_calculos
from utils.funciones import (
    CalcularNumeroVarillas,
    MostrarConfiguracionVarillas, 
    VerificarMaximosMinimos,
    # beta1_fc
)
from formulas.metodo_iterativo import MetodoIterativo 
from formulas.metodo_cuantias_maximas_minimas import (
    CuantiasMaximasMinimas
)

def DisenioVigaSimplementeReforzada():

	# ancho (null, float), peralte, recubrimiento <- pedir_parametros()
    ancho, peralte, recubrimiento = pedir_parametros()
    res_concreto, res_acero, momento_ultimo = parametros_calculos()
    peralte_efectivo = 0
    if tiene_seccion(ancho, peralte):
        print(f"Aplicando metodo Iterativo\n")
        uso_metodo_iterativo = True
        area_acero = MetodoIterativo(ancho, peralte, recubrimiento, res_concreto, res_acero, momento_ultimo)
    else:
        print(f"Aplicando metodo de cuantias maximas y minimas\n")
        uso_metodo_iterativo = False
        area_acero, ancho, peralte_efectivo = CuantiasMaximasMinimas(recubrimiento, res_concreto, res_acero, momento_ultimo)

    numero_varillas, area_acero_real, tipo_varilla = CalcularNumeroVarillas(area_acero)
	
    if uso_metodo_iterativo:
        resultado = VerificarMaximosMinimos(area_acero_real, ancho, peralte, recubrimiento, res_concreto, res_acero)
        margen_error = 10
        while resultado == False and margen_error > 0:
            margen_error = margen_error - 0.01
            numero_varillas, area_acero_real, tipo_varilla = CalcularNumeroVarillas(area_acero, margen_error)
            resultado = VerificarMaximosMinimos(area_acero_real, ancho, peralte, recubrimiento, res_concreto, res_acero) 
        if resultado == False:
            print("Se requiere de un diseño para una viga doblemente reforzada") 
            return
    #MostrarConfiguracionVarillas(numero_varillas, area_acero_real, cuantia_real)
    MostrarConfiguracionVarillas(numero_varillas, area_acero_real, ancho, peralte, peralte_efectivo, recubrimiento, uso_metodo_iterativo, tipo_varilla)
    print("GRACIAS POR USAR LA HUMILDE APLICACION")
if '__main__' == __name__:
    DisenioVigaSimplementeReforzada()
