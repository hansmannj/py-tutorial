# -*- coding: utf-8 -*-

from tkinter import *

import requests


class Change:

    def __init__(self):
        # window
        self.window = Tk()
        self.window.title("Währungsrechner")

        # textvariables
        self.chf = DoubleVar()
        self.chf.set(1)  # default
        self.currency = StringVar()
        self.output = StringVar()

        # widgets
        Label(master=self.window, text="Bitte Betrag in CHF eingeben", width=40).pack(pady=5)
        Entry(master=self.window, textvariable=self.chf).pack(padx=5)
        eur_button = Radiobutton(master=self.window, text="Euro", value="CHF_EUR", variable=self.currency)
        eur_button.pack()
        eur_button.select()  # Euro ist schon angewählt bei start.
        usd_button = Radiobutton(master=self.window, text="US-Dollar", value="CHF_USD", variable=self.currency)
        usd_button.pack()

        self.button = Button(master=self.window, text="Berechnen", command=self.calculate)
        self.button.pack(pady=5)
        Label(master=self.window, textvariable=self.output).pack(pady=5)

        # Get current rates
        try:
            self.rates = self.get_rates()
            self.output.set("Aktuelle Kurse wurden geladen")
        except Exception:
            self.output.set("Kurse konnten nicht geladen werden")
            self.rates = {"CHF_EUR": 0.85977,
                          "CHF_USD": 1.071}
            # self.button.config(state="disabled")

        # Show window
        self.window.mainloop()

    def calculate(self):
        try:
            chf = self.chf.get()
            currency = self.currency.get()
            result = str(chf * self.rates[currency])
            self.output.set("{} CHF = {} {}".format(chf, result, currency.split("_")[-1]))
        except Exception:
            self.output.set("Eingabe ungültig")

    @staticmethod
    def get_rates():
        service = r"https://free.currconv.com/api/v7/convert"
        params = {"apiKey": "93fc194dc99a31baa8d9",
                  "q": "CHF_EUR,CHF_USD",
                  "compact": "ultra"}

        response = requests.get(service, params)
        return response.json()


change = Change()
