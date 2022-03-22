import random
import string
from tkinter import *


class Lichtschalter:

    # Konstruktor, der das Fenster aufbaut
    def __init__(self):
        self.window = Tk()
        self.window.title("Lichtschalter")
        self.window.geometry("500x300")
        self.window.config(
            bg="black"
        )  # Hintergrundfarbe am Anfang = schwarz, Licht ist ausgeschaltet
        self.is_on = False

        self.label = Label(
            master=self.window,
            text="Licht ist ausgeschaltet",
            font=("Arial", 30),
            fg="white",
            bg="black"
        )
        self.label.pack(pady=80, padx=10)

        # Button erstellen. Command ist der Link auf die Funktion,
        # die bei Betätigung ausgeführt werden soll (mit self!)
        self.button = Button(master=self.window, text="Ein", command=self.switch)
        self.button.pack(pady=10, padx=10)

        # mainloop
        self.window.mainloop()

    def switch(self):
        # Zustand des Lichts ins Gegenteil umwandeln.
        # Also "aus", wenn es "ein" ist und "ein", wenn es "aus" ist.
        self.is_on = not self.is_on

        if self.is_on:
            self.label.config(text="Licht ist eingeschaltet.", bg="yellow", fg="black")
            self.window.config(bg="yellow")
            self.button.config(text="Aus")
        else:
            self.label.config(text="Licht ist ausgeschaltet.", bg="black", fg="white")
            self.window.config(bg="black")
            self.button.config(text="Ein")


# Programm ausführen
Lichtschalter()
