from tkinter import *
from PIL import Image
import time

root_frame = Tk()
root_frame.geometry("1000x600")
root_frame.title("VLAKOVÝ DISPEČING")
root_frame.config(background="black")
icon = PhotoImage(file="icon.gif")
root_frame.iconphoto(True, icon)

def OpenScheme():
    scheme_img = Image.open("scheme.png")
    return scheme_img.show()

def SchemeButton():
    return Button(root_frame, text="Mapa", command=OpenScheme)

def FirstPage():
    def FirstPageWithNames():
        def SecondPage():
            def ThirdPage():
                SchemeButton().destroy()
                main_label_2.destroy()
                btn_next.destroy()
                text.destroy()

                SchemeButton().place(x = 220, y = 15)

                text_score = Text(root_frame, height=3, width=20)
                text_score.place(x = 5, y = 10)

                score_text = """ Skóre """

                text_score.insert(END, score_text)

                localtime = time.asctime(time.localtime(time.time()))
                text_time = Text(root_frame, height=3, width=30)
                text_time.place(x = 600, y = 10)
                text_time.insert(END, localtime)

        
            main_label.destroy()
            btn.destroy()

            main_label_2 = Label(root_frame, text="Pokyny pre hranie hry:", fg="white", bg="black", font=("Century Schoolbook", 17))
            main_label_2.place(x = 100, y = 200)

            text = Text(root_frame, height=20, width=70)
            text.place(x = 370, y = 200)

            rules = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quam ex, pharetra ac risus eu, hendrerit placerat lacus. Nulla eget vestibulum elit. Mauris consequat, diam a gravida condimentum, lorem tellus volutpat velit, a suscipit velit augue id dolor. Aenean nec risus tellus. Sed ullamcorper commodo sapien eu fermentum. Donec sapien mi, tempor vitae dignissim at, sagittis eu nisi. Quisque pharetra sem vitae hendrerit pulvinar. Suspendisse sit amet commodo arcu. Nulla vel urna consequat, fermentum ipsum non, vestibulum nulla.

                        Nunc cursus fringilla sollicitudin. Vestibulum nec orci in quam ultricies sollicitudin et vel massa. Sed euismod nunc in pulvinar faucibus. Etiam sapien magna, sagittis nec fermentum a, suscipit et est. Nulla mollis posuere fermentum. Cras commodo aliquet sem id pretium. Vivamus pellentesque facilisis est a euismod. Nulla id maximus augue. Maecenas eget justo turpis.

                        Proin nec ultrices nisl. Duis arcu ligula, pharetra non arcu eget, ultricies condimentum nulla. Donec feugiat sed ipsum vitae bibendum. Nam a lacus augue. Cras nisi nisi, vulputate ac malesuada ut, pretium vitae ipsum. Nunc lacinia, odio vitae ullamcorper facilisis, dolor ante lacinia erat, vitae facilisis tellus dolor ut orci. Proin sit amet facilisis nulla. Mauris lectus felis, mattis dapibus mollis sed, sollicitudin non lectus. Duis imperdiet pulvinar. """

            SchemeButton().place(x = 450, y = 535)

            btn_next = Button(root_frame, text="Pokyny mám prečítané, môžem ísť hrať!", command=ThirdPage)
            btn_next.place(x = 520, y = 535)

            text.insert(END, rules)

        user_name_get = user_name.get()

        user_label.destroy()
        user_name.destroy()
        btn_user_name.destroy()

        main_label = Label(root_frame, text=user_name_get + ", vitajte na pracovisku vlakového dispečingu pre trať Prievidza - Kraľovany", fg="white", bg="black", font=("Century Schoolbook", 17))
        main_label.place(x = 120, y = 200)

        btn = Button(root_frame, text="POĎME NA TO!", command=SecondPage)
        btn.place(x = 450, y = 300)


    user_label = Label(root_frame, text="Zadajte svoje meno", fg="white", bg="black", font=("Century Schoolbook", 25))
    user_label.place(x = 330, y = 200)

    user_name = Entry(root_frame)
    user_name.place(x = 420, y = 310)

    btn_user_name = Button(root_frame, text="ENTER", command=FirstPageWithNames)
    btn_user_name.place(x = 550, y = 305)

FirstPage()
root_frame.mainloop()