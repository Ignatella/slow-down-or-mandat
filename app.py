from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

import os
import webbrowser
import detector

import mymenu as mn
import myframe as mf
import buttonsmenu as btm
import myscrollableview as msv


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Slow down or mandat - AO")
        self.root.geometry("800x600")
        self.root.config(bg="white")
        self.allImages = []
        self.allRes = []
        self.current = 0
        self.size = (400, 300)

    def donothing(self):
        pass

    def openfile(self):
        self.mainImg.grid_forget()
        self.file = filedialog.askopenfilename(title="Open file", filetypes=[
            ("PNG files", "*.png"),
            ("JPG files", "*.jpg")])
        try:
            im = Image.open(self.file)
            im.thumbnail(self.size, Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(im)
            self.mainImg = Label(self.mff, image=self.img, bg="white")
            self.mainImg.grid(row=0, column=0)
        except:
            messagebox.showerror(
                "Error", "An error has occured while opening the file")

    def loadfilesfromdir(self):
        dir = filedialog.askdirectory()
        fi = filter(lambda f: f.endswith(("png", "jpg")), os.listdir(dir))
        for f in fi:
            self.addToScrollable(f'{dir}/{f}')

    def addToScrollable(self, fi=""):
        try:
            if fi != "":
                self.allImages.append(fi)
                res = detector.perform_detection(fi)
                self.allRes.append(res)
            else:
                self.allImages.append(self.file)
                res = detector.perform_detection(self.file)
                self.allRes.append(res)
            self.msview = msv.MyScrollableView(self.lff)
            self.msview.showimages(self.allImages, self.allRes)
            self.msview.display(0, 0)
        except:
            messagebox.showerror(
                "Error", "An error has occured while performing operation")

    def arrowClick(self, mode):
        if len(self.allImages) > 0:
            if mode == "L":
                self.current -= 1
                if self.current < 0:
                    self.current = len(self.allImages)-1
            elif mode == "R":
                self.current += 1
                if self.current >= len(self.allImages):
                    self.current = 0
            im = Image.open(self.allImages[self.current])
            im.thumbnail(self.size, Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(im)
            self.mainImg = Label(self.mff, image=self.img, bg="white")
            self.mainImg.grid(row=0, column=0)
        else:
            messagebox.showerror("Error", "No images loaded")

    def draw(self):
        m = mn.MyMenu(self.root)
        m.submenu("File", ["Open file", "Export to CSV", "Load from directory"], [
                  self.openfile, self.donothing, self.loadfilesfromdir])
        m.submenu("Info", ["About", "Help"], [lambda: messagebox.showinfo(
            "Authors", "Ignacy\nKacper\nPiotr"), lambda: webbrowser.open("https://github.com/Ignatella/slow-down-or-mandat#readme")])

        buttonsFrame = mf.MyFrame(self.root)
        self.frm = buttonsFrame.createframe()
        btnmenu = btm.ButtonsMenu(self.frm)
        btnmenu.createbuttonsmenu(
            ["./assets/icons8-less-than-48.png", "./assets/icons8-more-than-48.png", "./assets/icons8-open-document-48.png", "./assets/icons8-export-csv-48.png", "./assets/icons8-licence-plate-48.png", "./assets/icons8-numbers-input-form-48.png"], [lambda:self.arrowClick("L"), lambda:self.arrowClick("R"), self.openfile, lambda: print("CSV export"), self.addToScrollable, self.loadfilesfromdir])
        buttonsFrame.display(0, 0, columnspan=2)

        mainFrame = mf.MyFrame(self.root)
        self.mff = mainFrame.createframe()
        self.mainImg = Label(
            self.mff, text="Main image", bg="white")
        self.mainImg.grid(row=0, column=0)
        mainFrame.display(2, 1, columnspan=2)

        leftFrame = mf.MyFrame(self.root)
        self.lff = leftFrame.createframe()
        msview = msv.MyScrollableView(self.lff)
        msview.showimages(self.allImages, self.allRes)
        msview.display(0, 0)
        leftFrame.display(2, 0, columnspan=1)
        m.configroot()
        self.root.grid_columnconfigure(4, weight=1)
        self.root.mainloop()


a = App()

a.draw()
