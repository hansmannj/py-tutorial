# -*- coding: utf-8 -*-

import random
from tkinter import *


class Programm:
    """Bauplan für mein Programm.
    """

    def __init__(self):
        # GUI aufbauen

        self.color_list = ["red", "blue", "pink", "green", "lime"]

        self.fenster = Tk()
        self.fenster.title("Mein Programm")

        self.label = Label(master=self.fenster, height=5, width=40, text="Ich bin ein Label")
        self.label.config(bg="black", fg="red")
        self.label.pack(pady=10, padx=10)

        self.eingabe = Entry(master=self.fenster, width=50)
        self.eingabe.pack(pady=10, padx=10)

        self.button = Button(master=self.fenster, text="Click me!", command=self.click)
        self.button.pack(pady=10, padx=10)

        self.color = Button(master=self.fenster, text="Farbe wechseln", command=self.change_color)
        self.color.pack(pady=10, padx=10)

        self.fenster.mainloop()

    def change_color(self):
        self.label.config(bg=random.choice(self.color_list))
        self.label.config(fg=random.choice(self.color_list))

    def click(self):
        benutzereinabe = self.eingabe.get()
        self.label.config(text=benutzereinabe)


Programm()
