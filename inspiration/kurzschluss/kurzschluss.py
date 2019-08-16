# -------------------------------------------------------------------------------
# Name:        Kurzschluss
# Purpose:     Fun
#
# Author:      Jonas und Renas, Lernende swisstopo
#
# History:     2019-08-15 created
#
# Copyright:   (c) swisstopo
# -------------------------------------------------------------------------------

import time
from tkinter import *


class Licht:

    def __init__(self):

        self.window = Tk()
        self.window.title("Lichtschalter")
        self.window.geometry("800x600")
        # self.window.attributes('-fullscreen', True)

        self.light_on = False
        self.timestamps = []

        self.images = {
            "on": PhotoImage(file="switch_on.png"),
            "off": PhotoImage(file="switch_off.png")
        }

        self.frame = Frame(master=self.window)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label = Label(self.frame, font=("Bahnschrift Bold", 100))
        self.label.pack(pady=50)

        self.button = Button(self.frame, command=self.click, borderwidth=0, image=self.images["off"])
        self.button.pack(pady=10)

        self.style()  # with default parameters

        self.window.minsize(width=800, height=600)
        self.window.mainloop()

    def style(self, image="off", bgcolor="black", fgcolor="white", text="Licht aus", state=NORMAL):
        self.window.config(bg=bgcolor)
        self.frame.config(bg=bgcolor)
        self.label.config(bg=bgcolor, fg=fgcolor, text=text)
        self.button.config(bg=bgcolor, activebackground=bgcolor, image=self.images[image], state=state)

    def short_circuit(self, stamp, clicks=10):
        # elapsed time of the last 10 clicks
        self.timestamps.append(stamp)
        if len(self.timestamps) > clicks:
            self.timestamps.pop(0)
        elapsed = self.timestamps[-1] - self.timestamps[0]
        if len(self.timestamps) == clicks and elapsed < clicks // 2:
            return True

    def click(self):
        if self.short_circuit(time.time()):
            self.style(image="off", bgcolor="red", fgcolor="white", text="Kurzschluss", state=DISABLED)
            self.window.after(2000, self.style)
            self.timestamps = []
        elif self.light_on:
            self.style()  # with default parameters
        else:
            self.style(image="on", bgcolor="yellow", fgcolor="black", text="Licht an")
        self.light_on = not self.light_on


Licht()
