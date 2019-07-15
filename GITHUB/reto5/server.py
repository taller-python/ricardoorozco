"""Clase encargada de desplegar el servicio REST para exponer los metodos de DB"""
import json
from bson import json_util
#from flask import Flask, request
from flask import Flask, jsonify
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from bson import ObjectId
#from flask import jsonify
import basededatos

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
                return json.dumps(result['empleados'], indent=4, default=json_util.default)
            return result['message']

        except Exception as err:
            return 'Error: ' + str(err)

class EmployeeId(Resource):
    "Clase para procesamiento de metodos crud"
    def get(self, employee_id):
        "Metodo que obtiene todos los registros de la DB"
        try:
            result = OBJMONGO.find_id(employee_id)

            if result['status'] == 'ok':
                employee = json.loads(json.dumps(result['empleado']))
                return jsonify(tipodocumento=employee['tipodocumento'])
            return result['message']

        except Exception as err:
            return 'Error: ' + str(err)

APIOBJECT.add_resource(EmployeeId, '/employees/<employee_id>')
APIOBJECT.add_resource(Employees, '/employees/')

if __name__ == '__main__':
    APPOBJECT.run(port='5002')
