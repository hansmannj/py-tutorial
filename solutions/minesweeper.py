# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        Minesweeper
# Purpose:     Game
#
# Author:      Lernende swisstopo
#
# History:     2019-07-28 ported to Python 3.7
#
# Created:     02.02.2018
# Copyright:   (c) swisstopo
# -------------------------------------------------------------------------------

import tkinter.messagebox
from random import *
from tkinter import *


class Game:
    """Bauplan für das gesamte Spiel.
    """

    def __init__(self, size):

        # Klassenvariablen initialisieren
        self.size = size
        self.counter = None
        self.bomb_list = None

        # Hauptfenster
        self.window = Tk()
        self.window.title("Minesweeper")

        # Icon
        try:
            self.window.iconbitmap(bitmap=r"..\resources\bombe.ico")
        except Exception:
            print("Icon not found")

        # Menu einbinden
        self.menu()

        # Frame für Spielfeld
        self.playground = Frame(master=self.window)
        self.playground.pack(side=TOP, pady=10, padx=10)

        # Statuszeile
        self.statusbar = Label(master=self.window)
        self.statusbar.pack(side=BOTTOM, pady=10, padx=10)

        # Spielfeld aufbauen
        self.reset()

        # Hauptfenster fixieren und anzeigen
        self.window.minsize(width=250, height=0)
        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def menu(self):

        # Menubar erstellen und ins Hauptfenster hängen
        menubar = Menu(master=self.window)
        self.window.config(menu=menubar)

        # Menu 'Datei' ertellen
        m_datei = Menu(master=menubar, tearoff=False)
        menubar.add_cascade(label="Spiel", menu=m_datei)

        # Menupunkte für Datei-Menu erstellen
        m_datei.add_command(label="Neustart", command=self.reset)
        m_datei.add_separator()
        m_datei.add_command(label="Beenden", command=self.quit)

        # Menu 'Einstellungen' erstellen
        m_config = Menu(master=menubar, tearoff=False)
        menubar.add_cascade(label="Einstellungen", menu=m_config)

        # Menupunkte für Einstellungs-Menu erstellen
        m_config.add_command(label="Spielfeldgrösse", command=self.config)

        # Menu 'Hilfe' ertellen
        m_help = Menu(master=menubar, tearoff=False)
        menubar.add_cascade(label="?", menu=m_help)

        # Menupunkte für Hilfe-Menu erstellen
        m_help.add_command(label="About", command=about)
        m_help.add_command(label="Spielregeln", command=rules)

    def config(self):

        # Neues Fenster erstellen
        cfg_window = Tk()
        cfg_window.title("Spielfeldgrösse")

        # Icon
        try:
            cfg_window.iconbitmap(bitmap="bombe.ico")
        except Exception:
            print("Icon not found")

        # Methode definieren, die nur für dieses Fenster benötigt werden
        def adopt():
            self.size = cfg_slider.get()
            cfg_window.destroy()
            self.reset()

        # Slider mit minimal und maximal möglicher Spielfeldgrösse
        cfg_slider = Scale(master=cfg_window, orient=HORIZONTAL, from_=3, to=25)
        cfg_slider.set(self.size)  # Standardwert ist die aktuell eingestellte Grösse
        cfg_slider.pack(side=TOP, pady=10, padx=10)

        cfg_ok = Button(master=cfg_window, text="Spiel neu starten", command=adopt)
        cfg_ok.pack(side=RIGHT, pady=10, padx=10)

        cfg_cancel = Button(master=cfg_window, text="Abbrechen", command=cfg_window.destroy)
        cfg_cancel.pack(side=BOTTOM, pady=10, padx=10)

        cfg_window.resizable(width=False, height=False)
        cfg_window.mainloop()

    def quit(self):
        if tkinter.messagebox.askyesno("Beenden", "Willst du das Spiel wirklich abbrechen?"):
            self.window.destroy()

    def reset(self):

        self.counter = 0

        # Liste mit zufälligen Koordinaten erstellen
        self.bomb_list = set()
        while len(self.bomb_list) < self.size:
            self.bomb_list.add((choice(range(self.size)), choice(range(self.size))))

        # Bestehendes Spielfeld räumen
        for cell in self.playground.winfo_children():
            cell.destroy()

        # Spielfeld aufbauen aus x*y Zellen
        for x in range(self.size):
            for y in range(self.size):
                Cell(self, x, y)

        self.statusbar.config(text="Spiel läuft", fg="dark green")

    def check(self, x, y):

        if (x, y) in self.bomb_list:
            # Prüfen, ob sich hier eine Bombe befindet
            return "Bomb"
        else:
            # Anzahl Bomben in den umliegenden Zellen zählen
            anzahl = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (x + dx, y + dy) in self.bomb_list:
                        anzahl += 1
            return anzahl


