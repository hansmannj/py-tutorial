# -*- coding: utf-8 -*-

import random
from tkinter import *


class FormVsFunction:

    def __init__(self):
        """ Hier steht nur Form
        """

        window = Tk()
        window.title("Form vs. Funktion")

        Button(master=window, text="Random", command=self.random).pack(padx=5, pady=5)
        self.label = Label(master=window, width=40)
        self.label.pack(padx=5, pady=5)

        window.mainloop()

    def random(self):
        self.label.config(text=str(random.randint(1, 100)))


FormVsFunction()
