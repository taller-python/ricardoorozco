"""Definicion de clase con conexion a base de datos Mongo"""
import pymongo

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
            for objectx in self.__collection.find({'tipodocumento': objjson['tipodocumento'], 'documento': objjson['documento']}):
                employee = objectx

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
