from utils.datos import pedir_parametros, tiene_seccion, VerificarMaximosMinimos, MostrarConfiguracionVarillas
from formulas import MetodoIterativo, CuantiasMaximasMinimas

def DisenioVigaSimplementeReforzada():

	# ancho (null, float), peralte, recubrimiento <- pedir_parametros()
    ancho, peralte, recubrimiento = pedir_parametros()

    """
	Si tiene_seccion(ancho, peralte):
		uso_metodo_iterativo <- verdadero
		AreaAcero <- MetodoIterativo()
	Caso contrario:
		uso_metodo_iterativo <- false
		AreaAcero <- CuantiasMaximasMinimas()
    """
    if tiene_seccion(ancho, peralte):
        use_metodo_iterativo = True
        area_acero = MetodoIterativo()
    else:
        uso_metodo_iterativo = False
        area_acero = CuantiasMaximasMinimas()

	#numero_varillas y area_acero_real <- CalcularNumeroVarillas(AreaAcero)
    numero_varillas, area_acero_real = CalcularNumeroVarillas()
	
    """
	Si uso_metodo_iterativo
		resultado <- VerificarMaximosMinimos(area_acero_real, ancho, peralte_util, parametros) 
		Si resultado verdadero:
			mostrar correcto
		Caso contrario
			mostrar FuncionalError
    """
    if uso_metodo_iterativo:
        resultado = VerificarMaximosMinimos()

    #MostrarConfiguracionVarillas(numero_varillas, area_acero_real, cuantia_real)
    MostrarConfiguracionVarillas()

