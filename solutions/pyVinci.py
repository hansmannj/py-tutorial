import io
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfile

from PIL import Image


# parts of this code are inspired by https://tkdocs.com/tutorial/canvas.html
# and https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06
class PyVinci:

    def __init__(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.geometry("1000x1000")
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=4)
        self.window.title("pyVinci")
        self.line_color = "black"
        self.line_size = 5
        self.lastx = None
        self.lasty = None

        # Buttom zum Starten des Farbwahl-Dialogs für die Stiftfarbe
        self.color_button = Button(master=self.window, text="Stiftfarbe", command=self.color_picker)
        self.color_button.grid(column=0, row=0, padx=20, pady=0)

        # Label, dass die aktuell gewählte Stiftfarbe anzeigt
        self.current_color_label = Label(master=self.window, bg=self.line_color, text="  ")
        self.current_color_label.grid(column=0, row=1, pady=5)

        # Schieberegler, um die Stiftgrösse auszuwählen
        self.size_selector = Scale(
            self.window, label='Stiftgrösse', orient='horizontal', from_=1, to=15
        )
        self.size_selector.grid(column=1, row=0, padx=20, pady=0)
        # Stiftgrösse bei Programmstart soll initialem Wert von self.line_size entsprechen
        self.size_selector.set(self.line_size)

        # Buttom, um den "Datei speichern"-Dialog zu öffnen
        self.save_button = Button(master=self.window, text="Speichern", command=self.save_to_file)
        self.save_button.grid(column=2, row=0, padx=20, pady=0)

        # Die Zeichenfläche
        self.canvas = Canvas(self.window, width=1000, height=900, bg="white")
        self.canvas.grid(columnspan=3, row=2)
        self.canvas.bind("<Button-1>", self.save_posn)
        self.canvas.bind("<B1-Motion>", self.add_line)

        self.window.mainloop()

    def save_posn(self, event):
        self.lastx = event.x
        self.lasty = event.y

    def add_line(self, event):
        self.line_size = self.size_selector.get()
        self.canvas.create_line(
            self.lastx,
            self.lasty,
            event.x,
            event.y,
            fill=self.line_color,
            width=self.line_size,
            capstyle="round"
        )
        self.save_posn(event)

    def color_picker(self):
        color = askcolor(title="Bitte Stiftfarbe wählen")
        self.line_color = color[1]
        self.current_color_label.configure(bg=self.line_color)

    def save_to_file(self):
        filename = asksaveasfile(mode='w', defaultextension=".jpeg")
        if filename:
            # Abspeichern in Postscript und konvertieren zu jpeg. Inspiriert von hier:
            # https://stackoverflow.com/questions/41940945/saving-canvas-from-tkinter-to-file
            ps = self.canvas.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.save(filename, 'jpeg')


PyVinci()
