from tkinter import *
root =Tk()

label1 = Label (root , text ="Firstname") #basically text 
label2 = Label (root, text="LastName")

entry1 =Entry (root) #text field box
entry2 = Entry(root)

label1.grid(row =0 , column=0) # Grid Layout 
label2.grid (row =1 ,column =0)

entry1.grid (row=0, column =1 )
entry2.grid (row =1 ,column =1)

root.mainloop() 