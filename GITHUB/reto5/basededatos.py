import pymongo
#import json
#from bson import json_util
from bson import ObjectId

class DataBaseMongo(object):
    def __init__(self):
        self.__tipodb = 'mongoDB'
        self.__rutamongo = 'mongodb://localhost:27017/'
        self.__nombredatabase = 'empleadosDB'
        self.__nombrecollection = 'empleadosCollect'
        self.__cliente = pymongo.MongoClient(self.__rutamongo)
        self.__database = self.__cliente[self.__nombredatabase]
        self.__collection = self.__database[self.__nombrecollection]

    def list_database_names(self):
        return self.__cliente.list_database_names()

    def insert(self, objjson):
        try:
            objinsert = self.__collection.insert_one(objjson)
            response = {
                'status': 'ok',
                'message': '',
                'Id': str(objinsert.inserted_id)
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response

    def find(self, objjson):
        try:
            employee = self.__collection.find_one({'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']})

            response = {
                'status': 'ok',
                'message': '',
                'empleado': employee
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response

    def find_id(self, employee_id):
        try:
            employee = self.__collection.find_one({'_id': ObjectId(employee_id)})

            response = {
                'status': 'ok',
                'message': '',
                'empleado': employee
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response

    def find_all(self):
        try:
            consecutivo = 1
            employees = {}
            for x in self.__collection.find():
                employees[consecutivo] = x
                consecutivo += 1
                #print(json.dumps(x, indent=4, default=json_util.default))

            response = {
                'status': 'ok',
                'message': '',
                'empleados': employees
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response

    def delete(self, objjson):
        try:
            self.__collection.delete_one({'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']})

            response = {
                'status': 'ok',
                'message': 'Empleado borrado - Tipo documento: ' + objjson['tipodocumento'] + ' - Documento: ' + objjson['documento']
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response

    def update(self, objjson):
        try:
            queryemployee = {'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']}
            updateemployee = {'$set': objjson}
            self.__collection.update_one(queryemployee, updateemployee)

            response = {
                'status': 'ok',
                'message': 'Empleado actualizado'
            }
        except Exception as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        finally:
            return response