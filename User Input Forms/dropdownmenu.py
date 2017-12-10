from tkinter import *
 
def function1():
    print("Menu Item Clicked")
    

root=Tk()
 
 
mymenu =Menu (root)
 
root.config(menu=mymenu)

submenu = Menu (mymenu)
mymenu.add_cascade (label="File" , menu=submenu)


submenu.add_command(label = "Project",command=function1)
submenu.add_command(label = "save", command =function1)

toolbar =Frame (root, bg= "pink")
buttonone= Button(toolbar,text = "Insert Files", command =function1)
buttonone.pack(side = LEFT ,padx=2 , pady=3 )
printbutton= Button(toolbar,text = "Attach Files", command = function1)
printbutton.pack(side = LEFT,padx=2,pady=3)

toolbar.pack(side=TOP,fill =X)
root.mainloop()

