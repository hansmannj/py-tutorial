# -*- coding: utf-8 -*-

import random
from tkinter import *


class Strobo:

    def __init__(self):
        window = Tk()
        window.title("Gugugs")
        window.attributes('-fullscreen', True)

        self.width = int(window.winfo_screenwidth() / 2)
        self.height = int(window.winfo_screenheight() / 2)

        label = Frame(master=window, bg="red", height=self.height, width=self.width)
        label.place(x=0, y=0)

        label_two = Frame(master=window, bg="blue", height=self.height, width=self.width)
        label_two.place(x=0, y=self.height)

        label_three = Frame(master=window, bg="yellow", height=self.height, width=self.width)
        label_three.place(x=self.width, y=0)

        label_four = Frame(master=window, bg="green", height=self.height, width=self.width)
        label_four.place(x=self.width, y=self.height)

        window.mainloop()

        # print(int(window.winfo_reqwidth()/2))

        def change_color():
            current_color = label.cget("bg")
            current_color = label_two.cget("bg")
            current_color = label_three.cget("bg")
            current_color = label_four.cget("bg")
            next_color = random.choice(["yellow", "red", "purple", "orange", "lime", "orange",
                                        "cyan", "magenta", "pink", "blue", "green"])
            label.config(bg=next_color)
            label_two.config(bg=next_color)
            label_three.config(bg=next_color)
            label_four.config(bg=next_color)
            window.after(100, change_color)

        # change_color()


Strobo()
