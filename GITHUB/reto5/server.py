"""Programa principal que despliega el servicio REST que expone los metodos de DB"""
import json
from bson import json_util

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import basededatos
import empleados

APPOBJECT = Flask(__name__)
APIOBJECT = Api(APPOBJECT)
OBJMONGO = basededatos.DataBaseMongo()

class Employees(Resource):
    "Clase para procesamiento de metodos crud"
    def get(self):
        "Metodo que obtiene todos los registros de la DB"
        try:
            result = OBJMONGO.find_all()

            if result['status'] == 'ok':
                #response = {
                #    'status':'ok',
                #    'message':json.dumps(result['empleados'], indent=4, default=json_util.default)
                #}
                response = json.loads(json.dumps(result['empleados'], indent=4, default=json_util.default))
            else:
                response = {
                    'status':'error',
                    'message':result['message']
                }
        except Exception as err:
            response = {
                'status':'error',
                'message':'Error: ' + str(err)
            }
        return response

    def post(self):
        "Metodo para insercion en DB"
        empleado = empleados.Employee()

        try:
            objectjson = {
                'tipodocumento': request.json['tipodocumento'],
                'documento': request.json['documento'],
                'nombre': request.json['nombre'],
                'apellidos': request.json['apellidos'],
                'correo': request.json['correo'],
                'cargo': request.json['cargo'],
                'valorhora': request.json['valorhora'],
                'horastrabajadas': request.json['horastrabajadas']
            }
            empleado.setemployee(objectjson)
            result = OBJMONGO.insert(empleado.getemployee())

            if result['status'] == 'ok':
                response = {
                    'status':'ok',
                    'message':'Registro creado',
                    'body': {
                        'Id':result['Id']
                    }
                }
            else:
                response = {
                    'status':'error',
                    'message':result['message']
                }
        except Exception as err:
            response = {
                'status':'error',
                'message':'Error: ' + str(err)
            }
        return response

class EmployeeId(Resource):
    "Clase para procesamiento de metodos crud"
    def get(self, employee_id):
        "Metodo que obtiene todos los registros de la DB"
        try:
            result = OBJMONGO.find_id(employee_id)
            empleado = empleados.Employee()

            if result['status'] == 'ok':
                empleado.setemployee(result['empleado'])
                return empleado.getemployee()
            return result['message']

        except Exception as err:
            return 'Error: ' + str(err)

APIOBJECT.add_resource(EmployeeId, '/employees/<employee_id>')
APIOBJECT.add_resource(Employees, '/employees/')

if __name__ == '__main__':
    APPOBJECT.run(port='5002')
