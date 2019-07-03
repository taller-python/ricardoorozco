from jsonschema import validate

schemaemployee = {
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
    __objectemployee = {}

    def __init__(self):
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
        finally:
            return response

    def setemployee(self, objjson):
        try:
            validate(instance = objjson, schema = schemaemployee)
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
        finally:
            return response

    def assignsalary(self):
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
        finally:
            return response

    def getdata(self, data):
        return self.__objectemployee[data]

    def getemployee(self):
        return self.__objectemployee

