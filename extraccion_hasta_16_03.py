from numpy import array


import csv
import urllib.request
from io import StringIO

fechas = array(['2020-03-03','2020-03-04','2020-03-05','2020-03-06','2020-03-07','2020-03-08','2020-03-09','2020-03-10','2020-03-11','2020-03-12','2020-03-13','2020-03-14','2020-03-15'
                ,'2020-03-16','2020-03-17','2020-03-18','2020-03-19','2020-03-20','2020-03-21','2020-03-22','2020-03-23','2020-03-24','2020-03-25','2020-03-26','2020-03-27'
                ,'2020-03-28','2020-03-29','2020-03-30','2020-03-31','2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05','2020-04-06','2020-04-07','2020-04-08','2020-04-09'
                ,'2020-04-10','2020-04-11','2020-04-12','2020-04-13','2020-04-14','2020-04-15'])
link = []

##print(len(fechas))
for i in fechas:
    link.append('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/'+i+'-CasosConfirmados-totalRegional.csv')

##print (link)

for j in link :
        respuesta = urllib.request.urlopen(j)
        f = StringIO(bytearray(respuesta.read()).decode())
        archivo = csv.reader(f)
        for filas in archivo:
            print(filas[0]+"\t"+filas[1])
               


           
