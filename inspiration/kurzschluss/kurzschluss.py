# -*- coding: utf-8 -*-

import time
from tkinter import *


class Licht:

    def __init__(self):

        self.window = Tk()
        self.window.title("Lichtschalter")
        self.window.attributes('-fullscreen', True)

        self.light_on = False
        self.bgcolor = "black"
        self.fgcolor = "white"
        self.counter = 0
        self.kurzschluss = False
        self.image = PhotoImage(file="switch_{}.png".format(int(self.light_on)))

        self.frame = Frame(master=self.window)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label = Label(self.frame, font=("Bahnschrift Bold", 110))
        self.label.pack(padx=50, pady=50)

        self.button = Button(self.frame, command=self.click, borderwidth=0)
        self.button.pack(padx=10, pady=10)

        self.reset()

        self.window.mainloop()

    def reset(self):
        self.bgcolor = "black"
        self.light_on = False
        self.image = PhotoImage(file="switch_{}.png".format(int(self.light_on)))
        self.window.config(bg=self.bgcolor)
        self.frame.config(bg=self.bgcolor)
        self.label.config(bg=self.bgcolor, fg=self.fgcolor, text="Licht aus")
        self.button.config(bg=self.bgcolor, activebackground=self.bgcolor,
                           image=self.image)
        self.kurzschluss = False
        self.counter = 0

    def click(self):
        if not self.kurzschluss:

            self.counter += 1

            if self.light_on == 1:
                self.image = PhotoImage(file="switch_{}.png".format(int(self.light_on)))
                self.light_on = 0
                self.label.config(text="Licht aus", fg="white", bg="black")
                self.button.config(bg="black", image=self.image, activebackground="black")
            else:
                self.image = PhotoImage(file="switch_{}.png".format(int(self.light_on)))
                self.light_on = 1
                self.label.config(text="Licht an", fg="black", bg="yellow")
                self.button.config(bg="yellow", image=self.image, activebackground="yellow")

            if self.counter == 0:
                self.start = time.time()

            if self.counter == 10:
                self.end = time.time()
                if self.end - self.start < 2:
                    self.label.config(text="Hör uf !", bg="red", fg="white")
                    self.button.config(bg="red", activebackground="red")
                    self.kurzschluss = True
                    self.window.after(3000, self.reset)
                else:
                    self.counter = 0


Licht()
