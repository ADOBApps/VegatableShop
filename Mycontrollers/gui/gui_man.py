# _*_ coding: utf-8 _*_
"""
Created on 21/06/2022
	Funciones para administrar bases de datos
@author: ADOB
"""

from tkinter import *

def sel():
	selection = "You selected the option " + str(var.get())
	label.config(text = selection)

root = Tk()
root.geometry('300x500')
root.title("Fruver")



var = IntVar()

R1 = Radiobutton(root, text="hortalizas de hojas", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="hortalizas de semilla", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="hortalizas frutos", variable=var, value=3, command=sel)
R3.pack( anchor = W )

R4 = Radiobutton(root, text="otras hortalizas", variable=var, value=4, command=sel)
R4.pack( anchor = W )


label = Label(root)
label.pack()

root.mainloop()