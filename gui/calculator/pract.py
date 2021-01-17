from tkinter import *
from math import *

root = Tk()

root.title("Jimbex Calculator") 

e = Entry(root, width  = 60)
e.grid(row = 0, column = 0, pady = 10, columnspan = 6)

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def delete():
	e.delete(0, END)

def add():
	f_num = e.get()
	global num
	global math
	math = "add"
	num = int(f_num)
	e.delete(0, END)

def multiply():
	f_num = e.get()
	global num
	global math
	math = "multiply"
	num = int(f_num)
	e.delete(0, END)
	

def divide():
	f_num = e.get()
	global num
	global math
	math = "divide"
	num = int(f_num)
	e.delete(0, END)

def subtract():
	f_num = e.get()
	global num
	global math
	math = "subtract"
	num = int(f_num)
	e.delete(0, END)

def powe():
	f_num = e.get()
	global num
	global math
	math = "power"
	num = int(f_num)
	e.delete(0, END)

def square():
	f_let = e.get()
	global num
	global math
	math = "square"
	num = str(f_let)
	e.delete(0, END)


def cent():
	f_let = e.get()
	global num
	global math
	math = "percent"
	num = int(f_num)
	e.delete(0, END)
	

	

def equal():
	s_num = e.get()
	e.delete(0, END)

	if math == "add":
		e.insert(0, num + int(s_num))
		e.insert(0, str(num) + " + " + s_num + " = ")

	if math == "subtract":
		e.insert(0, num - int(s_num))

	if math == "multiply":
		e.insert(0, num * int(s_num))

	if math == "divide":
		e.insert(0, num / int(s_num))

	if math == "power":
		e.insert(0, num ** int(s_num))

	if math == "square":
		e.insert(0, sqrt(int(s_num)))








num1 = Button(root, text = "1", padx = 30, pady = 20, fg = "white", bg = "black", command = lambda: button_click(1))
num2 = Button(root, text = "2", padx = 31, pady = 20, fg = "white", bg = "black", command = lambda: button_click(2))
num3 = Button(root, text = "3", padx = 32, pady = 20, fg = "white", bg = "black", command = lambda: button_click(3))
num4 = Button(root, text = "4", padx = 30, pady = 20, fg = "white", bg = "black", command = lambda: button_click(4))
num5 = Button(root, text = "5", padx = 31, pady = 20, fg = "white", bg = "black", command = lambda: button_click(5))
num6 = Button(root, text = "6", padx = 32, pady = 20, fg = "white", bg = "black", command = lambda: button_click(6))
num7 = Button(root, text = "7", padx = 30, pady = 20, fg = "white", bg = "black", command = lambda: button_click(7))
num8 = Button(root, text = "8", padx = 31, pady = 20, fg = "white", bg = "black", command = lambda: button_click(8))
num9 = Button(root, text = "9", padx = 32, pady = 20, fg = "white", bg = "black", command = lambda: button_click(9))
num0 = Button(root, text = "0", padx = 30, pady = 20, fg = "white", bg = "black", command = lambda: button_click(0))
point = Button(root, text = ".", padx = 32, pady = 20, fg = "white", bg = "black", command = lambda: button_click("."))
# fg fore ground colour
# bg back ground colour
# command what to do
# padx horizontal size
# pady vertical size


plus = Button(root, text = "+", padx = 30, pady = 20, fg = "white", bg = "black", command = add)
subtr = Button(root, text = "-", padx = 31, pady = 20, fg = "white", bg = "black", command = subtract)
div = Button(root, text = "/", padx = 31, pady = 20, fg = "white", bg = "black", command = divide)
mult = Button(root, text = "x", padx = 31, pady = 20, fg = "white", bg = "black", command = multiply)
power = Button(root, text = "^", padx = 31, pady = 20, fg = "white", bg = "black", command = powe)
sqare = Button(root, text = "_/", padx = 30, pady = 20, fg = "white", bg = "black", command = square)
percent = Button(root, text = "%", padx = 30, pady = 20, fg = "white", bg = "black", command = cent)
#cos = Button(root, text = "cos", padx = 30, pady = 20, fg = "white", bg = "black")
#sin = Button(root, text = "sin", padx = 30, pady = 20, fg = "white", bg = "black")
#tan = Button(root, text = "tan", padx = 30, pady = 20, fg = "white", bg = "black")
#cosec = Button(root, text = "cosec", padx = 30, pady = 20, fg = "white", bg = "black")
#sec = Button(root, text = "sec", padx = 30, pady = 20, fg = "white", bg = "black")
#cot = Button(root, text = "cot", padx = 30, pady = 20, fg = "white", bg = "black")
clear = Button(root, text = "clear", padx = 174, pady = 20, fg = "white", bg = "black", command = delete)
equals = Button(root, text = "=", padx = 183, pady = 20, fg = "white", bg = "black", command = equal)
back = Button(root, text = "back", padx = 22, pady = 20, fg = "white", bg = "black", )
quit = Button(root, text = "quit", padx = 24, pady = 20, fg = "white", bg = "black", command = root.quit)

num1.grid(row = 1, column = 1)
num2.grid(row = 1, column = 2)
num3.grid(row = 1, column = 3)
num4.grid(row = 2, column = 1)
num5.grid(row = 2, column = 2)
num6.grid(row = 2, column = 3)
num7.grid(row = 3, column = 1)
num8.grid(row = 3, column = 2)
num9.grid(row = 3, column = 3)
num0.grid(row = 4, column = 1)
point.grid(row = 4, column = 2)
plus.grid(row = 1, column = 4)
subtr.grid(row = 2, column = 4)
div.grid(row = 3, column = 4)
mult.grid(row = 4, column = 4)
power.grid(row = 4, column = 3)
sqare.grid(row = 1, column = 5)
percent.grid(row = 2, column = 5)
back.grid(row = 3, column = 5)
quit.grid(row = 4, column = 5)

#cos.grid(row = 1, column = 5)
#sin.grid(row = 2, column = 5)
#tan.grid(row = 3, column = 5)
clear.grid(row = 5, column = 1, columnspan = 5)
#cosec.grid(row = 1, column = 6)
#sec.grid(row = 2, column = 6)
#cot.grid(row = 3, column = 6)
equals.grid(row = 6, column = 1, columnspan = 5)

# columnspan




root.mainloop()