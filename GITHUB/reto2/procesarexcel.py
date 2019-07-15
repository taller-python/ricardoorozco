"""Funcion para procesamiento de archivo excel y operaciones artitmeticas"""
import os
import xlrd

def calculo_aritmetico_excel():
    "funcion encargada de aplicar la operacion aritmetica del archivo excel"
    try:
        cwd = os.getcwd()
        print('Directorio local: ' + str(cwd))
        print('Buscando archivo "operaciones.xlsx" en directorio local')

        fxlsx = xlrd.open_workbook('operaciones.xlsx')

        for sheet in fxlsx.sheets():
            print('Ejecutando operacion ' + sheet.name + '....')
            try:
                fout = open('resultado'+ sheet.name +'.txt', 'wt')
                for i in range(sheet.nrows):
                    if i > 0:
                        try:
                            cell_a = float(sheet.cell_value(i, 0))
                            cell_b = float(sheet.cell_value(i, 1))

                            if sheet.name == 'SUMA':
                                resultado = cell_a + cell_b
                            elif sheet.name == 'RESTA':
                                resultado = cell_a - cell_b
                            elif sheet.name == 'MULTIPLICACIÓN':
                                resultado = cell_a * cell_b
                            elif sheet.name == 'DIVISIÓN':
                                resultado = cell_a / cell_b

                            fout.write(str(resultado) + '\n')
                        except ArithmeticError as err:
                            fout.write('Error\n')
                        except ValueError as err:
                            fout.write('Error\n')
                print('Proceso finalizado. Se genero el archivo "resultado'+sheet.name+'.txt" con el resultado de la operacion')
            except FileNotFoundError as err:
                print('Error en archivo: {0}'.format(0))
            finally:
                fout.close()
    except OSError as err:
        print('Error: {0}'.format(err))
