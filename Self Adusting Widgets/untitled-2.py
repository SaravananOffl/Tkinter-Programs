from tkinter import *

root =Tk()


def dosomething():
    print("You Clicked the Button")

button1= Button(root,text ="Click me",bg="blue",command = dosomething)
button1.pack()

root.mainloop()
