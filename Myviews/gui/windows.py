# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Funciones para administrar bases de datos
@author: ADOB
"""

import tkinter as tk
from tkinter import Button
from tkinter import Listbox
import tkinter.ttk as ttk


class Windows:
	def __init__ (self, master, db_):
		print("Calling constructor")
		
		self.master = master

		# Acces to DB
		self.db = db_

		# Screen's size
		self.s_width = master.winfo_screenwidth()
		self.s_height = master.winfo_screenheight()
		self.n_width = round(self.s_width*0.80)
		self.n_height = round(self.s_height*0.80)
		self.lf_width = round(self.s_width*0.60)
		self.lf_height = round(self.s_height*0.60)
		self.notebook = ttk.Notebook(self.master, width=self.n_width, height=self.n_height)

		#
		

		# Frame 1 and 2
		self.labelvar1 = tk.StringVar()
		self.labelvar1.set("Common text")

		self.labelvar2 = tk.StringVar()
		self.labelvar2.set("Common text")

		self.uploadCheck()

		self.list_elements = []
		self.temp_element=""
		self.temp_table=""
		self.value=0

		self.notebook.pack()


	def __del__ (self):
		class_name = self.__class__.__name__
		self.temp_element =""
		print(class_name, "destroyed")

	# Set category vegetables to show
	def setCategory(self):
		self.listbox1.delete(0, tk.END)
		if (self.Combo.get() == "Pick an Option"):
			self.labelvar1.set("Seleccione una opción válida")
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
					#self.listbox2.insert(tk.END, f"{r[0]} precio por libra: ${r[1]}")
					self.checked(r, f"{self.value1[0][1]}")


	# Create and organize for firts win
	def uploadCategory(self, _list):
		self.frame1 = ttk.Frame(self.notebook)
		self.frame1.pack(fill=tk.BOTH, expand=True)
		self.notebook.add(self.frame1, text = "Categorias")
		self.labelframe1 = ttk.LabelFrame(self.frame1, text="Categorias")
		self.labelframe1.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)
		label1 = ttk.Label(self.labelframe1, textvariable=self.labelvar1)
		self.labelvar1.set("Categorias")
		label1.pack(pady = 50, padx = 20)

		self.notebook.select(self.frame1)

		self.vlist = _list
		self.Combo = ttk.Combobox(self.labelframe1, values = self.vlist)
		self.Combo.set("Pick an Option")
		self.Combo.pack(padx = 5, pady = 5)

		self.button1 = Button(self.labelframe1, text = "Submit", command=self.setCategory)
		self.button1.pack(padx = 5, pady = 5)

		self.button2 = Button(self.labelframe1, text = "Comprar", command=self.selectedItem)
		self.button2.pack(padx = 5, pady = 5)

		self.listbox1 = Listbox(self.labelframe1)
		self.listbox1.pack(fill=tk.BOTH, expand=True)

	
	#
	def shop(self):
		self.notebook.select(self.frame1)
	#
	def uploadCheck(self):
		self.frame2 = ttk.Frame(self.notebook)
		self.notebook.add(self.frame2, text="Carrito")

		self.labelframe2 = ttk.LabelFrame(self.frame2, text="Gracias por preferirnos")
		self.labelframe2.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)
		self.label2 = ttk.Label(self.labelframe2, textvariable=self.labelvar2)
		
		self.label2.pack(pady = 50, padx = 20)

		self.listbox2 = Listbox(self.labelframe2)
		self.listbox2.pack(fill=tk.BOTH, expand=True)

		self.button3 = Button(self.labelframe2, text = "Final", command=self._bye)
		self.button3.pack(padx = 5, pady = 5)

		self.button4 = Button(self.labelframe2, text = "Seguir Comprando", command=self.shop)
		self.button4.pack(padx = 5, pady = 5)

	#
	def _bye(self):
		self.master.destroy()

	#
	def checked(self, r, value):
		self.value = int(value) + int(self.value)
		self.labelvar2.set(f"El valor de factura es: ${self.value}")
		self.listbox2.insert(tk.END, f"{r[0]} precio por libra: ${r[1]}")
		

		
		
