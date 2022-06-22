#Author: ADOB
#Date: 21/06/2022
#Version: 1.0

import sqlite3 as sql

def createDB(db):
	conn = sql.connect(db)

	#Save (commit) the changes
	conn.commit()

	#Close DB connection
	conn.close()

def createTable(table):
	conn = sql.connect("vegetables.db")
	cursor = conn.cursor()

	#Use f-string to insert var values in sql sentence
	inst = f"CREATE TABLE '{table}'(name text,price integer)"
	cursor.execute(inst)
	conn.commit()
	conn.close()

def insertRow(table, name, price):
	conn = sql.connect("vegetables.db")
	cursor = conn.cursor()
	inst = f"INSERT INTO '{table}' VALUES ('{name}', {price})"
	cursor.execute(inst)

if __name__ == "__main__":
	#Create DataBase using fuction
	#
	createDB("vegetables.db")
	
	#Create tables using fuction
	#
	createTable("hojas")
	createTable("tallos")
	createTable("bulbos")
	createTable("flores")
	createTable("vainas")
	createTable("tuberculos")
	createTable("frutos")
	createTable("raices")
	
	#Insert elements in tables
	#
	insertRow("hojas", "Espinaca", 500)
	insertRow("hojas", "Acelga", 2250)
	insertRow("hojas", "Repollo", 1800)
	insertRow("hojas", "Lechuga", 1600)

	insertRow("tallos", "Esparragos", 7800)
	insertRow("tallos", "Apio", 3400)

	insertRow("bulbos", "Cebolla", 2250)
	insertRow("bulbos", "Puerro", 3000)
	insertRow("bulbos", "Ajo", 7400)

	insertRow("flores", "Coliflor", 5650)
	insertRow("flores", "Brocoli", 2800)
	insertRow("flores", "Alcachofa", 5650)

	insertRow("vainas", "Alverja", 10800)
	insertRow("vainas", "Habas", 2250)

	insertRow("tuberculos", "Papa", 750)
	insertRow("tuberculos", "Batata", 11550)

	insertRow("frutos", "Tomate", 2800)
	insertRow("frutos", "Pimiento", 3500)
	insertRow("frutos", "Berenjena", 4000)
	insertRow("frutos", "Calabacin", 500)
	insertRow("frutos", "Pepino", 3950)
	insertRow("frutos", "Aguacate", 4800)

	insertRow("raices", "Zanahoria", 3900)
	insertRow("raices", "Nabo", 9000)
	insertRow("raices", "Remolacha", 2250)