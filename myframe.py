from tkinter import Frame, W


"""
    Custom Frame widget with predefined styling
"""


class MyFrame:
    def __init__(self, root):
        self.root = root

    def createframe(self):
        self.fr = Frame(self.root, bd=0)
        return self.fr

    def display(self, row, column, columnspan=1):
        self.fr.grid(row=row, column=column,
                     columnspan=columnspan, sticky=W, pady=10)
