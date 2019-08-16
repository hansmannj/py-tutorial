import tkinter.messagebox
from tkinter import *


class Messages:

    def __init__(self):
        window = Tk()
        window.title("Box")

        btn_info = Button(master=window, text="Infobox", command=self.info)
        btn_info.pack(pady=15, padx=15, side=LEFT)

        btn_yesno = Button(master=window, text="Yes/No", command=self.yesno)
        btn_yesno.pack(pady=15, padx=50, side=LEFT)

        btn_retry = Button(master=window, text="Retry", command=self.retry)
        btn_retry.pack(pady=15, padx=15, side=LEFT)

        window.mainloop()

    def info(self, message="Ich bin eine Infobox"):
        tkinter.messagebox.showinfo("Info", message)

    def yesno(self, message="Alles paletti?"):
        result = tkinter.messagebox.askyesno("Ja - Nein", message)
        if result == True:
            self.info(message="Das freut micht!")
        else:
            self.info(message="Das ist aber schade")

    def retry(self, message="Nochmals versuchen?"):
        result = tkinter.messagebox.askretrycancel("Nochmals", message)
        if result:  # Kurzschreibweise für 'if result == True'
            self.yesno(message="Besser jetzt?")


Messages()