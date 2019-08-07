# -*- coding: utf-8 -*-

from tkinter import *


class Gui:

    def __init__(self):
        # Hauptfenster
        self.window = Tk()

        # Titel
        self.window.title("GUI")

        # Label
        self.label = Label(master=self.window, width=50, text="Ich bin ein Label")
        self.label.pack(padx=10, pady=10)

        # Eingabe
        self.eingabe = Entry(master=self.window, width=30)
        self.eingabe.pack(padx=10, pady=10)

        # Button
        self.button = Button(master=self.window, width=10, text="Klick me!")
        self.button.pack(padx=10, pady=10)

        # Fenster fixieren
        self.window.resizable(width=False, height=False)

        # Fenster darstellen
        self.window.mainloop()


Gui()
