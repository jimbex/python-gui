from tkinter import *

root = Tk()

root.title("Questionaire")

#global score
#score = 0


questions = [
  "What is the colour of rose\na. blue\nb. green\nc. red\n\n",
  "what is the colour of rice\na. black\nb. white\nc. grey\n\n",
  "What is the colour of the sea \na. red\nb. blue\nc. green\n\n"
 ]

question = Label(root, text = questions[0])
page_num = Label(root, text = "1 of " + str(len(questions) ), bd = 1, relief = SUNKEN, anchor = E)
question.grid(row = 0, column = 0, columnspan = 3)
page_num.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

  
def forward(questnum):
  	global question
  	global next_button
  	global back_button
  	global page_num
  	question.grid_forget()
  	question = Label(root, text = questions[questnum-0])
  	next_button = Button(root, text = ">>", padx = 10, pady = 10, command = lambda: forward(questnum+1))
  	back_button = Button(root, text = "<<", padx = 10, pady = 10, command = lambda: back(questnum-1))
  	page_num = Label(root, text = str(questnum +1) + " of " + str(len(questions)), bd = 1, relief = SUNKEN, anchor = E)
  	question.grid(row = 0, column = 0, columnspan = 3)
  	next_button.grid(row = 1, column = 2)
  	back_button.grid(row = 1, column = 0)
  	page_num.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

  	if questnum == 2:
  		next_button = Button(root, text = ">>", padx = 10, pady = 10, state = DISABLED)
  		next_button.grid(row = 1, column = 2)


def back(questnum):
  	global question
  	global next_button
  	global back_button
  	question.grid_forget()
  	question = Label(root, text = questions[questnum-0])
  	next_button = Button(root, text = ">>", padx = 10, pady = 10, command = lambda: forward(questnum+1))
  	back_button = Button(root, text = "<<", padx = 10, pady = 10, command = lambda: back(questnum-1))
  	page_num = Label(root, text = str(questnum +1) + " of " + str(len(questions)), bd = 1, relief = SUNKEN, anchor = E)
  	question.grid(row = 0, column = 0, columnspan = 3)
  	next_button.grid(row = 1, column = 2)
  	back_button.grid(row = 1, column = 0)
  	page_num.grid(row = 2, column = 0, columnspan = 3, sticky = W+E)

  	if questnum == 0:
  		back_button = Button(root, text = "<<", padx = 10, pady = 10, state = DISABLED)
  		back_button.grid(row = 1, column = 0)




next_button = Button(root, text = ">>", padx = 10, pady = 10, command = lambda: forward(1))
back_button = Button(root, text = "<<", padx = 10, pady = 10, command = back, state = DISABLED)
exit = Button(root, text = "exit", pady = 10, padx = 10, command = root.quit)


next_button.grid(row = 1, column = 2)
back_button.grid(row = 1, column = 0)
exit.grid(row = 1, column = 1, pady= 10)





    
    
   

 








root.mainloop()