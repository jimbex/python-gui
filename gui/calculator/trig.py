from tkinter import *
from math import *

root = Tk()
root.title("Trig Calc")

cos = Button(root, text = "cos", padx= 26, pady = 20, fg = "white", bg = "black")
cos.grid(row = 1, column = 4)

sin = Button(root, text = "sin", padx= 27.5, pady = 20, fg = "white", bg = "black")
sin.grid(row = 2, column = 4)

tan = Button(root, text = "tan", padx= 26.5, pady = 20, fg = "white", bg = "black")
tan.grid(row = 3, column = 4)

cosec = Button(root, text = "cosec", padx= 20.5, pady = 20, fg = "white", bg = "black")
cosec.grid(row = 1, column = 5)

sec = Button(root, text = "sec", padx= 27.5, pady = 20, fg = "white", bg = "black")
sec.grid(row = 2, column = 5)

cot = Button(root, text = "cot", padx= 27.5, pady = 20, fg = "white", bg = "black")
cot.grid(row = 3, column = 5)

equal = Button(root, text = "=", padx= 102, pady = 20, fg = "white", bg = "black")
equal.grid(row = 4, column = 3, columnspan = 3)

num1 = Button(root, text = "1", padx = 20, pady = 20, fg = "white", bg = "black")
num2 = Button(root, text = "2", padx = 21, pady = 20, fg = "white", bg = "black")
num3 = Button(root, text = "2", padx = 22, pady = 20, fg = "white", bg = "black")
num4 = Button(root, text = "4", padx = 20, pady = 20, fg = "white", bg = "black")
num5 = Button(root, text = "5", padx = 21, pady = 20, fg = "white", bg = "black")
num6 = Button(root, text = "6", padx = 22, pady = 20, fg = "white", bg = "black")
num7 = Button(root, text = "7", padx = 20, pady = 20, fg = "white", bg = "black")
num8 = Button(root, text = "8", padx = 21, pady = 20, fg = "white", bg = "black")
num9 = Button(root, text = "9", padx = 22, pady = 20, fg = "white", bg = "black")
num0 = Button(root, text = "0", padx = 20, pady = 20, fg = "white", bg = "black")
point = Button(root, text = ".", padx = 22, pady = 20, fg = "white", bg = "black")

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








root.mainloop()