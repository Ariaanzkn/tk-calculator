import tkinter
from tkinter import *

# + function
def plus():
    Title=(float(input.get()) + float(input2.get()))
    Label.config(text=Title)
# reset button function
def reset():
    input.delete(0, END)
    input2.delete(0, END)
    Label.config(text='')

window = Tk()
title = window.title('calculator')
window.geometry('500x500')
window.minsize(500, 500)

#label
Label = Label(window,text ="Welcome to TK_calculator",fg="red",bg='light gray',font=("Arial",20))
Label.pack()

#button

button = Button(window,text ="Calculate",bg='light gray',font=("Arial",10),command=plus)
button.pack()

button2 = Button(window,text ="Reset",bg='light gray',font=("Arial",10),command=reset)
button2.pack()

#inputs
input = Entry(window)
instruction_label =tkinter.Label(window, text="Input x:")
instruction_label.pack(pady=10)
input.pack()

input2 = Entry(window)
instruction_label =tkinter.Label(window, text="Input y:")
instruction_label.pack(pady=10)
input2.pack()

window.mainloop()
