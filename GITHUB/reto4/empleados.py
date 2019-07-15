"""Definicion de clase para procesamiento JSON de datos de empleado"""
from jsonschema import validate

SCHEMAEMPLOYEE = {
    "type": "object",
    "required": [
        "tipodocumento",
        "documento",
        "nombre",
        "apellidos"
    ],
    "properties": {
        "tipodocumento": {"type": "string"},
        "documento": {"type": "string"},
        "nombre": {"type": "string"},
        "apellidos": {"type": "string"},
        "cargo": {"type": "string"},
        "correo": {"type": "string"},
        "valorhora": {"type":"integer"},
        "horastrabajadas": {"type":"integer"},
        "salario": {"type":"integer"}
    }
}

class Employee(object):
    "clase para gestion de datos de empleado en objeto JSON"
    __objectemployee = {}

    def __init__(self):
        "Constructor clase"
        self.__objectemployee = {
            'tipodocumento': '',
            'documento': '',
            'nombre': '',
            'apellidos': '',
            'correo': '',
            'cargo': '',
            'valorhora': 0,
            'horastrabajadas': 0,
            'salario': 0
        }

#    def __init__(self, tipodocumento, documento, nombre, apellidos, correo, cargo):
#        self.__objectemployee = {
#            'tipodocumento': tipodocumento,
#            'documento': documento,
#            'nombre': nombre,
#            'apellidos': apellidos,
#            'correo': correo,
#            'cargo': cargo,
#            'valorhora': 0,
#            'horastrabajadas': 0,
#            'salario': 0
#        }

    def setdata(self, data, datainfo):
        "Metodo para carga o asignacion de datos de empleado por campo especifico"
        try:
            if data == 'valorhora' or data == 'horastrabajadas':
                self.__objectemployee[data] = int(datainfo)
            else:
                self.__objectemployee[data] = datainfo

            response = {
                'status', 'ok',
                'message', ''
            }
        except Exception as err:
            response = {
                'status', 'error',
                'message', str(err)
            }
        return response

    def setemployee(self, objjson):
        "Metodo para carga o asignacion de datos de empleado por JSON completo"
        try:
            validate(instance=objjson, schema=SCHEMAEMPLOYEE)
            self.__objectemployee = objjson
            respassig = self.assignsalary()

            if respassig['status'] == 'error':
                response = respassig
            else:
                response = {
                    'status': 'ok',
                    'message': ''
                }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def assignsalary(self):
        "Metodo para calculo de salario"
        try:
            self.__objectemployee['salario'] = self.__objectemployee['valorhora'] * self.__objectemployee['horastrabajadas']
            response = {
                'status', 'ok',
                'message', ''
            }
        except Exception as err:
            response = {
                'status', 'error',
                'message', str(err)
            }
        return response

    def getdata(self, data):
        "Metodo para retornar el valor de unn campo del objeto empleado"
        return self.__objectemployee[data]

    def getemployee(self):
        "Metodo para retornar la estructura JSON con los datos de empleado"
        return self.__objectemployee

