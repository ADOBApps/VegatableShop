# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Functions to manage Data base using class DBMan
@author: ADOB
"""

from Mycontrollers.db.db_man import DBMan

# Crea la base de datos de verduras por completo si no existe


db = DBMan()

# Create the store db
def createStore(_db):
	if (db.verifyDB(_db, "hojas")):
		print("Ok")
	else:
		db.createCategory("vegetables.db", "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Acelga", 2250, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Cilantro", 5000, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Diente de león", 5000, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Espinaca", 500, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Hinojo", 7000, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Orégano", 18150, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Perejil", 4500, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Lechuga", 1600, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Repollo", 1800, "hojas")
		db.insertVegetable("vegetables.db", "hojas", "Puerro", 3000, "hojas")

	if (db.verifyDB(_db,"v_semillas")):
		print("Ok")
	else:
		db.createCategory("vegetables.db", "v_semillas")
		db.insertVegetable("vegetables.db", "v_semillas", "Alverja", 10800, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Blanquillo", 5000, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Frijol Cargamanto", 8000, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Frijol Verde", 10780, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Frijol Caraota", 3140, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Garbanzo", 3790, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Habas", 2250, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Habichuelas", 6900, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Lenteja", 3000, "vainas")
		db.insertVegetable("vegetables.db", "v_semillas", "Soya", 2950, "vainas")

	if (db.verifyDB(_db, "frutos")):
		print("Ok")
	else:
		db.createCategory("vegetables.db", "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Ají", 2600, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Tomate", 2800, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Pimiento", 3500, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Berenjena", 4000, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Calabacin", 500, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Pepino", 3950, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Aguacate", 4800, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Mazorca", 3100, "frutos")
		db.insertVegetable("vegetables.db", "frutos", "Zapallo", 2300, "frutos")
	if (db.verifyDB(_db, "otras")):
		print("Ok")
	else:
		db.createCategory("vegetables.db", "otras")
		db.insertVegetable("vegetables.db", "otras", "Coliflor", 5650, "flores")
		db.insertVegetable("vegetables.db", "otras", "Brocoli", 2800, "flores")
		db.insertVegetable("vegetables.db", "otras", "Alcachofa", 5650, "flores")
		db.insertVegetable("vegetables.db", "otras", "Esparragos", 7800, "tallos")
		db.insertVegetable("vegetables.db", "otras", "Apio", 3400, "tallos")
		db.insertVegetable("vegetables.db", "otras", "Cebolla", 2250, "bulbos")
		db.insertVegetable("vegetables.db", "otras", "Puerro", 3000, "bulbos")
		db.insertVegetable("vegetables.db", "otras", "Ajo", 7400, "bulbos")
		db.insertVegetable("vegetables.db", "otras", "Papa", 750, "tuberculos")
		db.insertVegetable("vegetables.db", "otras", "Batata", 11550, "tuberculos")
		db.insertVegetable("vegetables.db", "otras", "Zanahoria", 3900, "raices")
		db.insertVegetable("vegetables.db", "otras", "Nabo", 9000, "raices")
		db.insertVegetable("vegetables.db", "otras", "Remolacha", 2250, "raices")

if __name__ == "__main__":
	createStore("vegetables.db")
