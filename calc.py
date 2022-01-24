from distutils.log import ERROR
from msilib.schema import Error
from tkinter import *
from turtle import left

calculadora = Tk()
calculadora.title("Mi calculadora")
calculadora.geometry("650x410")
calculadora.config(bg="aqua")

Display = StringVar()

wid = 20
hei = 2

operador = " "

def click(b):
    global operador
    operador += str(b)
    Display.set(operador)

def Limpiar():
    global operador
    operador = ""
    Display.set(operador)  

def Resultados():
    global operador  
    try:
        r = str(eval(operador)) 
    except:
        r = "ERROR" 
    Display.set(r)        

Fr1 = Frame(calculadora, bd=15, pady=2, relief=RIDGE)
Fr1.grid()

Fr2 = Frame(Fr1, bd=15, pady=2, width=600, height=300, bg="aqua", relief=RIDGE)
Fr2.grid()

Fr3 = Frame(Fr1, bd=10, pady=2, width=600, height=300, bg="aqua", relief=RIDGE)
Fr3.grid()

Fr4 = Frame(Fr2, bd=10, pady=2, width=590, height=50, bg="aqua", relief=SUNKEN)
Fr4.grid(row=0, column=0)
Fr4_entry = Entry(Fr4, font=("Calibri", 17, 'bold'), textvariable=Display, width=47)
Fr4_entry.grid(row=0, column=0)

Fr5 = Frame(Fr2, bd=2, pady=2, width=590, height=50, bg="aqua", relief=RIDGE)
Fr5.grid(row=1, column=0)

lbl = Label(Fr5, font=('arial', 20, 'bold'), text="Bienvenidos a mi Calculadora", fg="black", bd=3)
lbl.grid(row=0, column=0, padx=30)

boton_7 = Button(Fr3, text = "7", width = wid, height = hei, command=lambda: click(7))
boton_8 = Button(Fr3, text = "8", width = wid, height = hei, command=lambda: click(8))
boton_9 = Button(Fr3, text = "9", width = wid, height = hei, command=lambda: click(9))
boton_4 = Button(Fr3, text = "4", width = wid, height = hei, command=lambda: click(4))
boton_5 = Button(Fr3, text = "5", width = wid, height = hei, command=lambda: click(5))
boton_6 = Button(Fr3, text = "6", width = wid, height = hei, command=lambda: click(6))
boton_1 = Button(Fr3, text = "1", width = wid, height = hei, command=lambda: click(1))
boton_2 = Button(Fr3, text = "2", width = wid, height = hei, command=lambda: click(2))
boton_3 = Button(Fr3, text = "3", width = wid, height = hei, command=lambda: click(3))
boton_punto = Button(Fr3, text = ".", width = wid, height = hei, command=lambda: click("."))
boton_0 = Button(Fr3, text = "0", width = wid, height = hei, command=lambda: click(0))
boton_result = Button(Fr3, text = "Resultado", width = wid, height = hei, command=lambda: Resultados())
boton_ac = Button(Fr3, text = "AC", width = wid, height = hei, command=lambda: Limpiar())
boton_suma = Button(Fr3, text = "+", width = wid, height = hei, command=lambda: click("+"))
boton_resta = Button(Fr3, text = "-", width = wid, height = hei, command=lambda: click("-"))
boton_mult = Button(Fr3, text = "*", width = wid, height = hei, command=lambda: click("*"))
boton_div = Button(Fr3, text = "/", width = wid, height = hei, command=lambda: click("/"))

boton_7.grid(row=2, column=0)
boton_8.grid(row=2, column=1)
boton_9.grid(row=2, column=2)

boton_4.grid(row=3, column=0)
boton_5.grid(row=3, column=1)
boton_6.grid(row=3, column=2)

boton_1.grid(row=4, column=0)
boton_2.grid(row=4, column=1)
boton_3.grid(row=4, column=2)

boton_punto.grid(row=5, column=0)
boton_0.grid(row=5, column=1)
boton_ac.grid(row=5, column=2)

boton_suma.grid(row=6, column=0)
boton_resta.grid(row=6, column=1)
boton_mult.grid(row=6, column=2)
boton_div.grid(row=6, column=3)

boton_result.grid(row=2, column=3, rowspan=4, sticky=N+S)



calculadora.mainloop()