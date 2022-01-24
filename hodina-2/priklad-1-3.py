from tkinter import Tk, Label, Button

def vypis_textu():
    print("Ahoj ! tlacitko bolo stlacene")

def koniec():
    global win
    win.quit()
    win.withdraw()

win = Tk()
win.geometry('200x150+200+200')
win.title("Ahoj !")

label = Label(win, text="Prvy pokus s TkInter")
label.pack()

greet_button = Button(win, text="Vypis textu", command=vypis_textu)
greet_button.pack()

close_button = Button(win, text="Koniec", command=koniec)
close_button.pack()
win.mainloop()
