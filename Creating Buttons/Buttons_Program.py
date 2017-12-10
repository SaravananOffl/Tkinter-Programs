from tkinter import * # Make sure tkinter is installed,Tkinter is used for GUI implementation

root = Tk() # to initialise a window 

newframe = Frame ( root ) #to create a frame
newframe.pack() #set newframe to root window

newoframe = Frame(root)  #same as above
newoframe.pack(side = BOTTOM) # this frame is set to bottom of the window

button1 =  Button(newframe ,text=" BUTTON 1 " , fg="RED") #Creating a button

button1.pack() 

button2= Button(newoframe , text="BUTTON 2" , fg="BLUE") # same as above
button2.pack()

root.mainloop() # this is to make the window stay until the user exits manually