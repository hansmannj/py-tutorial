import tkinter.messagebox
from tkinter import *


class Messages:

    def __init__(self):
        self.window = Tk()
        self.window.title("Box")

        self.btn_info = Button(master=self.window, text="Infobox", command=self.info)
        self.btn_info.pack(pady=10, padx=10, side=LEFT)

        self.btn_yesno = Button(master=self.window, text="Yes/No", command=self.yesno)
        self.btn_yesno.pack(pady=10, padx=10, side=LEFT)

        self.btn_retry = Button(master=self.window, text="Retry", command=self.retry)
        self.btn_retry.pack(pady=10, padx=10, side=LEFT)

        self.window.mainloop()

    def info(self, message="Ich bin eine Infobox"):
        tkinter.messagebox.showinfo("Info", message)

    def yesno(self, message="Alles paletti?"):
        result = tkinter.messagebox.askyesno("Ja - Nein", message)
        if result:
            self.info(message="Das freut micht!")
        else:
            self.info(message="Das ist aber schade")

    def retry(self, message="Nochmals versuchen?"):
        result = tkinter.messagebox.askretrycancel("Nochmals", message)
        if result:
            self.yesno(message="Besser jetzt?")


Messages()
