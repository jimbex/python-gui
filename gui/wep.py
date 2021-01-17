from tkinter import *
import math

root = Tk()

root.title("learn")
root.iconbitmap("")

stats = Tk()

stats.title("statistics")

e = Entry(stats, width  = 50)
e.grid(row = 0, column = 0, pady = 10, columnspan = 5)

def button_click(number):
	#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))














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
