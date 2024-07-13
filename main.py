from utils.datos import pedir_parametros, tiene_seccion, parametros_iterativo
from utils.funciones import (
    CalcularNumeroVarillas,
    MostrarConfiguracionVarillas, 
    VerificarMaximosMinimos
)
from formulas.metodo_iterativo import MetodoIterativo 
from formulas.metodo_cuantias_maximas_minimas import (
    CuantiasMaximasMinimas
)

def DisenioVigaSimplementeReforzada():

	# ancho (null, float), peralte, recubrimiento <- pedir_parametros()
    ancho, peralte, recubrimiento = pedir_parametros()

    if tiene_seccion(ancho, peralte, recubrimiento):
        print(f"Aplicando metodo Iterativo\n")
        use_metodo_iterativo = True
        area_acero = MetodoIterativo(ancho, peralte, recubrimiento)
    else:
        print(f"Aplicando metodo de cuantias maximas y minimas\n")
        uso_metodo_iterativo = False
        area_acero = CuantiasMaximasMinimas()

    numero_varillas, area_acero_real = CalcularNumeroVarillas()
	
    if uso_metodo_iterativo:
        resultado = VerificarMaximosMinimos()

    #MostrarConfiguracionVarillas(numero_varillas, area_acero_real, cuantia_real)
    MostrarConfiguracionVarillas()

if '__main__' == __name__:
    DisenioVigaSimplementeReforzada()
