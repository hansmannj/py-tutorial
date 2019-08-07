# -*- coding: utf-8 -*-

from tkinter import *


class Events:

    def __init__(self):
        self.window = Tk()
        self.window.title("Events")

        self.label = Label(master=self.window, text="Click me!", width=25)
        self.label.pack(pady=20, padx=20)

        self.label.bind(sequence="<Button-1>", func=self.leftclick)
        self.label.bind(sequence="<Button-3>", func=self.rightclick)

        self.window.mainloop()

    def rightclick(self, event):
        event.widget.config(text="Rechts")

    def leftclick(self, event):
        event.widget.config(text="Links")


Events()
