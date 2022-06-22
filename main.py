# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Funciones para administrar bases de datos
@author: ADOB
"""

import sqlite3 as sql

def createDB(db):
	conn = sql.connect(db)

	#Guardamos (commit) los cambios
	conn.commit()

	#Cerramos la conexión
	conn.close()

def createTable(db, table):
	conn = sql.connect(db)
	cursor = conn.cursor()

	#Usamos f-string insertar valores de variables en sentencia sql
	inst = f"CREATE TABLE '{table}'(name text,price integer)"
	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo crear la tabla: {table}")
	conn.commit()
	conn.close()

def insertRow(db, table, name, price):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"INSERT INTO '{table}' VALUES ('{name}', {price})"
	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo insertar el dato en la tabla '{table}'")
	conn.commit()
	conn.close()

def readRows(db, table):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT * FROM '{table}'"
	try:
		cursor.execute(inst)
		data = cursor.fetchall()
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
	conn.commit()
	conn.close()
	print(data)

	#Retorna una lista, los elementos de esta son tuplas
	return data

#Actualizar datos
def updateDatum(db, table, item, price):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"UPDATE '{table}' SET price={price} WHERE name='{item}'"

	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
		
	conn.commit()
	conn.close()

#Eliminar fila
def deleteRow(db, table, item):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst= f"DELETE FROM '{table}' WHERE name='{item}'"

	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo borrar {item} de la tabla '{table}'")
	conn.commit()
	conn.close()

if __name__ == "__main__":
	#Creamos la base de datos
	#
	createDB("vegetables.db")
	
	#Cremos las tablas
	#
	createTable("vegetables.db", "hojas")
	createTable("vegetables.db", "tallos")
	createTable("vegetables.db", "bulbos")
	createTable("vegetables.db", "flores")
	createTable("vegetables.db", "vainas")
	createTable("vegetables.db", "tuberculos")
	createTable("vegetables.db", "frutos")
	createTable("vegetables.db", "raices")
	
	#Insertamos valores en las tablas
	#
	insertRow("vegetables.db", "hojas", "Espinaca", 500)
	insertRow("vegetables.db", "hojas", "Acelga", 2250)
	insertRow("vegetables.db", "hojas", "Repollo", 1800)
	insertRow("vegetables.db", "hojas", "Lechuga", 1600)

	insertRow("vegetables.db", "tallos", "Esparragos", 7800)
	insertRow("vegetables.db", "tallos", "Apio", 3400)

	insertRow("vegetables.db", "bulbos", "Cebolla", 2250)
	insertRow("vegetables.db", "bulbos", "Puerro", 3000)
	insertRow("vegetables.db", "bulbos", "Ajo", 7400)

	insertRow("vegetables.db", "flores", "Coliflor", 5650)
	insertRow("vegetables.db", "flores", "Brocoli", 2800)
	insertRow("vegetables.db", "flores", "Alcachofa", 5650)

	insertRow("vegetables.db", "vainas", "Alverja", 10800)
	insertRow("vegetables.db", "vainas", "Habas", 2250)

	insertRow("vegetables.db", "tuberculos", "Papa", 750)
	insertRow("vegetables.db", "tuberculos", "Batata", 11550)

	insertRow("vegetables.db", "frutos", "Tomate", 2800)
	insertRow("vegetables.db", "frutos", "Pimiento", 3500)
	insertRow("vegetables.db", "frutos", "Berenjena", 4000)
	insertRow("vegetables.db", "frutos", "Calabacin", 500)
	insertRow("vegetables.db", "frutos", "Pepino", 3950)
	insertRow("vegetables.db", "frutos", "Aguacate", 4800)

	insertRow("vegetables.db", "raices", "Zanahoria", 3900)
	insertRow("vegetables.db", "raices", "Nabo", 9000)
	insertRow("vegetables.db", "raices", "Remolacha", 2250)

	readRows("vegetables.db", "raices")

	updateDatum("vegetables.db", "raices", "Zanahoria", 3900)

	insertRow("vegetables.db", "tuberculos", "Yuca", 3900)
	readRows("vegetables.db", "tuberculos")

	deleteRow("vegetables.db", "tuberculos", "Yuca")
	readRows("vegetables.db", "tuberculos")