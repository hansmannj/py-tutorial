from tkinter import *
from tkinter import messagebox


class Game:

    def __init__(self):

        # Hauptfenster
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.clicks = None
        self.player = "X"

        self.colors = {"X": "red", "O": "blue"}

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
                # Button erstellen und im Grid an entsprechender x,y Position anzeigen
                button = Label(
                    master=self.playground,
                    width=2,
                    height=1,
                    background="light gray",
                    font=("Arial", 40)
                )
                button.grid(column=x, row=y, padx=1, pady=1)

                # Funktion an den Button binden, wenn Mausklick
                button.bind(sequence="<Button-1>", func=self.click)

        # Spielstand auf Anfang setzen
        self.reset()

        # Hauptfenster fixieren und anzeigen
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def reset(self):

        self.clicks = {"O": set(), "X": set()}

        for cell in self.playground.winfo_children():
            cell.config(text="", state="normal")

        self.statusbar.config(text=f"{self.player} ist dran", fg=self.colors[self.player])

    def click(self, event):
        if not event.widget["text"]:

            event.widget.config(text=self.player, fg=self.colors[self.player])

            g = event.widget.grid_info()
            self.clicks[self.player].add(f"{g['column']}{g['row']}")

            # check for win
            for winner in self.winners:
                if winner.issubset(self.clicks[self.player]):
                    message = f"{self.player} gewinnt"
                    self.statusbar.config(text=message, fg=self.colors[self.player])
                    self.popup(title=message, message=f"{message}\nNochmals spielen?")
                    return

            # switch player
            self.player = list(self.clicks)[not bool(list(self.clicks).index(self.player))]

            if len([j for i in self.clicks.values() for j in i]) == 9:
                message = "Unentschieden"
                self.statusbar.config(text=message, fg="green")
                self.popup(title=message, message=f"{message}\nNochmals spielen?")
            else:
                self.statusbar.config(text=f"{self.player} ist dran", fg=self.colors[self.player])

    def popup(self, title, message):
        # Messagebox wenn Spiel beendet.
        if messagebox.askyesno(title, message):
            self.reset()
        else:
            self.window.destroy()


# Spiel starten
Game()
