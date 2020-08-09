# -*- coding: utf-8 -*-

from tkinter import *


class Gui:

    def __init__(self):
        # Hauptfenster
        window = Tk()

        # Titel
        window.title("Widgets")

        frame = LabelFrame(master=window, text=" Frame ", relief=GROOVE, borderwidth=1, )
        frame.pack(padx=10, pady=10)

        # Label
        label = Label(master=frame, text="Eingabe")
        label.pack(padx=10, pady=10, side=LEFT)

        # Eingabe

        eingabe = Entry(master=frame, width=30)
        eingabe.pack(padx=10, pady=10, side=LEFT)

        # Button
        button = Button(master=window, width=10, text="Klick me!")
        button.pack(padx=10, pady=10)

        # Radio Button
        radio = Radiobutton(master=window, state="active")
        radio.pack(padx=10, side=LEFT)

        # Checkbox
        check = Checkbutton(master=window, state="normal")
        check.pack(padx=10, side=LEFT)

        # Fenster fixieren
        # window.resizable(width=False, height=False)

        # Fenster darstellen
        window.mainloop()


Gui()