def rules():
    tkinter.messagebox.showinfo("Spielregeln",
                                "Linksklick auf ein Feld deckt es auf. Wenn sich dahinter eine Bombe versteckt, "
                                "hast du verloren. Falls das Feld frei ist, wird die Anzahl Bomben in den angrenzenden "
                                "acht Spielfeldern angezeigt. Mit Rechtsklick kannst du ein Feld markieren, von dem du "
                                "vermutest, dass es eine Bombe enthält. Viel Spass!")


def about():
    tkinter.messagebox.showinfo("About",
                                "Dieses Programm wurde im Rahmen des Kurses 'Python für Lernende swisstopo' 2019 "
                                "entwickelt. Alle Rechte Vorbehalten. Viel Spass!")


class Cell:
    """Bauplan für eine einzelne Zelle.
    """

    def __init__(self, game, x, y):
        # Klassenvariablen initialisieren
        self.x = x
        self.y = y
        self.game = game

        # Button erstellen und im Grid an entsprechender x,y Position anzeigen
        button = Label(master=self.game.playground, width=2, height=1, background="light gray")
        button.grid(column=x, row=y, padx=1, pady=1)

        # Funktionen an den Button binden:
        # Linksklick: aufdecken
        # Rechtsklick: markieren
        button.bind(sequence="<Button-1>", func=self.explore)
        button.bind(sequence="<Button-3>", func=self.mark)

    @staticmethod
    def mark(event):
        # Feld orange einfärben
        if event.widget["state"] == "normal":
            event.widget.config(bg="orange", text="?")

    def explore(self, event):

        def popup(title, message):
            # Messagebox wenn Spiel verloren. Neustart oder nochmals?
            if tkinter.messagebox.askyesno(title, message):
                self.game.style()
            else:
                self.game.window.destroy()

        def reveal(color):
            # alle Felder aufdecken und Bomben rot einfärben, wenn Spiel verloren wurde
            for col, row in self.game.bomb_list:
                for widget in self.game.playground.grid_slaves(row, col):
                    widget.config(bg=color, text="X", state="disabled")

        # Da der Button weiss, an welcher Posision er sich befindet,
        # kann er die Methode check aus der Klasse Game fragen, was sich genau
        # an seiner Position und in den umliegenden Feldern befindet.

        result = self.game.check(self.x, self.y)

        if result == "Bomb":
            # Falls eine Bombe getroffen wurde:
            # - Alle Bomben rot einfärben und disablen (reveal), Game Over anzeigen
            # - Messagebox öffnen und Benutzer fragen, ob er ein neues Spiel
            #   starten oder das Programm beenden möchte

            reveal(color="red")
            self.game.statusbar.config(text="Game over!", fg="red")
            popup(title="Game Over!",
                  message="Du hast {} Felder aufgedeckt.\nNochmals versuchen?".format(self.game.counter))

        elif event.widget["state"] == "normal":
            # Falls das Feld frei ist und noch nie angeklickt wurde:
            # - Feld grün einfärben und disablen.
            # - Anzahl Punkte aktualisieren
            event.widget.config(bg="lime", state="disabled", text=result)
            self.game.counter += 1

            # Gewonnen, wenn alle Felder abgeräumt
            if self.game.counter == self.game.size ** 2 - self.game.size:
                reveal(color="dark green")
                self.game.statusbar.config(text="Du hast gewonnen".format(self.game.counter))
                popup(title="Gewonnen!",
                      message="Du hast alle Felder aufgedeckt.\nNochmals spielen?")
            else:
                self.game.statusbar.config(text="Du hast {} Felder abgeräumt".format(self.game.counter))


# Spiel starten mit einer Spielfeldgrösse von 10*10
Game(10)
