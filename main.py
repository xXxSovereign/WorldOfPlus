from commands.mapStuff import *
from tkinter import *

root = Tk()

root.geometry("500x500")

root.title("poggy woggy")


def button():
    myLable = Label(root, text="not poggers :(")
    myLable.pack()


def cmd():
    l = Label(root, text="pretty pog :)")
    l.pack()


myLabel = Label(root, text="its 4:10")
myLabel.pack()

myLabel2 = Label(root, text="broooo")
myLabel2.pack()

myLabel3 = Label(root, text="Poggers")
myLabel3.pack()

butonp = Button(root, text="click me", command=button)
butonp.pack()

boton = Button(root, text="dont k;lcik me plox", command=cmd)
boton.pack()

root.mainloop()
