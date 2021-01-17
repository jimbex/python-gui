from tkinter import *
from numpy import array
import numpy
import math
import statistics

stats = Tk()

stats.title("statistics")

e = Entry(stats, width  = 30)
e.grid(row = 0, column = 0, pady = 10, columnspan = 4)
global count
global total
global inp
total = 0
count = 0
def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))




def avg():
	global num
	global inp
	inp = "next"
	f_num = list(e.get().split(" "))
	e.delete(0, END)
	total = 0
	count = 0
	for x in f_num:
		total = total + int(x)
		count = count + 1

	#x = list(map(int, f_num.split(",")))
	e.delete(0, END)
	e.insert(0, total / count)

	#numb = int(f_num)
	#num = list(f_num)
	#numb = int(num)


def variance():
	global num
	global inp
	inp = "next"
	f_num = array(e.get().split(" "))
	e.delete(0, END)
	total = 0
	count = 0
	for x in f_num:
		total = total + int(x)
		count = count + 1
		total = total / count
		
	a = 0
	sums = 0

	while a < count:
		num = int(f_num[a]) - total
		sums = sums + (num ** 2) 
		a = a + 1

	sums = sums / a
	e.insert(0, sums)

	#num = count - 1

def sd():
	global num
	global inp
	inp = "next"
	f_num = array(e.get().split(" "))
	e.delete(0, END)
	total = 0
	count = 0
	for x in f_num:
		total = total + int(x)
		count = count + 1
		total = total / count
		
	a = 0
	sums = 0

	while a < count:
		num = int(f_num[a]) - total
		sums = sums + (num ** 2) 
		a = a + 1

	sums = sums / a
	e.insert(0, math.sqrt(sums))



	


def clear():
	e.delete(0, END)



	


num1 = Button(stats, text = "1", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(1))
num2 = Button(stats, text = "2", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(2))
num3 = Button(stats, text = "3", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(3))
num4 = Button(stats, text = "4", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(4))
num5 = Button(stats, text = "5", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(5))
num6 = Button(stats, text = "6", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(6))
num7 = Button(stats, text = "7", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(7))
num8 = Button(stats, text = "8", padx = 31, pady = 20, fg = "black", bg = "white", command = lambda: button_click(8))
num9 = Button(stats, text = "9", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click(9))
num0 = Button(stats, text = "0", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(0))
point = Button(stats, text = ".", padx = 32, pady = 20, fg = "black", bg = "white", command = lambda: button_click("."))
next_num = Button(stats, text = "n", padx = 30, pady = 20, fg = "black", bg = "white", command = lambda: button_click(" "))
mean = Button(stats, text = "A", padx = 30, pady = 20, fg = "black", bg = "white", command = avg)
var = Button(stats, text = "V", padx = 30, pady = 20, fg = "black", bg = "white", command = variance)
erase = Button(stats, text = "clear", padx = 20, pady = 20, fg = "black", bg = "white", command = clear)
sdev = Button(stats, text = "S", padx = 30, pady = 20, fg = "black", bg = "white", command = sd)

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
next_num.grid(row = 4, column = 3)
mean.grid(row = 1, column = 4)
var.grid(row = 2, column = 4)
erase.grid(row = 3, column = 4)
sdev.grid(row = 4, column = 4)


stats.mainloop()