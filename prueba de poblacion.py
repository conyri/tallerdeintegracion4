import csv
import urllib.request
from io import StringIO

url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR.csv'
respuesta = urllib.request.urlopen(url)
f = StringIO(bytearray(respuesta.read()).decode())
archivo = csv.reader(f)

for filas in archivo:
    print(filas[0]+"\t" +filas[1]+"\t" +filas[2])

