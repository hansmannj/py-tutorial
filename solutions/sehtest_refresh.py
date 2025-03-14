import random
import string
from tkinter import *


class SehtestRefresh:

    # Konstruktor, der das Fenster aufbaut
    def __init__(self):
        self.window = Tk()
        self.window.title("Sehtest")
        self.window.config(bg="white")  # Hintergrundfarbe
        # self.window.attributes("-fullscreen", True)

        # Leere Liste mit Labels vorbereiten und mit self von aussen zugänglich machen
        self.labels = []

        # Leere Labels vorbereiten, ins window packen und zur Liste hinzufügen
        for fontsize in range(100, 0, -20):
            label = Label(master=self.window, font=("Arial", fontsize), width=6, bg="white")
            label.pack()
            self.labels.append(label)

        # Button erstellen. Command ist der Link auf die Funktion,
        # die bei Betätigung ausgeführt werden soll (mit self!)
        button = Button(master=self.window, text="Neue Buchstaben", command=self.refresh)
        button.pack(pady=10, padx=10)

        # Einmal die Methode 'refresh()' ausführen, damit beim Start
        # bereits Zufallsbuchstaben angefüllt sind
        self.refresh()

        # mainloop
        self.window.mainloop()

    def refresh(self):
        # Methode, um den Text der Labels zu ändern
        # Alle labels sind in der Liste self.labels verfügbar

        for label in self.labels:
            label.config(text=" ".join(random.choices(string.ascii_uppercase, k=3)))


# Programm ausführen
SehtestRefresh()
