from tkinter import *

root = Tk()

root.title("jago")

e = Entry(root, width = 50, bg = "grey", fg = "black")

e.pack()


#def myClick():
#	l = Label(root, text = "Hello" + e.get())
#	l.pack()

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def clear():
	e.delete(0, END)

def add():
	first = e.get()
	global f_num
	f_num = int(first)
	e.delete(0, END)

def equal():
	second = e.get()
	e.delete(0, END)
	e.insert(0, f_num + int(second))



mybutton = Button(root, text = "test", fg = "white", bg = "black", command = lambda: button_click(5))
mybutton.pack()



root.mainloop() 