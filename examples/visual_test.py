import string
from random import *
from tkinter import *


class Vision:

    def __init__(self):
        # Konstruktor

        # Hauptfenster
        self.window = Tk()
        self.window.title("Sehtest")

        # Liste mit Labels
        self.labels = [Label(master=self.window, font=("Arial", 100), width=6),
                       Label(master=self.window, font=("Arial", 80), width=6),
                       Label(master=self.window, font=("Arial", 60), width=6),
                       Label(master=self.window, font=("Arial", 40), width=6)]

        # Labels anzeigen
        for l in self.labels:
            l.pack()

        # Button
        self.button = Button(master=self.window, text="new", command=self.refresh)
        self.button.pack(pady=10)

        # Methode 'refresh' einmal ausfuehren, dass Anfangswerte sichtbar sind
        self.refresh()

        # Fenster anzeigen
        self.window.mainloop()

    def refresh(self):
        # Methode, die ausgefuehrt wird, wenn Button geklickt wird

        # Alphabet
        abc = string.ascii_uppercase

        # Fuer alle Labes Zufallsbuchstaben generieren
        for l in self.labels:
            l.config(text=choice(abc) + " " + choice(abc) + " " + choice(abc))


Vision()
