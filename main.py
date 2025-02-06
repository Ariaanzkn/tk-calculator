import tkinter
from tkinter import *



# main function
def Callculator():
    if Operator.get() == '+':
        return Plus()
    elif Operator.get() == '-':
        return Minus()
    elif Operator.get() == '*':
        return Multiplication()
    elif Operator.get() == '/':
        return Division()
    else:
        Label.config(text='Invalid Operator')
        return Label
# + function
def Plus():
    Title=(float(number1.get()) + float(number2.get()))
    Label.config(text=Title)
# - function
def Minus():
    Title=(float(number1.get()) - float(number2.get()))
    Label.config(text=Title)
# * function
def Multiplication():
    Title=(float(number1.get()) * float(number2.get()))
    Label.config(text=Title)
# / function
def Division():
    if number2.get() == '0':
        Label.config(text='Error: Division by zero')
        return Label
    else:
        Title=(float(number1.get()) / float(number2.get()))
        Label.config(text=Title)
# reset button function
def reset():
    number1.delete(0, END)
    number2.delete(0, END)
    Operator.delete(0, END)
    Label.config(text='')
    

#window
window = Tk()
title = window.title('calculator')
window.geometry('500x500')
window.minsize(500, 500)

#label
Label = Label(window,text ="Welcome to TK_calculator",fg="red",bg='light gray',font=("Arial",20))
Label.pack()

#button
button = Button(window,text ="Calculate",bg='light gray',font=("Arial",10),command=Callculator)
button.pack()

button2 = Button(window,text ="Reset",bg='light gray',font=("Arial",10),command=reset)
button2.pack()

#inputs
number1 = Entry(window)
instruction_label = tkinter.Label(window, text="Input x:")
instruction_label.pack(pady=10)
number1.pack()

number2 = Entry(window)
instruction_label = tkinter.Label(window, text="Input y:")
instruction_label.pack(pady=10)
number2.pack()

Operator = Entry(window)
instruction_label = tkinter.Label(window, text="Input Operator:(+,-,*,/)")
instruction_label.pack(pady=10)
Operator.pack()

window.mainloop()
