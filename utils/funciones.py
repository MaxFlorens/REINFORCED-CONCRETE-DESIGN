# import random
# from formulas.metodo_cuantias_maximas_minimas import Cuantia_min

def Cuantia_max(Cuantia_bal):
    
    Ro = 0.75 * Cuantia_bal
    print(f"se realizara el proceso del calculo para la cuantia maxima con un Ro de: {Ro}")
    return Ro

def Cuantia_min(res_concreto, res_acero):

    Ro = (0.7 * res_concreto**(1/2))/(res_acero)
    print(f"se realizara el proceso del calculo para la cuantia mínima con un Ro de: {Ro}")
    return Ro

def menu():
    print("Elige la cuantia que deseas calcular")
    print("1. Cuantia maxima")
    print("2. Cuantia minima")
    print("3. Salir")

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
                #print(f"estos son los errores que resultan: {error}")
                if error < 5 and peralte_efectivo > peralte_efectivo_previo:
                    ancho_previo = ancho
                    peralte_efectivo_previo = peralte_efectivo
                    error_ = error
                    #print(f"El error que queda al ultimo: {error_}")
    print(f"El error mas mínimo es: {error_}")
    return ancho_previo, peralte_efectivo_previo

def cuantia_balanceada(res_concreto, res_acero, beta1):
    Cuantia_bal = (0.85 * res_concreto * beta1 * 6000)/(res_acero * (6000 + res_acero))
    return Cuantia_bal

def CalcularNumeroVarillas(area_acero, margen_error = 1):
    """
    Se calculara las varillas necesarias para obtener un error menor a 10% entre el area de acero teorico y el real 
    OJO: se usaran varillas de un solo área 
    """
    area_acero_real_previo = 0
    numero_varillas_previo = 1000
    tipo_varilla = ''
    #areas_nominales = [0.28, 0.50, 0.71, 1.13, 1.29, 1.99, 2.84, 5.10, 10.06]
    varillas_nominales = {'6mm': 0.28,'8mm': 0.50, '3/8"': 0.71, '12mm': 1.13, '1/2"': 1.29, '5/8"': 1.99, '3/4"': 2.84, '1"': 5.10, '1 3/8"': 10.06}
    
    for varilla in varillas_nominales:
        numero_varillas = area_acero // varillas_nominales[varilla]
        area_acero_real = numero_varillas * varillas_nominales[varilla]
        error = abs(((area_acero - area_acero_real)/(area_acero))*100)
        if error < margen_error and numero_varillas < numero_varillas_previo:
            area_acero_real_previo = area_acero_real
            numero_varillas_previo = numero_varillas
            tipo_varilla = varilla
           # print(f"El area de acero real es: {area_acero_real}")
            #print(f"El numero de varillas es: {numero_varillas}")
            #print(f"La varilla usada es : {varilla} cuyo area es : {varillas_nominales[varilla]} cm2")
            #print(f"El porcentaje de error la usar esta varillas es de: {error}")
    return numero_varillas_previo, area_acero_real_previo, tipo_varilla

def VerificarMaximosMinimos(area_acero_real, ancho, peralte, recubrimiento, res_concreto, res_acero):
    """
    Esta verificación solo se realizará cuando se aplique el método iterativo
    - Se determina el valor del beta1
    - Se determinara la cuantia balanceada
    - Se determinara la cuantia maxima
    - Se determinara la cuantia minima
    - Se determinara la cuantia de acuerda al área de acero y el ancho y el peralte efectivo (peralte-recubrimiento)
    - esta funcion es una validación, que resultará en verdadera si la cuntia calculada, es menor a la cuantía máxima 
    y mayor a la cuantia minima.
    """
    beta1 = beta1_fc(res_concreto)
    Cuantia_bal = cuantia_balanceada(res_concreto, res_acero, beta1)
    Cuantia_maxima = Cuantia_bal * 0.75
    Cuantia_minima = Cuantia_min(res_concreto, res_acero)
    peralte_efectivo = peralte - recubrimiento
    Cuantia_calculada = area_acero_real / (ancho * peralte_efectivo)
    return (Cuantia_calculada < Cuantia_maxima and Cuantia_calculada > Cuantia_minima)

def MostrarConfiguracionVarillas(numero_varillas, area_acero_real, ancho, peralte, peralte_efectivo, recubrimiento, uso_metodo_iterativo, tipo_varilla):
    """
    Se mostrarán todos los resultados según sea el caso que se trabajo
    - si se uso el metodo de iteración, se tendra que calcular el peralte efectivo para mostrarlo
    - si se uso el metodo de cuantias, el peralte efectivo ya tendra y no sera necesario calcularlo
    """
    print(f"Mostrando resultados: \n")
    if uso_metodo_iterativo:
        peralte_efectivo = peralte - recubrimiento
        print(f"La seccion de la viga es de: ancho = {ancho}, peralte = {peralte}, recubrimiento = {recubrimiento}")
        print(f"peralte efectivo = {peralte_efectivo}")
        print(f"El acero real en la viga es de: {area_acero_real} y el numero de varillas es de {numero_varillas} de {tipo_varilla}")
    peralte = peralte_efectivo + recubrimiento
    print(f"La seccion de la viga es de: ancho = {ancho}, peralte = {peralte}, recubrimiento = {recubrimiento}")
    print(f"peralte efectivo = {peralte_efectivo}")
    print(f"El acero real en la viga es de: {area_acero_real} y el numero de varillas es de {numero_varillas} de {tipo_varilla}")
if '__main__' == __name__:
    numero_varillas_previo, area_acero_real_previo = CalcularNumeroVarillas(area_acero=25.5)
    print(f"numero de varillas optimo : {numero_varillas_previo}")
    print(f"area de acero real: {area_acero_real_previo}")
    print("loading utils.funciones.py file\n")


