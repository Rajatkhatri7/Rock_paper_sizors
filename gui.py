#Gui for games
#sudo apt-get install python3-tk

import tkinter

from tkinter import *

from tkinter import ttk

import rock_paper_sizor

root = Tk()
root.title("LINUX USER & DEVOLOPER'S GAMES")

mainframe = Frame(root,height = 200,width = 500)
#mainframe.pack_propogate(0)
mainframe.pack(padx = 5,pady = 5)

intro = Label(mainframe ,text = "Welcome to Linux Developer's Game collection")

intro.pack(side = TOP)

rps_button = Button(mainframe,text = "Rock,paper & sizor",command = rock_paper_sizor.start)
rps_button.pack()

exit_button = Button(mainframe ,text = "Quit",command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop(0)
