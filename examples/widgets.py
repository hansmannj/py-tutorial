# -*- coding: utf-8 -*-

from tkinter import *


class Properties:

    def __init__(self):
        """Form.
        """

        window = Tk()
        window.title("Properties")

        # Die zwei Variablen, die durch Benutzerinteraktion geändert werden können
        # Sie werdem mit ihren jeweiligen Widgets verknüpft und können von aussen gelesen und geschrieben werden.
        self.text = StringVar()
        self.upper = IntVar()

        # Der ganze Rest ist dann nur Darstellung
        self.label = Label(master=window, width=40)
        self.label.pack(pady=10, padx=10)

        eingabe = Entry(master=window, width=20, textvariable=self.text)
        eingabe.pack(padx=10, pady=10)

        check = Checkbutton(master=window, state="normal", variable=self.upper)
        check.pack(padx=10, pady=10)

        # Bei command steht, welche Funktion bei Betätigung des Buttons aufgerufen werden soll
        button = Button(master=window, text="Auswerten", command=self.on_click)
        button.pack(padx=10, pady=10)

        window.resizable(width=False, height=False)
        window.mainloop()

    def on_click(self):
        """Funktion.
        """

        # Dank der Notation mit self können wir direkt auf Objekte aus der __init__ Funktion zugreifen

        # Text aus der dem Eingabefeld zugeordneten Variable auslesen
        text = self.text.get()

        # Testen, ob Checkbox aktiviert ist
        if self.upper.get():
            text = text.upper()

        # Text im Label ändern
        self.label.config(text=text)


Properties()
