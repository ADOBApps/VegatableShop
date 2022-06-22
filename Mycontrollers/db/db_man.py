# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Class to manage Data base
@author: ADOB
"""

import sqlite3 as sql

class DBMan:

	def __init__ (self):
		print("Calling constructor")

	def __del__ (self):
		class_name = self.__class__.__name__
		print(class_name, "destroyed")

	def createDB(self, db):
		conn = sql.connect(db)
		#Save (commit) the changes
		conn.commit()

		#Close DB connection
		conn.close()

	def createTable(self, db,table):
		conn = sql.connect(db)
		cursor = conn.cursor()

		#Use f-string to insert var values in sql sentence
		inst = f"CREATE TABLE '{table}'(name text,price integer)"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo crear la tabla '{table}'")

		conn.commit()
		conn.close()

	def insertRow(self, db, table, name, price):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES ('{name}', {price})"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")

		conn.commit()
		conn.close()

	def insertRows(self, db, table, myList):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"INSERT INTO '{table}' VALUES (?, ?)"
		try:
			cursor.executemany(inst, myList)
		except:
			print(f"No se pudo insertar el dato en la tabla '{table}'")
		conn.commit()
		conn.close()

	def readRows(self, db, table):
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

	#Read data ordered ascendent
	def readOrdered(self, db, table, field):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' ORDER BY {field}"

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

	def searchByName(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE name like '{item}'"

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

	def searchByLess(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"SELECT * FROM '{table}' WHERE price < {item}"

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

	#Update datum
	def updateDatum(self, db, table, item, price):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst = f"UPDATE '{table}' SET price={price} WHERE name='{item}'"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo modificar el valor de {item} de la tabla '{table}'")
		
		conn.commit()
		conn.close()

	#Delete datum
	def deleteRow(self, db, table, item):
		conn = sql.connect(db)
		cursor = conn.cursor()
		inst= f"DELETE FROM '{table}' WHERE name='{item}'"

		try:
			cursor.execute(inst)
		except:
			print(f"No se pudo borrar {item} de la tabla '{table}'")
		conn.commit()
		conn.close()