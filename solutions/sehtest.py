import random
import string
from tkinter import *


class Sehtest:

    def __init__(self):
        window = Tk()
        window.title("Sehtest")
        # window.geometry("500x500")
        for i in range(4):
            buchstaben = random.choices(string.ascii_uppercase, k=3)
            label = Label(
                master=window, width=50, text=buchstaben, font=("Arial", int(100 - (i * 20)))
            )
            label.pack(padx=10, pady=10)
        window.mainloop()


Sehtest()
