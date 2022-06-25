# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Funciones para administrar bases de datos
@author: ADOB
"""

import sqlite3 as sql

#Crea la base de datos
def createDB(db):
	conn = sql.connect(db)

	#Guardamos (commit) los cambios
	conn.commit()

	#Cerramos la conexión
	conn.close()

#Crea categorías de hortalizas
def createCategory(db, table):
	conn = sql.connect(db)
	cursor = conn.cursor()

	#Usamos f-string insertar valores de variables en sentencia sql
	inst = f"CREATE TABLE '{table}'(name text, price integer, mytype text)"
	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo crear la tabla: {table}")
	conn.commit()
	conn.close()

#Inserta hortalizas
def insertVegetable(db, table, name, price, mytype):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"INSERT INTO '{table}' VALUES ('{name}', {price}, '{mytype}')"
	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo insertar el dato en la tabla '{table}'")
	conn.commit()
	conn.close()

#Lee los datos de un producto
def getVegetables(db, table):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT * FROM '{table}'"
	try:
		cursor.execute(inst)
		data = cursor.fetchall()
		for r in data:
			print(r)
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
	conn.commit()
	conn.close()

	#Retorna una lista, los elementos de esta son tuplas
	return data

#Obtener vegetales por subcategoría o tipo
def getByType(db, table, mytype):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT * FROM '{table}' WHERE mytype='{mytype}'"
	try:
		cursor.execute(inst)
		data = cursor.fetchall()
		for r in data:
			print(r)
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
	conn.commit()
	conn.close()

	#Retorna una lista, los elementos de esta son tuplas
	return data

#Obtener datos de un solo producto
def getByName(db, table, name):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT * FROM '{table}' WHERE name='{name}'"
	try:
		cursor.execute(inst)
		data = cursor.fetchall()
		for r in data:
			print(r)
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
	conn.commit()
	conn.close()

	#Retorna una lista, los elementos de esta son tuplas
	return data

#Actualizar datos de un producto
def updatePrice(db, table, item, price):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"UPDATE '{table}' SET price={price} WHERE name='{item}'"

	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo leer los datos de la tabla '{table}'")
		
	conn.commit()
	conn.close()

#Obtener precio


#Eliminar producto (fila)
def deleteVegetable(db, table, item):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst= f"DELETE FROM '{table}' WHERE name='{item}'"

	try:
		cursor.execute(inst)
	except:
		print(f"No se pudo borrar {item} de la tabla '{table}'")
	conn.commit()
	conn.close()

#Verifica existencia de tablas
def verifyDB(db, table):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
	try:
		listOfTables = cursor.execute(inst).fetchall()
		if listOfTables == []:
			return False
		else:
			print("Exists")
			return True
	except:
		print("Fatal error")
	conn.commit()
	conn.close()

#Verifica la existencia de un elemento
def verifyDatum(db, table, element):
	conn = sql.connect(db)
	cursor = conn.cursor()
	inst = f"SELECT * FROM '{table}' WHERE name='{element}'"
	try:
		listOfElements = cursor.execute(inst).fetchall()
		if listOfElements:
			print("Exists")
			return True
		else:
			print("No found")
			return False
	except:
		print("Fatal error")
	conn.commit()
	conn.close()

# Crea la base de datos de verduras por completo si no existe
def createStore(db):
	if (verifyDB(db, "hojas")):
		print("Ok")
	else:
		createCategory("hortalizas.db", "hojas")
		insertVegetable("hortalizas.db", "hojas", "Acelga", 2250, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Cilantro", 5000, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Diente de león", 5000, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Espinaca", 500, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Hinojo", 7000, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Orégano", 18150, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Perejil", 4500, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Lechuga", 1600, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Repollo", 1800, "hojas")
		insertVegetable("hortalizas.db", "hojas", "Puerro", 3000, "hojas")

	if (verifyDB(db,"v_semillas")):
		print("Ok")
	else:
		createCategory("hortalizas.db", "v_semillas")
		insertVegetable("hortalizas.db", "v_semillas", "Alverja", 10800, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Blanquillo", 5000, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Frijol Cargamanto", 8000, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Frijol Verde", 10780, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Frijol Caraota", 3140, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Garbanzo", 3790, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Habas", 2250, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Habichuelas", 6900, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Lenteja", 3000, "vainas")
		insertVegetable("hortalizas.db", "v_semillas", "Soya", 2950, "vainas")

	if (verifyDB(db, "frutos")):
		print("Ok")
	else:
		createCategory("hortalizas.db", "frutos")
		insertVegetable("hortalizas.db", "frutos", "Ají", 2600, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Tomate", 2800, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Pimiento", 3500, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Berenjena", 4000, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Calabacin", 500, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Pepino", 3950, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Aguacate", 4800, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Mazorca", 3100, "frutos")
		insertVegetable("hortalizas.db", "frutos", "Zapallo", 2300, "frutos")
	if (verifyDB(db, "otras")):
		print("Ok")
	else:
		createCategory("hortalizas.db", "otras")
		insertVegetable("hortalizas.db", "otras", "Coliflor", 5650, "flores")
		insertVegetable("hortalizas.db", "otras", "Brocoli", 2800, "flores")
		insertVegetable("hortalizas.db", "otras", "Alcachofa", 5650, "flores")
		insertVegetable("hortalizas.db", "otras", "Esparragos", 7800, "tallos")
		insertVegetable("hortalizas.db", "otras", "Apio", 3400, "tallos")
		insertVegetable("hortalizas.db", "otras", "Cebolla", 2250, "bulbos")
		insertVegetable("hortalizas.db", "otras", "Puerro", 3000, "bulbos")
		insertVegetable("hortalizas.db", "otras", "Ajo", 7400, "bulbos")
		insertVegetable("hortalizas.db", "otras", "Papa", 750, "tuberculos")
		insertVegetable("hortalizas.db", "otras", "Batata", 11550, "tuberculos")
		insertVegetable("hortalizas.db", "otras", "Zanahoria", 3900, "raices")
		insertVegetable("hortalizas.db", "otras", "Nabo", 9000, "raices")
		insertVegetable("hortalizas.db", "otras", "Remolacha", 2250, "raices")

if __name__ == "__main__":

	#Creamos la base de datos
	#
	createStore("hortalizas.db")
	getByType("hortalizas.db", "otras", "tuberculos")




