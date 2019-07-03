from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
import json
from bson import ObjectId
from bson import json_util
from flask import jsonify
import basededatos

app = Flask(__name__)
api = Api(app)
objMongo = basededatos.DataBaseMongo()

class Employees(Resource):
    def get(self):
        try:
            result = objMongo.find_all()

            if result['status'] == 'ok':
                return json.dumps(result['empleados'], indent=4, default=json_util.default)
            else:
                return result['message']

        except Exception as err:
            return 'Error: ' + str(err)

class EmployeeId(Resource):
    def get(self, employee_id):
        try:
            result = objMongo.find_id(employee_id)

            if result['status'] == 'ok':
                employee = json.loads(json.dumps(result['empleado']))
                return jsonify(tipodocumento=employee['tipodocumento'])
            else:
                return result['message']

        except Exception as err:
            return 'Error: ' + str(err)

api.add_resource(EmployeeId, '/employees/<employee_id>')
api.add_resource(Employees, '/employees/')

if __name__ == '__main__':
    app.run(port='5002')