import time
from tkinter import *


class Schalter:

    def __init__(self):
        self.window = Tk()
        self.window.title("Lichtschalter")

        self.is_on = True
        self.clicks = []

        self.label = Label(
            master=self.window,
            width=50,
            height=10
        )
        self.label.pack()

        button = Button(
            master=self.window,
            text="I/O",
            command=self.switch
        )
        button.pack()

        self.switch()

        self.window.mainloop()

    def switch(self):

        if len(self.clicks) >= 10:
            self.clicks.pop(0)
        self.clicks.append(time.time())
        print(self.clicks)

        if len(self.clicks) == 10:
            diff = max(self.clicks) - min(self.clicks)
            print(diff)
            if diff < 5:
                self.label.config(text="Kurzschluss", bg="red", fg="white")
                return

        if self.is_on:
            self.label.config(text="Das Licht ist aus", bg="black", fg="white")
            self.is_on = False
        else:
            self.label.config(text="Das Licht ist ein", bg="yellow", fg="black")
            self.is_on = True


Schalter()
