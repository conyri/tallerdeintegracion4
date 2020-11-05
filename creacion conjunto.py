from numpy import array
import csv
import urllib.request
from io import StringIO
import mysql.connector


dbConnect= {
    'host': 'localhost',
    'user':'root',
    'password':'',
    'database':'casos'
}
conexion = mysql.connector.connect(**dbConnect)
cursor = conexion.cursor()

fechas = array(['2020-03-03','2020-03-04','2020-03-05','2020-03-06','2020-03-07','2020-03-08'])
link = []
sqlInsertar= "insert IGNORE into regiones(Nombre_Reg,N_Contagiados_Reg,Fecha_Reg)values(%s,%s,%s)"
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
            print(i+"\t"+ filas[0]+"\t"+filas[1])
            cursor.execute(sqlInsertar,('filas[0]','filas[1]','i'))
            conexion.commit()
            cursor.close()
            

