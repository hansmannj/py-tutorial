import random
import string
from tkinter import *


class Sehtest:

    # Konstruktor, der das Fenster aufbaut
    def __init__(self):
        self.window = Tk()
        self.window.title("Sehtest")
        self.window.config(bg="black")  # Hintergrundfarbe
        # window.attributes("-fullscreen", True)

        self.interval = Entry(master=self.window)
        self.interval.pack()

        # Leere Liste mit Labels vorbereiten und mit self von aussen zugänglich machen
        self.labels = []

        # Leere Labels vorbereiten, ins window packen und zur Liste hinzufügen
        for fontsize in range(100, 0, -20):
            label = Label(
                master=self.window,
                font=("Arial", fontsize),
                width=6
            )
            label.pack()
            self.labels.append(label)

        # Button erstellen. Command ist der Link auf die Funktion,
        # die bei Betätigung ausgeführt werden soll (mit self!)
        button = Button(master=self.window,
                        text="Neue Buchstaben",
                        command=self.neuebuchstaben)
        button.pack(pady=10, padx=10)

        # Einmal die Methode 'neuebuchstaben()' ausführen, damit beim Start
        # bereits Zufallsbuchstaben angefüllt sind
        self.neuebuchstaben()

        # mainloop
        self.window.mainloop()

    def zufallsbuchstaben(self):
        # Methode fürs Generieren der formatierten Zufallsbuchstaben
        return " ".join(random.choices(string.ascii_uppercase, k=3))

    def neuebuchstaben(self):
        # Methode, um den Text der Labels zu ändern
        # Alle labels sind in der Liste self.labels verfügbar


        try:
            step = int(self.interval.get())
        except:
            step = 20

        fontsize = 100

        for label in self.labels:
            label.config(
                text=self.zufallsbuchstaben(),
                bg="black",
                fg=random.choice(["red", "blue", "yellow", "green"]),
                font=("Arial", fontsize)
            )
            fontsize -= step


# Programm ausführen
Sehtest()
