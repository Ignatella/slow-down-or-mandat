from tkinter import scrolledtext
from PIL import ImageTk, Image
from tkinter.constants import INSERT, END, WORD, DISABLED

"""
    Custom scrollable view that presents images
"""


class MyScrollableView:
    def __init__(self, root):
        self.root = root
        self.scr = scrolledtext.ScrolledText(
            self.root, wrap=WORD, width=20, bg=None)
        self.images = []

    def showimages(self, images, results):
        self.scr.delete('1.0', END)
        self.images = []
        if len(images) != len(results):
            raise Exception(
                "The number of functions and elements doesn't match")

        for i in range(len(images)):
            img = ImageTk.PhotoImage(Image.open(images[i]).resize((64, 64)))
            self.scr.image_create(INSERT, padx=5, pady=5, image=img)
            self.scr.insert(INSERT, f'  {results[i]}')
            self.scr.insert(INSERT, '\n')
            self.images.append(img)

    def display(self, row, column, columnspan=1):
        self.scr.config(state=DISABLED)
        self.scr.grid(row=row, column=column, columnspan=columnspan)
