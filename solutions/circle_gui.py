# -*- coding: utf-8 -*-

import math

from tkinter import *


class Circle:

    def __init__(self):
        """ In dieser Methode steht Hier
        """


        # Hauptfenster
        window = Tk()
        window.title("Kreis")

        # Eingabefeld
        self.input = Entry(master=window, width=30)
        self.input.pack(pady=10, padx=20)

        # Buttons
        Button(master=window, text="Umfang", command=self.calc_circumference).pack()
        Button(master=window, text="Fläche", command=self.calc_area).pack()
        Button(master=window, text="Durchmesser", command=self.calc_diameter).pack()

        # Resultat
        self.message = Label(master=window)
        self.message.pack(pady=10, padx=20)

        # Fenster anzeigen
        window.mainloop()

    def check_input(self):
        try:
            self.radius = float(self.input.get())
            return True
        except Exception:
            self.message.config(text="Ungültige Eingabe", fg="red")
            return False

    def calc_diameter(self):
        if self.check_input():
            self.message.config(text=str(self.radius * 2), fg="green")

    def calc_circumference(self):
        if self.check_input():
            self.message.config(text=str(self.radius * 2 * math.pi), fg="green")

    def calc_area(self):
        if self.check_input():
            self.message.config(text=str(self.radius ** 2 * math.pi), fg="green")


Circle()
