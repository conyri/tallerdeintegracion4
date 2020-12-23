from pymongo import MongoClient
import pymongo
import time as ti
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import streamlit as st
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import pandas as pd

st.title("Detecccion del Covid en Chile")


myclient = pymongo.MongoClient("mongodb+srv://constanza:constanza@cluster0.getl7.mongodb.net/integracion4?retryWrites=true&w=majority")
query={}

mydb = myclient["integracion4"]
mycol = mydb["regiones"]
cursor = mydb['regiones'].find(query)
df =  pd.DataFrame(list(cursor))
no_id=True

if no_id and '_id' in df:
        del df['_id']

df.to_csv('1.csv', index=False)
Reg=('Coquimbo','Arica y Parinacota')
Regiones = list(range(len(Reg)))
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
  x1 = np.array(x).reshape(-1, 1)
  y1 = np.array(y).reshape(-1, 1)
  x_train, x_test, y_train, y_test = train_test_split(x1, y1,
                                                      test_size=0.2,
                                                      train_size=0.8,
                                                      shuffle=True) 
  linreg = LinearRegression()
  linreg.fit(x_train,y_train)
  ypredict = linreg.predict(x_test)

  # Error Cuadrado Medio
  rmse = np.sqrt(mean_squared_error(ypredict, y_test))
  print ('Error cuadrado medio: \n',rmse)

  aPred = []
  aX = []
  for i in range(0,355):
    pred = linreg.predict([[i]])
    aPred.append(int(pred))
    aX.append(i)
  fig = plt.figure()
  plt.plot(aX,aPred,color="red")
  plt.scatter(x,y)
  plt.title(nombre)
  plt.xlabel('Dias')
  plt.ylabel('Nuevos contagios')
  plt.show()
  st.pyplot()
nombre = st.sidebar.selectbox('Selecciona una region', ('Coquimbo','Arica y Parinacota',('Tarapacá'),('Antofagasta'),('Atacama'),('Valparaíso'),('Metropolitana'),('O’Higgins'),('Ñuble'),('Biobío'),('Araucanía'),('Los Ríos'),('Los Lagos'),('Aysén'),('Magallanes')) ,)
region(nombre)
def load_data():
   data = pd.read_csv('1.csv')
   return data
data = load_data()
if st.checkbox('Mostrar datos'):
   data


