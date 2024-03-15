import random
import string
from tkinter import *


class Sehtest:

    def __init__(self):
        window = Tk()
        window.title("Sehtest")
        self.my_labels = []
        window.geometry("800x1000")
        for i in range(4):
            buchstaben = random.choices(string.ascii_uppercase, k=3)
            label = Label(
                master=window, width=10, text=buchstaben, font=("Arial", int(100 - (i * 20)))
            )
            label.pack(padx=10, pady=10)
            self.my_labels.append(label)

        window.mainloop()


Sehtest()
