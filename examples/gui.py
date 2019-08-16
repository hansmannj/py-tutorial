# Modul importieren
from tkinter import *


# Bauplan definieren
class Gui:

    def __init__(self):
        # Hauptfenster
        window = Tk()

        # Titel
        window.title("GUI")

        # Button
        button = Button(master=window, width=10, text="Klick me!")
        button.pack(padx=10, pady=10)

        # Frame
        frame = LabelFrame(master=window, text="Mein Frame", relief=GROOVE, borderwidth=1)
        frame.pack(padx=10, pady=10)

        # Label
        label = Label(master=frame, width=30, text="Ich bin ein Label", font=("Arial", 20))
        label.pack(padx=10, pady=10)

        # Eingabe
        eingabe = Entry(master=frame, width=30)
        eingabe.pack(padx=10, pady=10)

        # Fenster fixieren
        window.resizable(width=False, height=False)

        # Fenster darstellen
        window.mainloop()


# Programm ausführen
Gui()
