from tkinter import *

root_frame = Tk()
root_frame.geometry("1000x600")
root_frame.title("VLAKOVÝ DISPEČING")
root_frame.config(background="black")
icon = PhotoImage(file="icon.gif")
root_frame.iconphoto(True, icon)

def FirstPage():
    def SecondPage():
        main_label.destroy()
        btn.destroy()

        main_label_2 = Label(root_frame, text="Prievidza - Chynorany", fg="white", bg="black", font=("Century Schoolbook", 17))
        main_label_2.place(x = 120, y = 200)

    main_label = Label(root_frame, text="Vitajte na pracovisku vlakového dispečingu pre trať Prievidza - Chynorany", fg="white", bg="black", font=("Century Schoolbook", 17))
    main_label.place(x = 120, y = 200)

    btn = Button(root_frame, text="ZAČAŤ HRAŤ", command=SecondPage)
    btn.place(x = 450, y = 300)

FirstPage()
root_frame.mainloop()