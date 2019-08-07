# -*- coding: utf-8 -*-

from tkinter import *


class Gui:

    def __init__(self):
        # Hauptfenster
        self.window = Tk()

        # Titel
        self.window.title("Widgets")

        self.frame = LabelFrame(master=self.window, text=" Frame ", relief=GROOVE, borderwidth=1, )
        self.frame.pack(padx=10, pady=10)

        # Label
        self.label = Label(master=self.frame, text="Eingabe")
        self.label.pack(padx=10, pady=10, side=LEFT)

        # Eingabe

        self.eingabe = Entry(master=self.frame, width=30)
        self.eingabe.pack(padx=10, pady=10, side=LEFT)

        # Button
        self.button = Button(master=self.window, width=10, text="Klick me!")
        self.button.pack(padx=10, pady=10)

        # Radio Button
        self.radio = Radiobutton(master=self.window, state="active")
        self.radio.pack(padx=10, side=LEFT)

        # Checkbox
        self.check = Checkbutton(master=self.window, state="normal")
        self.check.pack(padx=10, side=LEFT)

        # Fenster fixieren
        # self.window.resizable(width=False, height=False)

        # Fenster darstellen
        self.window.mainloop()


Gui()
