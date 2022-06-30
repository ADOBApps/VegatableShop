# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Functions to manage Data base using class DBMan
@author: ADOB
"""

import tkinter as tk
import tkinter.ttk as ttk

from Mycontrollers.db.db_man import DBMan
from Myviews.gui.windows import Windows


# Crea la base de datos de verduras por completo si no existe

db = DBMan()

# Start Graphic User Interface (Windows module)
def launcher():
	root = tk.Tk()
	s_width = round(root.winfo_screenwidth()*0.80)
	s_height = round(root.winfo_screenheight()*0.80)
	root.geometry(f"{s_width}x{s_height}")
	root.title("Verdurería")

	window = Windows(root, db)
	window.uploadCategory(["hojas", "semillas", "frutos", "otras"])
	root.mainloop()

# Create the store db
def createStore(_db):
	if (db.verifyDB(_db, "hojas")):
		print("Ok")
	else:
		db.createCategory("hortalizas.db", "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Acelga", 2250, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Cilantro", 5000, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Diente de león", 5000, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Espinaca", 500, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Hinojo", 7000, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Orégano", 18150, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Perejil", 4500, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Lechuga", 1600, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Repollo", 1800, "hojas")
		db.insertVegetable("hortalizas.db", "hojas", "Puerro", 3000, "hojas")

	if (db.verifyDB(_db,"v_semillas")):
		print("Ok")
	else:
		db.createCategory("hortalizas.db", "v_semillas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Alverja", 10800, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Blanquillo", 5000, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Frijol Cargamanto", 8000, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Frijol Verde", 10780, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Frijol Caraota", 3140, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Garbanzo", 3790, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Habas", 2250, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Habichuelas", 6900, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Lenteja", 3000, "vainas")
		db.insertVegetable("hortalizas.db", "v_semillas", "Soya", 2950, "vainas")

	if (db.verifyDB(_db, "frutos")):
		print("Ok")
	else:
		db.createCategory("hortalizas.db", "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Ají", 2600, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Tomate", 2800, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Pimiento", 3500, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Berenjena", 4000, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Calabacin", 500, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Pepino", 3950, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Aguacate", 4800, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Mazorca", 3100, "frutos")
		db.insertVegetable("hortalizas.db", "frutos", "Zapallo", 2300, "frutos")

	if (db.verifyDB(_db, "otras")):
		print("Ok")
	else:
		db.createCategory("hortalizas.db", "otras")
		db.insertVegetable("hortalizas.db", "otras", "Coliflor", 5650, "flores")
		db.insertVegetable("hortalizas.db", "otras", "Brocoli", 2800, "flores")
		db.insertVegetable("hortalizas.db", "otras", "Alcachofa", 5650, "flores")
		db.insertVegetable("hortalizas.db", "otras", "Esparragos", 7800, "tallos")
		db.insertVegetable("hortalizas.db", "otras", "Apio", 3400, "tallos")
		db.insertVegetable("hortalizas.db", "otras", "Cebolla", 2250, "bulbos")
		db.insertVegetable("hortalizas.db", "otras", "Puerro", 3000, "bulbos")
		db.insertVegetable("hortalizas.db", "otras", "Ajo", 7400, "bulbos")
		db.insertVegetable("hortalizas.db", "otras", "Papa", 750, "tuberculos")
		db.insertVegetable("hortalizas.db", "otras", "Batata", 11550, "tuberculos")
		db.insertVegetable("hortalizas.db", "otras", "Zanahoria", 3900, "raices")
		db.insertVegetable("hortalizas.db", "otras", "Nabo", 9000, "raices")
		db.insertVegetable("hortalizas.db", "otras", "Remolacha", 2250, "raices")	

# Carrito
def createCarrito(_db):
	if (db.verifyDB(_db, "compras")):
		print("Carrito exists")
	else:
		db.createCategory(_db, "compras")
		print("Creating carrito")


if __name__ == "__main__":
	createStore("hortalizas.db")
	createCarrito("carrito.db")
	launcher()