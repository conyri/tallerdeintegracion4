import mysql.connector

dbConnect= {
    'host': 'localhost',
    'user':'root',
    'password':'',
    'database':'casos'
}
conexion = mysql.connector.connect(**dbConnect)

cursor = conexion.cursor()
#Insertar datos en la tabla regiones
sqlInsertar= 'insert into regiones ' 