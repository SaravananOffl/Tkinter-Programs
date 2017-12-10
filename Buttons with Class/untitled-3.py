from tkinter import *

class MyButtons :
    
    def __init__(self , rootone):
        frame = Frame(rootone)
        frame.pack()
        
        self.printButton = Button(frame,text="click Here", command=self.printmessage())
        self.printButton.pack()
        
        self.quitbutton = Button(frame, text="exit",command =frame.quit)
        self.quitbutton.pack(side = LEFT)
    
    
    def printmessage(self):
        print("Button Clicked")

root =Tk()
b = MyButtons(root)
root.mainloop()