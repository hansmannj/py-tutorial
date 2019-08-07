# -*- coding: utf-8 -*-


import tkinter.filedialog
from tkinter import *


class Filebrowser:

    def __init__(self):
        self.window = Tk()
        self.window.title("Filebrowser")

        self.textarea = Text(master=self.window, wrap=WORD, font=("Courier New", 20), width=25, height=10)
        self.textarea.pack(pady=10, padx=10, side=TOP, fill=BOTH)

        self.frame = Frame(master=self.window)
        self.frame.pack(pady=10, padx=10, side=BOTTOM, fill=BOTH)

        self.btn_open = Button(master=self.frame, text="Load File", command=self.open_file)
        self.btn_open.pack(side=LEFT)

        self.btn_sort = Button(master=self.frame, text="Sort Text", command=self.sort_text)
        self.btn_sort.pack(side=LEFT, padx=10)

        self.btn_save = Button(master=self.frame, text="Save Text", command=self.save_text)
        self.btn_save.pack(side=RIGHT)

        self.vornamen = None

        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def open_file(self):
        # Filebrowser öffnen
        quelle = tkinter.filedialog.askopenfilename()

        # Clear
        self.textarea.delete(1.0, END)
        self.vornamen = []

        # Datei einlesen
        with open(quelle, "r") as lesezugriff:
            zeilen = lesezugriff.readlines()

        # Vornamen extrahieren und anzeigen
        for zeile in zeilen:
            nachname, vorname = zeile.strip().split(" ")
            self.vornamen.append(vorname)
            self.textarea.insert(INSERT, vorname + "\n")

    def sort_text(self):
        # Bestehende Anzeige clearen
        self.textarea.delete(1.0, END)

        # Und sortiert wieder anzeigen
        for vn in sorted(self.vornamen):
            self.textarea.insert(INSERT, vn + "\n")

    def save_text(self):
        ziel = tkinter.filedialog.asksaveasfilename()
        data = self.textarea.get("1.0", END).encode("utf-8")
        with open(ziel, "w") as schreibzugriff:
            schreibzugriff.write(data)


Filebrowser()
