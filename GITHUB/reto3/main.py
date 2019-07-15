"""funcion principal para evalucion de compuertas logicas"""
import poo

EVAL_AND = poo.CompuertaAND()
EVAL_OR = poo.CompuertaOR()
try:
    print('Ingrese 0 o 1 para las compuertas')
    COMPONENTE1 = int(input('componente 1: '))
    COMPONENTE2 = int(input('componente 2: '))

    print('Resultado Compuerta AND: ' + str(EVAL_AND.evaluar(COMPONENTE1, COMPONENTE2)))
    print('Resultado Compuerta OR: ' + str(EVAL_OR.evaluar(COMPONENTE1, COMPONENTE2)))
except Exception as err:
    print('Error: ' + str(err))
