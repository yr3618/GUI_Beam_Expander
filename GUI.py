
from tkinter import *
from PIL import Image, ImageTk





#FUNCTION FOR THE INPUT



#This function is used to change btw windows
def change(root, action):
    root.destroy()
    if action== "Beam expander":
         beam()
    if action== "h":
        welcome()
    if action== "Interferometer":
        interferometer()




def call():
    root=Tk()
    start(root)
    root.mainloop()


def welcome():
    root=Tk()
    welcome_screen(root)
    root.mainloop()

def welcome_screen(root):
    global Image, pic, choice, a
    root.title("Lego photonics")
    root.geometry("400x400")
    root.configure(bg="white")
    image = Image.open('GUILOGO.png')
    resize = image.resize((100, 50), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(resize)
    mylabel=Label(root, image=pic).place(x=10, y=10)
    hello=Label(root, text="Hello! Thank you for using our prototypes! Please select which one you would like to use now", wraplength=400, justify="center", bg="white")
    hello.place(x=200, y=100, anchor='center')
    clicked=StringVar()
    clicked.set("Choose")
    dropt=OptionMenu(root, clicked, "Beam expander", "Interferometer"). place(x=200, y=150, anchor='center')
    Submit=Button(root, text="Submit", command=lambda : change(root, clicked.get())).place(x=200, y=190, anchor='center')


def beam():
    root=Tk()
    beam_(root)
    root.mainloop


def beam_(root):
    global Image, image2, pic2, resize2
    def click():

        global my_string_var
        entered_text=textentry.get() #Collect Text
        my_string_var = StringVar()
        try:
            M = float(entered_text)
            if 0.5 <= M <= 2:


                tosay="Okay!"
                my_string_var.set("Okay!")
            else:
                my_string_var.set("We are sorry but we cannot perform this at the moment.")
        except ValueError:
            my_string_var.set("You idiot you need a number ")
        magnification=Label(root, textvariable = my_string_var, justify='center', bg="white")
        magnification.place(x=200, y=220, anchor='center')


    root.title("Lego photonics")
    root.geometry("400x400")
    root.configure(bg="white")
    image2 = Image.open('GUILOGO.png')
    resize2 = image2.resize((100, 50), Image.ANTIALIAS)
    pic2 = ImageTk.PhotoImage(resize2)
    mylabel=Label(root, image=pic2).place(x=10, y=10)
    beam=Label(root, text="Our LEGO variable beam expander can perform magnification between 0.5 and 2. Please enter which magnification you desire to perform.", wraplength=400, justify="center", bg="white")
    beam.place(x=200, y=100, anchor='center')
    home="h"
    #Text Box
    textentry=Entry(root, width=20, bg="#C6C2F0")
    textentry.place(x=200, y=150, anchor='center')
    a=textentry.get()
    sub=Button(root, text="Submit", width=6, command=click).place(x=200, y=180, anchor='center')
    go_home=Button(root, text="Home screen", command=lambda : change(root, home)).place(x=200, y=350, anchor='center')

def interferometer():
    root=Tk()
    interferometer_(root)
    root.mainloop


def interferometer_(root):
    global image3, pic3
    root.title("Lego photonics")
    root.geometry("400x400")
    root.configure(bg="white")
    image3 = Image.open('GUILOGO.png')
    resize3 = image3.resize((100, 50), Image.ANTIALIAS)
    pic3 = ImageTk.PhotoImage(resize3)
    mylabel=Label(root, image=pic3).place(x=10, y=10)
    beam=Label(root, text="Our interferometer is not available yet. Thank you for choosing us.", wraplength=400, justify="center", bg="white")
    beam.place(x=200, y=100, anchor='center')
    home="h"
    go_home=Button(root, text="Home screen", command=lambda : change(root, home)).place(x=200, y=350, anchor='center')




welcome()
