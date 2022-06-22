# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Functions to manage Data base using class DBMan
@author: ADOB
"""

from Mycontrollers.db.db_man import DBMan

if __name__ == "__main__":
	db = DBMan()
	#Create DataBase using fuction
	#
	db.createDB("vegetables.db")
	
	#Create tables using fuction
	#
	#db.createTable("vegetables.db", "hojas")
	#db.createTable("vegetables.db", "tallos")
	#db.createTable("vegetables.db", "bulbos")
	#db.createTable("vegetables.db", "flores")
	#db.createTable("vegetables.db", "vainas")
	#db.createTable("vegetables.db", "tuberculos")
	#db.createTable("vegetables.db", "frutos")
	#db.createTable("vegetables.db", "raices")
	
	#Insert elements in tables
	#
	#db.insertRow("vegetables.db", "hojas", "Espinaca", 500)
	#db.insertRow("vegetables.db", "hojas", "Acelga", 2250)
	#db.insertRow("vegetables.db", "hojas", "Repollo", 1800)
	#db.insertRow("vegetables.db", "hojas", "Lechuga", 1600)

	#db.insertRow("vegetables.db", "tallos", "Esparragos", 7800)
	#db.insertRow("vegetables.db", "tallos", "Apio", 3400)

	#db.insertRow("vegetables.db", "bulbos", "Cebolla", 2250)
	#db.insertRow("vegetables.db", "bulbos", "Puerro", 3000)
	#db.insertRow("vegetables.db", "bulbos", "Ajo", 7400)

	#db.insertRow("vegetables.db", "flores", "Coliflor", 5650)
	#db.insertRow("vegetables.db", "flores", "Brocoli", 2800)
	#db.insertRow("vegetables.db", "flores", "Alcachofa", 5650)

	#db.insertRow("vegetables.db", "vainas", "Alverja", 10800)
	#db.insertRow("vegetables.db", "vainas", "Habas", 2250)

	#db.insertRow("vegetables.db", "tuberculos", "Papa", 750)
	#db.insertRow("vegetables.db", "tuberculos", "Batata", 11550)

	#db.insertRow("vegetables.db", "frutos", "Tomate", 2800)
	#db.insertRow("vegetables.db", "frutos", "Pimiento", 3500)
	#db.insertRow("vegetables.db", "frutos", "Berenjena", 4000)
	#db.insertRow("vegetables.db", "frutos", "Calabacin", 500)
	#db.insertRow("vegetables.db", "frutos", "Pepino", 3950)
	#db.insertRow("vegetables.db", "frutos", "Aguacate", 4800)

	#db.insertRow("vegetables.db", "raices", "Zanahoria", 3900)
	#db.insertRow("vegetables.db", "raices", "Nabo", 9000)
	#db.insertRow("vegetables.db", "raices", "Remolacha", 2250)

	#myList = [("Zanahoria", 3900), ("Nabo", 9000), ("Remolacha", 2250)]
	
	#db.insertRows("vegetables.db", "raices", myList)

	#db.readOrdered("vegetables.db", "hojas", "price")
	
	#db.searchByLess("vegetables.db", "hojas", 2000)
	
	#db.updateDatum("vegetables.db", "raices", "Zanahoria", 3900)
	#db.readRows("vegetables.db", "raices")
	
	#db.insertRow("vegetables.db", "tuberculos", "Yuca", 3900)
	#db.readRows("vegetables.db", "tuberculos")
	
	#db.deleteRow("vegetables.db", "tuberculos", "Yuca")
	#db.readRows("vegetables.db", "tuberculos")

