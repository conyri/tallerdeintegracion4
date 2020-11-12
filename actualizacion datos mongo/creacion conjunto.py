from numpy import array
import csv
import pymongo
import urllib.request
from io import StringIO
import pymysql 
from pymongo import MongoClient

con = MongoClient('mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority')
db = con['integracion4']
#collection = db['pruebas']

fechas = array(['2020-11-01','2020-11-02','2020-11-03','2020-11-04','2020-11-05'])
link = []
otros =[]
otros2 =[]
##print(len(fechas))
for i in fechas:
    link =['https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/'+i+'-CasosConfirmados-totalRegional.csv']
    for j in link :
        print ("link",link)
        #print ("fecha",i)
        respuesta = urllib.request.urlopen(j)
        f = StringIO(bytearray(respuesta.read()).decode())
        archivo = csv.reader(f)    
        for filas in archivo:
            document= {'N_region':filas[0],'N_cont_region':filas[2],'N_recu_region':filas[8],'fecha_region':i}
            _id = db['pruebas'].insert(document)
            print (_id)






