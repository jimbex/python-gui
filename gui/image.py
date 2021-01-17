from tkinter import *
import PIL

root = Tk()
root.title('Jago')
root.iconbitmap('c:/NIIT/palm-tree-icon.ico')


img = PhotoImage(file = "c:/Users/USER/Downloads/play-curiosity-inner-child-card.png")
mylabel = Label(image= img)
mylabel.pack()













quit = Button(root, text = "quit", command = root.quit)
quit.pack()



root.mainloop()