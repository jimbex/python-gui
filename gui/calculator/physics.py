from tkinter import *
from math import *

jimbex = Tk()

jimbex.title("Physiscs Calculator")

#motion all kinds

e = Entry(jimbex, width = 40)
e.grid(row = 0, column = 0, columnspan = 4, pady = 5)

def button_click(number):
		#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))


def initial():
	f_num = e.get()
	global ini
	global numb1
	ini = "ini"
	numb1 = int(f_num)
	e.delete(0, END)
		
		

def final():
	s_num = e.get()
	global fin
	global parameter
	global numb2
	parameter = "fin"
	fin = "fin"
	numb2 = int(s_num)
	e.delete(0, END)

def length():
	t_num = e.get()
	global parameter
	global numb3
	parameter = "len"
	numb3 = int(t_num)
	e.delete(0, END)
	
	

def seconds():
	i_num = e.get()
	global parameter
	global fin
	global numb4
	fin = "sec"
	parameter = "sec"
	numb4 = int(i_num)
	e.delete(0, END)


def acceleration():
	a_num = e.get()
	global acc
	global numb5
	acc = "acc"
	numb5 = int(a_num)
	e.delete(0, END)

def find_ini():
	if acc == "acc":
		if parameter == "sec" and fin == "fin":
			e.insert(0, numb2 - (numb5 * numb4))
		if fin == "fin" and parameter == "len":
			e.insert(0, sqrt((numb2 * numb2) - (numb3 * numb5 * 2)))
		if parameter == "len" and fin == "sec":
			e.insert(0, (numb3 - (0.5 * numb5 * (numb4 * numb4))) / numb4)
	
	

def find_len():
	if acc == "acc":
		if ini == "ini" and parameter == "sec":
			e.insert(0, (numb1 * numb4) + (0.5 * numb5 *(numb4 * numb4)) )
		if ini == "ini" and parameter == "fin":
			e.insert(0, ((numb2 * numb2) - (numb1 * numb1)) / (2 * numb5))

def find_fin():

	if acc == "acc":
		if ini == "ini" and parameter == "sec":
			e.insert(0, numb1 + (numb5 * numb4) )
		if ini == "ini" and parameter == "len":
			e.insert(0, sqrt((numb1 * numb1) + (2 * numb5 * numb3)))

		
		
def find_acc():
	if ini == "ini":
		if fin == "fin" and parameter == "sec":
			e.insert(0, (numb2 - numb1) / numb4)
		if fin == "fin" and parameter == "len":
			e.insert(0, ((numb2 * numb2) - (numb1 * numb1)) / (2 * numb3))
		if fin == "sec" and parameter == "len":
			e.insert(0, (numb3 - (numb1 * numb4)) / (0.5 * (numb4 * numb4)))

def find_time():
	if ini == "ini" and acc == "acc":
		if fin == "fin":
			e.insert(0, (numb2 - numb1) / numb5)






def find():
	e.delete(0, END)
	


		


	
		



num1 = Button(jimbex, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
num2 = Button(jimbex, text = "2", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
num3 = Button(jimbex, text = "3", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
num4 = Button(jimbex, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
num5 = Button(jimbex, text = "5", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
num6 = Button(jimbex, text = "6", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
num7 = Button(jimbex, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
num8 = Button(jimbex, text = "8", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
num9 = Button(jimbex, text = "9", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
num0 = Button(jimbex, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
let1 = Button(jimbex, text = "u", padx = 30, pady = 20, fg = "black", bg = "white", command = find_ini)
let2 = Button(jimbex, text = "v", padx = 30, pady = 20, fg = "black", bg = "white", command = find_fin)
let3 = Button(jimbex, text = "s", padx = 32, pady = 20, fg = "black", bg = "white", command = find_len)
let4 = Button(jimbex, text = "t", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click("t"))
let5 = Button(jimbex, text = "a", padx = 30, pady = 20, fg = "black", bg = "white", command = find_acc)
point = Button(jimbex, text = ".", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
F_vel = Button(jimbex, text = "Fvel", padx = 28, pady = 20, fg = "black", bg = "white", command = final)
I_vel = Button(jimbex, text = "Ivel", padx = 28, pady = 20, fg = "black", bg = "white", command = initial)
Distance = Button(jimbex, text = "Dist", padx = 28, pady = 20, fg = "black", bg = "white", command = length)
time = Button(jimbex, text = "Time", padx = 25, pady = 20, fg = "black", bg = "white", command = seconds)
answer = Button(jimbex, text = "clear", padx = 22, pady = 20, fg = "black", bg = "white", command = find)
accelerate = Button(jimbex, text = "Accl", padx = 27, pady = 20, fg = "black", bg = "white", command = acceleration)






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
F_vel.grid(row = 4, column = 3)
I_vel.grid(row = 1, column = 3)
let1.grid(row = 5, column = 0)
let2.grid(row = 5, column = 1)
let3.grid(row = 5, column = 2)
let4.grid(row = 6, column = 1)
let5.grid(row = 6, column = 0)
Distance.grid(row = 2, column = 3)
time.grid(row = 3, column = 3)
answer.grid(row = 4, column = 2)
accelerate.grid(row = 5, column = 3)








jimbex.mainloop()