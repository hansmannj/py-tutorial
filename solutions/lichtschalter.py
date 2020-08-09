# -*- coding: utf-8 -*-

from tkinter import *


class Light:

    def __init__(self):

        # Hauptfenster
        window = Tk()
        window.title("Lichtschalter")

        # Label im Hauptfenster erstellen
        self.label = Label(master=window, width=50, height=5)
        self.label.pack()

        # Button im Hauptfenster erstellen und Methode angeben, die beim Klicken ausgeführt werden soll
        button = Button(master=window, text="O/I", command=self.switch)
        button.pack(pady=10, padx=10)

        # Ausgangsstatus setzen und Methode einmal ausführen
        self.on = False
        self.switch()

        # Hauptfenster anzeigen
        window.resizable(width=False, height=False)
        window.mainloop()

    def switch(self):
        # Je nach Status Label und Hintegrund anpassen
        if self.on:
            self.label.config(text="Licht ein", fg="black", bg="yellow")
        else:
            self.label.config(text="Licht aus", fg="white", bg="black")

        # Neuen Status in der Variable speichern
        self.on = not self.on


# Programm ausführen
Light()
