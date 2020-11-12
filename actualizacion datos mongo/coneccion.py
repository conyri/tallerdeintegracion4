import pandas as pd
from pymongo import MongoClient
import pymongo
from numpy import array
from bson.objectid import ObjectId
from bs4 import BeautifulSoup

con = MongoClient('mongodb://programmer:RjCkUNuelX02EgAw@cluster0-shard-00-00-x5voi.mongodb.net:27017,cluster0-shard-00-01-x5voi.mongodb.net:27017,cluster0-shard-00-02-x5voi.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
db = con['integracion4']
collection = db['regiones']


fechas = array(['2020-03-03','2020-03-04','2020-03-05','2020-03-06','2020-03-07','2020-03-08'])
link = []



for i in fechas:
    link =['https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/'+i+'-CasosConfirmados-totalRegional.csv']
    for j in link :
        print ("link",link)
        #print ("fecha",i)
        df=pd.read_csv(j ,sep = ",")
        #df=pd.DataFrame(datos)
        #print(df.columns)
        #print(i,df['Region'][0:16],df[' Casos nuevos'][0:16],df[' Casos recuperados'][0:16])
        url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR.csv'
        dat=pd.read_csv(url)
##        print (i,df['Region'][0:16],df[' Casos nuevos'][0:16],df[' Casos recuperados'][0:16],dat['Poblacion'],dat['Region'])
        document = {'N_region':df['Region'][0:16], 'P_region':dat['Poblacion'],'N_cont_region':df[' Casos nuevos'][0:16], 'N_recu_region':df[' Casos recuperados'][0:16],'fecha_region':i,'Nun-region':dat['Codigo region']}
        _id = db ['regiones'].insert(document)
        print (_id)
    
