"""Definicion de clase con conexion a base de datos Mongo"""
import pymongo
#import json
#from bson import json_util
from bson import ObjectId

class DataBaseMongo(object):
    "Clase con procedimiento de llamado a base de datos MongoDB"

    def __init__(self):
        "Metodo de inicializacion de clase"
        self.__tipodb = 'mongoDB'
        self.__rutamongo = 'mongodb://localhost:27017/'
        self.__nombredatabase = 'empleadosDB'
        self.__nombrecollection = 'empleadosCollect'
        self.__cliente = pymongo.MongoClient(self.__rutamongo)
        self.__database = self.__cliente[self.__nombredatabase]
        self.__collection = self.__database[self.__nombrecollection]

    def list_database_names(self):
        "Metodo que lista las DB creadas"
        return self.__cliente.list_database_names()

    def insert(self, objjson):
        "Metodo de insercion"
        try:
            objinsert = self.__collection.insert_one(objjson)
            response = {
                'status': 'ok',
                'message': '',
                'Id': str(objinsert.inserted_id)
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def find(self, objjson):
        "Metodo de busqueda a partir del tipo y documento"
        try:
            employee = self.__collection.find_one({'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']})

            response = {
                'status': 'ok',
                'message': '',
                'empleado': employee
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def find_id(self, employee_id):
        "Metodo de busqueda a partir del Id generado por Mongo"
        try:
            employee = self.__collection.find_one({'_id': ObjectId(employee_id)})

            response = {
                'status': 'ok',
                'message': '',
                'empleado': employee
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def find_all(self):
        "Metodo de busqueda - retorna todos los registros"
        try:
            consecutivo = 1
            employees = {}
            for objectx in self.__collection.find():
                employees[consecutivo] = objectx
                consecutivo += 1
                #print(json.dumps(x, indent=4, default=json_util.default))

            response = {
                'status': 'ok',
                'message': '',
                'empleados': employees
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def delete(self, objjson):
        "Metodo para borrado a partir del tipo y documento"
        try:
            self.__collection.delete_one({'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']})

            response = {
                'status': 'ok',
                'message': 'Empleado borrado - Tipo documento: ' + objjson['tipodocumento'] + ' - Documento: ' + objjson['documento']
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response

    def update(self, objjson):
        "Metodo para actualizacion a partir del tipo y documento"
        try:
            queryemployee = {'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']}
            updateemployee = {'$set': objjson}
            self.__collection.update_one(queryemployee, updateemployee)

            response = {
                'status': 'ok',
                'message': 'Empleado actualizado'
            }
        except pymongo.errors.PyMongoError as err:
            response = {
                'status': 'error',
                'message': str(err)
            }
        return response
