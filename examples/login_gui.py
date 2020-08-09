# -*- coding: utf-8 -*-

import hashlib
from tkinter import *


class Login:

    def __init__(self):
        self.users = {"Elias": "81dc9bdb52d04dc20036dbd8313ed055",
                      "Paula": "d93591bdf7860e1e4ee2fca799911215",
                      "Felix": "39cec6d4d21b5dade7544dab6881423e"}

        window = Tk()
        window.title("Login")

        self.name = Entry(master=window, width=30)
        self.name.focus_set()
        self.password = Entry(master=window, width=30, show="*")

        # self.button = Button(master=self.window, text="Login", command=self.login)
        self.button = Button(master=window, text="Login")

        # Events mit 'bind' an Widget binden. Unter sequence kann angegeben werden,
        # welcher Tastendruck oder Klick den unter func angegebenen Event auslöst.
        self.button.bind(sequence="<Button-1>", func=self.login)
        window.bind(sequence="<Return>", func=self.login)



        self.message = Label(master=window)

        self.name.pack(pady=10, padx=20)
        self.password.pack(pady=10, padx=20)
        self.button.pack(pady=10, padx=20)
        self.message.pack(pady=10, padx=20)

        window.resizable(width=False, height=False)
        window.mainloop()

    def login(self, event):
        print(event)

        # Benutzereingaben abgreifen
        name = self.name.get()
        password = self.password.get()

        # Wenn Benutzer existiert
        if name in self.users.keys():

            # Passwoerter vegleichen (verschluesselt!)
            if hashlib.md5(password.encode("utf-8")).hexdigest() == self.users[name]:
                self.message.config(text="Willkommen " + name, fg="green")
            else:
                self.message.config(text="Falsches Passwort", fg="red")

        # Wenn Benutzer nicht existiert
        else:
            self.message.config(text="Unbekannter Benutzer", fg="orange")


Login()
