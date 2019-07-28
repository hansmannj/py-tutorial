# -*- coding: utf-8 -*-

import json
from tkinter import *

import urllib2


class Change:

    def __init__(self):
        # window
        self.window = Tk()
        self.window.title("Währungsrechner")

        # textvariables
        self.chf = DoubleVar()
        self.currency = StringVar()
        self.output = StringVar()

        # widgets
        Label(master=self.window, text="Bitte Betrag in CHF eingeben", width=40).pack(pady=5)
        Entry(master=self.window, textvariable=self.chf).pack(padx=5)
        eur_button = Radiobutton(master=self.window, text="Euro", value="EUR", variable=self.currency)
        eur_button.pack()
        eur_button.select()  # Euro ist schon angewählt bei start.
        usd_button = Radiobutton(master=self.window, text="US-Dollar", value="USD", variable=self.currency)
        usd_button.pack()

        self.button = Button(master=self.window, text="Berechnen", command=self.calculate)
        self.button.pack(pady=5)
        Label(master=self.window, textvariable=self.output).pack(pady=5)

        # Get current rates
        try:
            self.rates = self.get_rates()
        except:
            self.output.set("Kurse konnten nicht geladen werden")
            self.rates = {"EUR": 0.85977,
                          "USD": 1.071}
            # self.button.config(state="disabled")

        # Show window
        self.window.mainloop()

    def calculate(self):
        try:
            chf = self.chf.get()
            currency = self.currency.get()
            result = str(chf * self.rates[currency])
            self.output.set(result + " " + currency)
        except Exception:
            self.output.set("Eingabe ungültig")

    @staticmethod
    def get_rates():
        response = urllib2.urlopen("https://api.fixer.io/latest?base=CHF&symbols=USD,EUR")
        result = json.load(response)
        return result["rates"]


change = Change()
