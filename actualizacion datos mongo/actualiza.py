from pymongo import MongoClient
import pymongo
import time as ti

myclient = pymongo.MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")

mydb = myclient["integracion4"]
mycol = mydb["regiones"]

myquery = { "fecha_region": "2020-04-25" }
#newvalues = { "$set": { "Poblacion": "691854" ,"ID_region": "02"} }
newvalues = { "$set": { "N_recu_region": "0" } }

mydoc = mycol.find(myquery)
x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
##for x in mydoc:
##  print(x)
