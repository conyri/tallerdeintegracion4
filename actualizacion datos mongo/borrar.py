from pymongo import MongoClient
import pymongo



con = MongoClient('mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority')
db = con['integracion4']
collection = db['regiones']


deleteuser = {'N_region': "Total"}
resultado = collection.delete_many(deleteuser)
print ('Numero de documentos eliminados ' + str(resultado.deleted_count))
