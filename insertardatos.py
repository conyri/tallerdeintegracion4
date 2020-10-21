import mysql.connector
#conectarse a la base de datos
dbConnect= {
    'host': 'localhost',
    'user':'root',
    'password':'',
    'database':'casos'
}
conexion = mysql.connector.connect(**dbConnect)

cursor = conexion.cursor()
#Insertar datos en la tabla regiones
sqlInsertar= "insert into regiones(ID_Region,Nombre_Reg,N_Hab_Reg,N_Contagiados_Reg,N_Recuperados_Reg,Fecha_Reg)values(%s,%s,%s,%s,%s,%s)" 

cursor.execute(sqlInsertar,('1','Aracunia','2','3','3','12'))
conexion.commit()
cursor.close()