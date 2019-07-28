# -*- coding: utf-8 -*-

from tkinter import *


class Light:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()
        self.window.title("Lichtschalter")

        # Label im Hauptfenster erstellen
        self.label = Label(master=self.window, width=50, height=5)
        self.label.pack()

        # Button im Hauptfenster erstellen und Methode angeben, die beim Klicken ausgeführt werden soll
        self.button = Button(master=self.window, text="O/I", command=self.switch)
        self.button.pack(pady=10, padx=10)

        # Ausgangsstatus setzen und Methode einmal ausführen
        self.on = False
        self.switch()

        # Hauptfenster anzeigen
        self.window.mainloop()

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
