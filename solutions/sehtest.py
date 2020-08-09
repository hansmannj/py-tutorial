import string
from random import choice
from tkinter import *


class Vision:

    def __init__(self):
        # Konstruktor

        # Hauptfenster
        window = Tk()
        window.title("Sehtest")

        abc = string.ascii_uppercase

        # Labels
        Label(master=window, font=("Arial", 100), width=6,
              text=choice(abc) + " " + choice(abc) + " " + choice(abc)).pack()
        Label(master=window, font=("Arial", 80), width=6,
              text=choice(abc) + " " + choice(abc) + " " + choice(abc)).pack()
        Label(master=window, font=("Arial", 60), width=6,
              text=choice(abc) + " " + choice(abc) + " " + choice(abc)).pack()
        Label(master=window, font=("Arial", 40), width=6,
              text=choice(abc) + " " + choice(abc) + " " + choice(abc)).pack()

        # Fenster anzeigen
        window.mainloop()


Vision()
