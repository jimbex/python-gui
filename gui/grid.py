from tkinter import *

root = Tk()

#creating a label widget
def function():
	myLabel1 = Label(root, text = "What is the colour of rose \na. blue\nb. green\nc. red\n\n")
	ent = Entry()
#	myLabel2 = Label(root, text = "Calc")

#Shoving it into the screen
	myLabel1.pack()
#	myLabel2.pack()
	ent.pack()


but = Button(root, text = "click", command = function)

but.pack()


root.mainloop()