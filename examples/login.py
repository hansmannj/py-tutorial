from tkinter import *


class Login:

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

        btn_cancel = Button(master=self.window, text="Cancel", width=10)
        btn_cancel.bind(sequence="<Button-1>", func=self.cancel)
        btn_cancel.pack(padx=10, pady=10, side=LEFT)

        btn_login = Button(master=self.window, text="Login", width=10)
        btn_login.pack(padx=10, pady=10, side=RIGHT)

        btn_login.bind(sequence="<Button-1>", func=self.login)

        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def cancel(self, event):
        self.window.destroy()

    def login(self, event):
        pass


Login()
