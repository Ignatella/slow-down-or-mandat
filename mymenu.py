from tkinter import Menu

"""
    Custom menu widget for the project
"""


class MyMenu:
    def __init__(self, root):
        self.root = root
        self.menu = Menu(root)

    def submenu(self, label, elems, funcs):
        submenu = Menu(self.menu, tearoff=0)

        if len(elems) != len(funcs):
            raise Exception(
                "The number of functions and elements doesn't match")

        for i in range(len(elems)):
            submenu.add_command(label=elems[i], command=funcs[i])

        self.menu.add_cascade(label=label, menu=submenu)

    def configroot(self):
        self.root.config(menu=self.menu)
