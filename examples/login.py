import hashlib
import json
import tkinter.messagebox
from tkinter import *


class Grid:

    def __init__(self):
        self.window = Tk()

        self.window.title("Login")
        
        self.window.bind(sequence="<Escape>", func=self.cancel)
        self.window.bind(sequence="<Return>", func=self.login)

        frame = LabelFrame(master=self.window, text="Login")
        frame.pack(padx=10, pady=10)

        lbl_user = Label(master=frame, text="Username:")
        lbl_user.grid(row=0, column=0, padx=10, pady=10)

        user = Entry(master=frame, width=30)
        user.grid(row=0, column=1, padx=10, pady=10)
        user.focus()

        lbl_pwd = Label(master=frame, text="Passwort:")
        lbl_pwd.grid(row=1, column=0, padx=10, pady=10)

        pwd = Entry(master=frame, width=30, show="*")
        pwd.grid(row=1, column=1, padx=10, pady=10)

        self.btn_cancel = Button(master=self.window, text="Cancel", width=10)
        self.btn_cancel.bind(sequence="<Button-1>", func=self.cancel)
        self.btn_cancel.pack(padx=10, pady=10, side=LEFT)
        

        self.btn_login = Button(master=self.window, text="Login", width=10, command=self.login)
        self.btn_login.pack(padx=10, pady=10, side=RIGHT)

        
        

        self.btn_login.bind(sequence="<Button-1>", func=self.login)
        

        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def cancel(self, event):
        self.window.destroy()


    def login(self, event):
        self.btn_login.focus()
        username = self.user.get()
        password = hashlib.md5(self.pwd.get().encode("utf-8")).hexdigest()

        # existierende Benutzer laden
        users = self.load_users()

        if (username, password) in users.items():
            tkinter.messagebox.showinfo(title="Login", message="Erfolgreich eingelogged")
            self.window.destroy()
        elif username in users.keys():
            result = tkinter.messagebox.askretrycancel(title="Passwort falsch", message="Ungültiges Passwort")
            if result:
                self.pwd.config(text="")
                self.pwd.focus()
            else:
                self.window.destroy()
        else:
            result = tkinter.messagebox.askretrycancel(title="Unbekannter Benutzer", message="Benutzername unbekannt")
            if result:
                self.user.config(text="")
                self.user.focus()
                self.pwd.config(text="")
            else:
                self.window.destroy()

    @staticmethod
    def load_users():
        with open(r"..\resources\users.json", "r") as r:
            return json.loads(r.read())


# Programm ausführen
Grid()
