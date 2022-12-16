from tkinter import Button, W
from PIL import ImageTk, Image

"""
    Custom buttons menu widget, that presents different options with image as an background
"""


class ButtonsMenu:
    def __init__(self, root):
        self.root = root

    def createbuttonsmenu(self, images, funcs):
        if len(images) != len(funcs):
            raise Exception(
                "The number of functions and elements doesn't match")

        self.images = []
        self.btns = []
        for i in range(len(images)):
            img = ImageTk.PhotoImage(
                Image.open(images[i]))
            self.images.append(img)

            btn = Button(self.root, image=img,
                         command=funcs[i], bg="white", bd=0, padx=5, pady=5)
            btn.grid(row=0, column=i, sticky=W)
