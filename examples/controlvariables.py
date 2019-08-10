# -*- coding: utf-8 -*-

from tkinter import *


class Controlvars:

    def __init__(self):
        # Hauptfenster
        self.window = Tk()
        self.window.title("Kontrollvariablen")

        # Dynamische Variable im Hauptfenster registrieren
        self.dynamischer_text = StringVar()

        # Zwei Labels erstellen, deren Texte sich auf die dynamische Veriable beziehen
        self.label1 = Label(master=self.window, width=20, textvariable=self.dynamischer_text)
        self.label1.pack()

        self.label2 = Label(master=self.window, width=20, textvariable=self.dynamischer_text)
        self.label2.pack()

        # Ein Eingabefeld erstellen, das den dynamischen Text ändert
        self.eingabe = Entry(master=self.window, width=50, textvariable=self.dynamischer_text)
        self.eingabe.pack(pady=10, padx=10)

        # Hauptfenster anzeigen
        self.window.mainloop()


# Programm ausführen
Controlvars()
