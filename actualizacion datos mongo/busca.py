from pymongo import MongoClient
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")

mydb = myclient["integracion4"]
mycol = mydb["regiones"]

myquery = { 'N_region': "Arica y Parinacota" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
