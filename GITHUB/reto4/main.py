import basededatos
import empleados
import json
from bson import json_util

def main():
    menu = 0
    objMongo = basededatos.DataBaseMongo()
    empleado = empleados.Employee()

    while menu != 5:
        print('Consola de digitalizacion de empleados - Empresa Pepito Perez')
        print('Menu de opciones')
        menu = int(input('Digite [1: Nuevo empleado, 2: Seleccionar empleado, 3: Modificar empleado, 4: Borrar empleado, 5: Salir]: '))

        if menu == 1:
            try:
                result = empleado.setdata('tipodocumento', input('Tipo Documento: '))
                result = empleado.setdata('documento', input('Documento: '))
                result = empleado.setdata('nombre', input('Nombre: '))
                result = empleado.setdata('apellidos', input('Apellidos: '))
                result = empleado.setdata('correo', input('Correo: '))
                result = empleado.setdata('cargo', input('Cargo: '))
                result = empleado.setdata('horastrabajadas', int(input('Horas trabajadas: ')))
                result = empleado.setdata('valorhora', int(input('Valor hora: ')))
                empleado.assignsalary()

                result = objMongo.insert(empleado.getemployee())
                if result['status'] == 'ok':
                    print('Empledo creado - Id: ' + result['Id'])
                else:
                    print(result['message'])
            except Exception as err:
                print('Error: ' + str(err))
        elif menu == 2:
            try:
                result = empleado.setdata('tipodocumento', input('Tipo Documento: '))
                result = empleado.setdata('documento', input('Documento: '))
                result = objMongo.find(empleado.getemployee())

                if result['status'] == 'ok':
                    print(json.dumps(result['empleado'], indent=4, default=json_util.default))
                else:
                    print(result['message'])

            except Exception as err:
                print('Error: ' + str(err))
        elif menu == 4:
            try:
                result = empleado.setdata('tipodocumento', input('Tipo Documento: '))
                result = empleado.setdata('documento', input('Documento: '))
                result = objMongo.delete(empleado.getemployee())

                if result['status'] == 'ok':
                    print(result['message'])
                else:
                    print(result['message'])

            except Exception as err:
                print('Error: ' + str(err))
        elif menu == 3:
            try:
                result = empleado.setdata('tipodocumento', input('Tipo Documento: '))
                result = empleado.setdata('documento', input('Documento: '))
                result = empleado.setdata('nombre', input('Nombre: '))
                result = empleado.setdata('apellidos', input('Apellidos: '))
                result = empleado.setdata('correo', input('Correo: '))
                result = empleado.setdata('cargo', input('Cargo: '))
                result = empleado.setdata('horastrabajadas', int(input('Horas trabajadas: ')))
                result = empleado.setdata('valorhora', int(input('Valor hora: ')))
                empleado.assignsalary()

                result = objMongo.update(empleado.getemployee())

                if result['status'] == 'ok':
                    print(result['message'])
                else:
                    print(result['message'])

            except Exception as err:
                print('Error: ' + str(err))
        else:
            print('Programa Finalizado')
            break

main()