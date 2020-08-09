from tkinter import *


class Events:

    def __init__(self):
        window = Tk()
        window.title("Events")

        button = Label(master=window, text="Click me!", width=25, background="light grey")
        button.pack(pady=20, padx=20)

        button.bind(sequence="<Button-1>", func=self.leftclick)
        button.bind(sequence="<Button-3>", func=self.rightclick)

        window.mainloop()

    def rightclick(self, event):
        event.widget.config(text="Rechts")

    def leftclick(self, event):
        event.widget.config(text="Links")


Events()
