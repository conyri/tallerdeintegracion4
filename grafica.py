from pymongo import MongoClient
import pymongo
import time as ti
import numpy as np
import random
import matplotlib.pyplot as plt


myclient = pymongo.MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")

mydb = myclient["integracion4"]
mycol = mydb["regiones"]

def region(nombre):
  mydoc = mycol.find(
  {"N_region": nombre},
  {"N_cont_region":1,"_id":0}
  )
  x = []
  y = []
  cont = 0
  for i in mydoc:
    y.append(int(float(i["N_cont_region"])))
    cont = cont + 1
    x.append(cont)

  plt.scatter(x,y)
  plt.title(nombre)
  plt.xlabel('Dias')
  plt.ylabel('Nuevos contagios')
  plt.show()

nombre = str(input("Ingrese nombre de Region: "))
region(nombre)
















