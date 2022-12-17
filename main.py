from tkinter import *
from tkinter import ttk


def CreateWindow():
    root_frame = Tk()
    root_frame.title("VLAKOVÝ DISPEČING")
    root_frame.geometry("800x500")

    icon = PhotoImage(file="icon.gif")
    root_frame.iconphoto(True, icon)

    root_frame.mainloop()


CreateWindow()