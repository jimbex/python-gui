from tkinter import *

root = Tk()
root.title('Jago')
root.iconbitmap('c:/NIIT/palm-tree-icon.ico')

frame = LabelFrame(root, text = "jago", padx = 10, pady = 10)
frame.pack(padx = 4, pady = 4)
b = Button(frame, text = "fuck u", padx = 10, pady = 10, command = root.quit)
b.pack()






root.mainloop()