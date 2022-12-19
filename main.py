from tkinter import *
from PIL import Image

root_frame = Tk()
root_frame.geometry("1000x600")
root_frame.title("VLAKOVÝ DISPEČING")
root_frame.config(background="black")
icon = PhotoImage(file="icon.gif")
root_frame.iconphoto(True, icon)


def OpenScheme():
    scheme_img = Image.open("scheme.png")
    return scheme_img.show()

def FirstPage():
    def FirstPageWithName():
        main_label.destroy()
        user_name.destroy

        btn = Button(root_frame, text="POĎME NA TO!", command=SecondPage)
        btn.place(x = 450, y = 300)


    def SecondPage():
        main_label.destroy()
        btn.destroy()

        main_label_2 = Label(root_frame, text="Prievidza - Chynorany", fg="white", bg="black", font=("Century Schoolbook", 17))
        main_label_2.place(x = 120, y = 200)

        btn_scheme = Button(root_frame, text="Mapa", command=OpenScheme)
        btn_scheme.place(x = 450, y = 300)
        

    main_label = Label(root_frame, text="Vitajte na pracovisku vlakového dispečingu pre trať Prievidza - Chynorany", fg="white", bg="black", font=("Century Schoolbook", 17))
    main_label.place(x = 120, y = 200)

    user_label = Label(root_frame, text="Zadajte svoje meno:", fg="white", bg="black", font=("Century Schoolbook", 17))
    user_label.place(x = 200, y = 300)

    user_name = Entry(root_frame)
    user_name.place(x = 420, y = 310)

    btn_user_name = Button(root_frame, text="ENTER", command=FirstPageWithName)
    btn_user_name.place(x = 550, y = 305)

FirstPage()
root_frame.mainloop()