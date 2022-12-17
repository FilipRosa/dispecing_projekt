from tkinter import *

def ShowNameDataBtn():
    user_name = ent.get()
    
    print(user_name)

root_frame = Tk()
root_frame.geometry("1000x600")
root_frame.title("VLAKOVÝ DISPEČING")
root_frame.config(background="black")

icon = PhotoImage(file="icon.gif")
root_frame.iconphoto(True, icon)

main_label = Label(root_frame, text="Vitajte na pracovisku vlakového dispečingu pre trať Prievidza - Chynorany", fg="white", bg="black", font=("Century Schoolbook", 17))
main_label.place(x = 120, y = 200)

name_label = Label(root_frame, text="Zadajte Vaše meno: ", fg="white", bg="black")
name_label.place(x = 330, y = 300)

ent = Entry(root_frame)
ent.place(x = 450, y = 300)

btn = Button(root_frame, text="ENTER", command=ShowNameDataBtn)
btn.place(x = 580, y = 297)

root_frame.mainloop()
