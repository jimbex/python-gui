from tkinter import *
from math import *

root = Tk()

root.title("Jimbex Calculator") 

r = IntVar()
r.set("2")



Radiobutton(root, text = "option 1", variable = r, value = 1).pack()

Radiobutton(root, text = "option 2", variable = r, value = 2).pack()

myLabel = Label(root, text = r.get())
myLabel.pack()


root.mainloop()