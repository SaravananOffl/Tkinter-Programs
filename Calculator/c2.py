try:
    # for Python2
    from Tkinter import *  # notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry('400x200+100+200')

label1=Label(root,text="Enter first number")
label2=Label(root,text = "Enter second number")
 
entryone=Entry(root,textvariable=number1)
entrytwo=Entry(root,textvariable=number2)

label1.grid(row=0,column=0)
entryone.grid(row=0,column=1)

label2.grid(row=1,column=0)
entrytwo.grid(row=1,column=1)

CalcButton=Button(root,command=add)

def add(number1,number2):
    print(number1+number2)

CalcButton.pack()
root.mainloop()
