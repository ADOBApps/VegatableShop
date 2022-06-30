# _*_ coding: utf-8 _*_
"""
Created on 24/06/2022
	Clase encargada de admninistrar los gráficos de la app
	Emplea Notebooks de ttk, Listbox, Frames, Label, LabelFrames
	y combox al igual que otras herramientas de Tkinter
@author: ADOB
"""

import tkinter as tk
from tkinter import Button
from tkinter import Listbox
from tkinter import messagebox as mb
import tkinter.ttk as ttk

class Windows:
	#Starting function
	def __init__ (self, master, db_):
		print("Calling constructor")
		
		# Tk object instance
		self.master = master

		# Access to DB
		self.db = db_

		# Screen's size
		self.s_width = master.winfo_screenwidth()
		self.s_height = master.winfo_screenheight()
		self.n_width = round(self.s_width*0.80)
		self.n_height = round(self.s_height*0.80)
		self.lf_width = round(self.s_width*0.60)
		self.lf_height = round(self.s_height*0.60)
		self.notebook = ttk.Notebook(self.master, width=self.n_width, height=self.n_height)

		# labelvar 1 and 2
		self.labelvar1 = tk.StringVar()
		self.labelvar1.set("Common text")

		self.labelvar2 = tk.StringVar()
		self.labelvar2.set("Factura")

		# Create temp and recursive list and strings
		self.list_elements = []
		self.list_elements1 = []
		self.carrito_elements = []
		self.temp_element=""
		self.temp_element1=""
		self.temp_table=""
		self.value=0
		self.value1=0

		# Create a carrito tap
		self.uploadCheck()

		# Organize notebook
		self.notebook.pack()

	# Finish program
	def __del__ (self):
		class_name = self.__class__.__name__
		self.list_elements = []
		self.list_elements1 = []
		self.carrito_elements = []
		self.temp_element=""
		self.temp_element1=""
		self.temp_table=""
		self.value=0
		self.value1=0
		print(class_name, "destroyed")

	# Set category vegetables to show
	def setCategory(self):
		self.listbox1.delete(0, tk.END)
		if (self.Combo.get() == "Escoja una opción"):
			mb.showerror("Escoja", "Seleccione una opción válida por favor")
		else:
			if (self.Combo.get() == "semillas"):
				self.list_elements = self.db.getVegetables("hortalizas.db", "v_semillas")
			else:
				self.list_elements = self.db.readRows("hortalizas.db", self.Combo.get())
			for r in self.list_elements:
				print(f"{r[0]} precio por libra: ${r[1]}")
				self.temp_element = r[0]
				self.listbox1.insert(tk.END, f"{r[0]} precio por libra: ${r[1]}")

	# Get selected item and its price
	def selectedItem(self):
		if self.listbox1.curselection():
			for i in self.listbox1.curselection():
				for r in self.list_elements:
					if (f"{r[0]}" in self.listbox1.get(i)):
						if self.Combo.get() == "semillas":
							self.temp_table="v_semillas"
						else:
							self.temp_table=self.Combo.get()
						self.value1 = self.db.getByName("hortalizas.db", f"{self.temp_table}", f"{r[0]}")
						print(f"LO ENCONTRÉ Y SU PRECIO ES: $ {self.value1[0][1]}")
						self.notebook.select(self.frame2)
						#Confirm and generate the check
						self.checked(r, f"{self.value1[0][1]}")
		else:
			mb.showinfo("Infor", "Sleccione un producto")

	# Create and organize for firts win
	def uploadCategory(self, _list):
		self.frame1 = ttk.Frame(self.notebook)
		self.frame1.pack(fill=tk.BOTH, expand=True)
		self.notebook.add(self.frame1, text = "Categorías")
		self.labelframe1 = ttk.LabelFrame(self.frame1, text="Categorías")
		self.labelframe1.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)
		label1 = ttk.Label(self.labelframe1, textvariable=self.labelvar1)
		self.labelvar1.set("Categorías")
		label1.pack(pady=50, padx=20)

		self.notebook.select(self.frame1)

		self.vlist = _list
		self.Combo = ttk.Combobox(self.labelframe1, values = self.vlist)
		self.Combo.set("Escoja una opción")
		self.Combo.pack(padx=5, pady=5)

		self.button1 = Button(self.labelframe1, text = "Aceptar", command=self.setCategory)
		self.button1.pack(padx=5, pady=5, side="right")

		self.button2 = Button(self.labelframe1, text = "Comprar", command=self.selectedItem)
		self.button2.pack(padx=5, pady=5, side="right")

		self.listbox1 = Listbox(self.labelframe1)
		self.listbox1.pack(fill=tk.BOTH, expand=True)

	# Get selected item and its price
	def carritoItem(self):
		self.carrito_elements = self.db.readRows("carrito.db", "compras")
		if self.carrito_elements:
			mb.showinfo("Bienvenido", "Su carrito contiene productos")
			for r in self.carrito_elements:
				print(f"{r[0]} precio por libra: ${r[1]}")
				self.temp_element1 = r[0]
				self.listbox2.insert(tk.END, f"{r[0]} precio por libra: ${r[1]}")
			if self.getPrice():
				self.labelvar2.set(f"El valor de factura es: ${self.getPrice()}")
		else:
			print("Carrito vacío")

	# Deleted products
	def deleteItem(self):
		if self.listbox2.curselection():
			for i in self.listbox2.curselection():
				for r in self.carrito_elements:
					if (f"{r[0]}" in self.listbox2.get(i)):
						if self.db.verifyDatum("carrito.db", "compras", f"{r[0]}") and self.db.deleteRow("carrito.db", "compras", f"{r[0]}"):
							self.listbox2.delete(i)
							mb.showinfo("Hecho", f"se eliminó {self.listbox2.get(i)}")
							break
						else:
							mb.showerror("Error eliminando ", f"{self.listbox2.get(i)}")
		else:
			mb.showinfo("Infor", "Seleccione un producto")
		if self.getPrice():
			self.labelvar2.set(f"El valor de factura es: ${self.getPrice()}")

	# Calculate cumulate value
	def getPrice(self):
		mycarrito_elements = self.db.readRows("carrito.db", "compras")
		if mycarrito_elements:
			self.value1 = 0
			for r in mycarrito_elements:
				print(f"This error {r[1]}")
				self.value1 = int(self.value1) + r[1]
			return self.value1
		else:
			print("Carrito vacío")
			return self.value1

	# Action function of button4
	def shop(self):
		self.notebook.select(self.frame1)

	# Action fuction of button 5
	def unshop(self):
		if self.listbox2.curselection():
			self.deleteItem()
		else:
			mb.showerror("Precaución", "Debe seleccionar el producto que desea remover")

	# Create "carrito" tab
	def uploadCheck(self):
		self.frame2 = ttk.Frame(self.notebook)
		self.notebook.add(self.frame2, text="Carrito")

		self.labelframe2 = ttk.LabelFrame(self.frame2, text="Sus compras")
		self.labelframe2.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

		self.label2 = ttk.Label(self.labelframe2, textvariable=self.labelvar2)
		self.label2.pack(pady = 50, padx = 20)

		self.button3 = Button(self.labelframe2, text = "Finalizar", command=self._bye)
		self.button3.pack(padx = 5, pady = 5, side="right")

		self.button4 = Button(self.labelframe2, text = "Añadir", command=self.shop)
		self.button4.pack(padx = 5, pady = 5, side="right")

		self.button5 = Button(self.labelframe2, text = "Eliminar", command=self.unshop)
		self.button5.pack(padx = 5, pady = 5, side="right")

		self.listbox2 = Listbox(self.labelframe2)
		self.listbox2.pack(fill=tk.BOTH, expand=True)

		self.carritoItem()	

	# Quit
	def _bye(self):
		mb.showinfo("Bye", "Gracias por preferirnos")
		self.master.destroy()

	# To buy
	def checked(self, r, value):
		self.value = self.getPrice() + int(value)
		self.labelvar2.set(f"El valor de factura es: ${self.value}")
		if self.db.insertProduct("carrito.db", "compras", f"{r[0]}", int(value), "compra"):
			print("producto insertado en el carrito")
		else:
			print("Error al insertar el producto")
		self.listbox2.insert(tk.END, f"{r[0]} precio por libra: ${r[1]}")
		