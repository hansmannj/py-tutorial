from tkinter import *
from tkinter import messagebox


class Game:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.score = None
        self.player = "X"

        self.winners = (
            {"00", "01", "02"},  # row 0
            {"10", "11", "12"},  # row 1
            {"20", "21", "22"},  # row 2
            {"00", "10", "20"},  # col 0
            {"01", "11", "21"},  # col 1
            {"02", "12", "22"},  # col 2
            {"00", "11", "22"},  # \
            {"02", "11", "20"}  # /
        )

        # Frame für Spielfeld
        self.playground = Frame(master=self.window)
        self.playground.pack(side=TOP, pady=10, padx=10)

        # Statuszeile
        self.statusbar = Label(master=self.window)
        self.statusbar.pack(side=BOTTOM, pady=10, padx=10)

        # Spielfeld aufbauen
        for x in range(3):
            for y in range(3):
                Cell(self, x, y)

        # Spielstand auf Anfang setzen
        self.reset()

        # Hauptfenster fixieren und anzeigen
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def reset(self):

        self.score = {
            "0": set(),
            "X": set()
        }

        for cell in self.playground.winfo_children():
            cell.config(text="", state="normal")


class Cell:
    """Bauplan für eine einzelne Zelle.
    """

    def __init__(self, game, x, y):
        # Klassenvariablen initialisieren
        self.x = x
        self.y = y
        self.game = game

        # Button erstellen und im Grid an entsprechender x,y Position anzeigen
        button = Label(master=self.game.playground, width=2, height=1, background="light gray", font=("Arial", 40))
        button.grid(column=x, row=y, padx=1, pady=1)

        # Funktionen an den Button binden
        button.bind(sequence="<Button-1>", func=self.click)

    def click(self, event):

        def popup(title, message):
            # Messagebox wenn Spiel beendet.
            if messagebox.askyesno(title, message):
                self.game.reset()
            else:
                self.game.window.destroy()

        if event.widget["state"] == "normal":

            event.widget.config(text=self.game.player, state="disabled")
            self.game.score[self.game.player].add(f"{self.x}{self.y}")

            if len([j for i in self.game.score.values() for j in i]) == 9:
                self.game.statusbar.config(text="Unentschieden")
                popup(title="Unentschieden",
                      message="Unentschieden\nNochmals spielen?")

            else:
                for winner in self.game.winners:
                    if winner.issubset(self.game.score[self.game.player]):
                        self.game.statusbar.config(text=f"Spieler {self.game.player} hat gewonnen")
                        popup(title=f"Spieler {self.game.player} hat gewonnen!",
                              message=f"Spieler {self.game.player} hat gewonnen!\nNochmals spielen?")
                        break

            # switch player
            self.game.player = list(self.game.score)[not bool(list(self.game.score).index(self.game.player))]
            self.game.statusbar.config(text=f"Spieler {self.game.player} ist an der Reihe", fg="dark green")


# Spiel starten
Game()
