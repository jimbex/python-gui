from tkinter import *
import math

jimbex = Tk()

jimbex.title("Projectile")

#motion all kinds

e = Entry(jimbex, width = 40)
e.grid(row = 0, column = 0, columnspan = 4, pady = 5)

def button_click(number):
		#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))


def Time():
	f_num = e.get()
	global parameter
	global numb1
	parameter = "time"
	numb1 = int(f_num)
	e.delete(0, END)


def Hmax():
	f_num = e.get()
	global parameter
	global numb2
	parameter = "Height"
	numb2 = int(f_num)
	e.delete(0, END)


def Range():
	f_num = e.get()
	global parameter
	global numb3
	parameter = "range"
	numb3 = int(f_num)
	e.delete(0, END)

def Rmax():
	f_num = e.get()
	global parameter
	global numb4
	parameter = "rmax"
	numb4 = int(f_num)
	e.delete(0, END)

def ini():
	f_num = e.get()
	global parameter
	global numb4
	parameter = "ini"
	numb4 = int(f_num)
	e.delete(0, END)

def tita():
	f_num = e.get()
	global parameter
	global numb5
	parameter = "tita"
	numb5 = int(f_num)
	e.delete(0, END)

def find_time():
	e.insert(0, (2 * numb4 * math.sin(math.radians(numb5))) / 10)

def find_Hmax():
	e.insert(0, ((numb4 * numb4) * (math.sin(math.radians(numb5)) * math.sin(math.radians(numb5)))) / 20 )

def find_range():
	e.insert(0, ((numb4 * numb4) * math.sin(math.radians(numb5 * 2))) / 10)

def find_Rmax():
	e.insert(0, (numb4 * numb4) / 10)

def find_u():
	if parameter == "time":
		e.insert(0, (10 * numb1) / (2 * math.sin(math.radians(numb5))))
	if parameter == "Height":
		e.insert(0, math.sqrt(()))
	if parameter == "range":
		e.insert(0, math.sqrt((numb3 * 10) / math.sin(math.radians(numb5))))
	if parameter == "rmax":
		e.insert(0, math.sqrt(numb4 * 10))

def find_tita():
	if parameter == "time":
		e.insert(0, (10 * numb1) / (2 * math.sin(math.radians(numb5))))
	if parameter == "Height":
		e.insert(0, math.sqrt())
	if parameter == "range":
		e.insert(0, math.degrees(math.asin((numb3 * 10) / (2 * (numb4 * numb4)))))

def clear():
	e.delete(0, END)
	






num1 = Button(jimbex, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
num2 = Button(jimbex, text = "2", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
num3 = Button(jimbex, text = "3", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
num4 = Button(jimbex, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
num5 = Button(jimbex, text = "5", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
num6 = Button(jimbex, text = "6", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
num7 = Button(jimbex, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
num8 = Button(jimbex, text = "8", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
num9 = Button(jimbex, text = "9", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
num0 = Button(jimbex, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
point = Button(jimbex, text = ".", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
Height = Button(jimbex, text = "Hmax", padx = 17, pady = 20, fg = "black", bg = "white", command = Hmax)
sec = Button(jimbex, text = "time", padx = 20, pady = 20, fg = "black", bg = "white", command = Time)
rang = Button(jimbex, text = "range", padx = 17, pady = 20, fg = "black", bg = "white", command = Range)
maxR = Button(jimbex, text = "Rmax", padx = 18, pady = 20, fg = "black", bg = "white", command = Rmax)
speed = Button(jimbex, text = "U", padx = 30, pady = 20, fg = "black", bg = "white", command = ini)
teeta = Button(jimbex, text = "θ", padx = 30, pady = 20, fg = "black", bg = "white", command = tita)
find_height = Button(jimbex, text = "Hmax =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_Hmax)
find_sec = Button(jimbex, text = "t =", padx =  31, pady = 20, fg = "black", bg = "white", command = find_time)
find_rang = Button(jimbex, text = "Range =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_range)
find_maxr = Button(jimbex, text = "Rmax =", padx = 18, pady = 20, fg = "black", bg = "white", command = find_Rmax)
find_speed = Button(jimbex, text = "u =", padx = 30, pady = 20, fg = "black", bg = "white", command = find_u)
find_teeta = Button(jimbex, text = "θ =", padx = 30, pady = 20, fg = "black", bg = "white", command = find_tita)
erase = Button(jimbex, text = "clear", padx = 20, pady = 20, fg = "black", bg = "white", command = clear)







num1.grid(row = 1, column = 0)
num2.grid(row = 1, column = 1)
num3.grid(row = 1, column = 2)
num4.grid(row = 2, column = 0)
num5.grid(row = 2, column = 1)
num6.grid(row = 2, column = 2)
num7.grid(row = 3, column = 0)
num8.grid(row = 3, column = 1)
num9.grid(row = 3, column = 2)
num0.grid(row = 4, column = 0)
point.grid(row = 4, column = 1)
Height.grid(row = 4, column = 2)
sec.grid(row = 5, column = 0)
rang.grid(row = 5, column = 1)
maxR.grid(row = 5, column = 2)
erase.grid(row = 6, column = 2)
speed.grid(row = 6, column = 0)
teeta.grid(row = 6, column = 1)
find_height.grid(row = 1, column = 3)
find_sec.grid(row = 2, column = 3)
find_rang.grid(row = 3, column = 3)
find_maxr.grid(row = 4, column = 3)
find_speed.grid(row = 5, column = 3)
find_teeta.grid(row = 6, column = 3)




jimbex.mainloop()



