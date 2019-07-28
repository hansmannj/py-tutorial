# -*- coding: utf-8 -*-

import math

from tkinter import *


class Circle:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()
        self.window.title("Kreis")

        # Eingabefeld
        self.input = Entry(master=self.window, width=30)
        self.input.pack(pady=10, padx=20)

        # Buttons
        self.circumference = Button(master=self.window, text="Umfang", command=self.calc_circumference)
        self.area = Button(master=self.window, text="Fläche", command=self.calc_area)
        self.diameter = Button(master=self.window, text="Durchmesser", command=self.calc_diameter)

        self.circumference.pack()
        self.area.pack()
        self.diameter.pack()

        # Message
        self.message = Label(master=self.window)
        self.message.pack(pady=10, padx=20)

        # Fenster anzeigen
        self.window.mainloop()

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
