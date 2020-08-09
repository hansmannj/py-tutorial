# -*- coding: utf-8 -*-

from tkinter import *


class Controlvars:

    def __init__(self):
        # Hauptfenster
        window = Tk()
        window.title("Kontrollvariablen")

        # Dynamische Variable im Hauptfenster registrieren
        dynamischer_text = StringVar()

        # Zwei Labels erstellen, deren Texte sich auf die dynamische Veriable beziehen
        label1 = Label(master=window, width=20, textvariable=dynamischer_text)
        label1.pack()

        label2 = Label(master=window, width=20, textvariable=dynamischer_text)
        label2.pack()

        # Ein Eingabefeld erstellen, das den dynamischen Text ändert
        eingabe = Entry(master=window, width=50, textvariable=dynamischer_text)
        eingabe.pack(pady=10, padx=10)

        # Hauptfenster anzeigen
        window.mainloop()


# Programm ausführen
Controlvars()
