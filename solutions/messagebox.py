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

    @staticmethod
    def info():
        tkinter.messagebox.showinfo("Infobox", "Ich bin eine Infobox")

    @staticmethod
    def yesno():
        result = tkinter.messagebox.askyesno("Ja - Nein", "Alles paletti?")
        print(result)

    @staticmethod
    def retry():
        result = tkinter.messagebox.askretrycancel("Nochmals", "Nochmals versuchen?")
        print(result)


Messages()
