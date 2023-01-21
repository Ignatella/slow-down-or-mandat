import tkinter as tk
import customtkinter as ctk
import os

import detector

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from menu import Menu
from scrollbarlist import ScrollbarList
from imagenavigation import ImageNavigation
import csv

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Slow down or mandat - AO")
        self.geometry(f"{800}x{600}")
        self.all_images = []
        self.all_res = {}
        self.current = 0
        self.size = (400, 300)

    def setImage(self, path):
        im = Image.open(path)
        im.thumbnail(self.size, Image.Resampling.LANCZOS)
        self.img = ctk.CTkImage(im, size=im.size)
        if self.main_img:
            self.main_img.grid_forget()
        self.main_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.main_img.grid(row=1, column=1)

    def setRes(self,value):
        self.main_img_result.grid_forget()
        self.main_img_result = ctk.CTkLabel(self, text=value)
        self.main_img_result.grid(row=2, column=1)

    def openfile(self):
        self.main_img.grid_forget()
        self.file = filedialog.askopenfilename(title="Open file", filetypes=[
            ("PNG files", "*.png"),
            ("JPG files", "*.jpg")])
        try:
            self.setImage(self.file)
        except Exception as e:
            if len(self.file) != 0:
                messagebox.showerror(
                    "Error", "An error has occured while opening the file")

    def loadfilesfromdir(self):
        dir = filedialog.askdirectory()
        fi = filter(lambda f: f.endswith(("png", "jpg")), os.listdir(dir))
        for f in fi:
            f_path = f'{dir}/{f}'
            self.all_images.append(f_path)
            res = detector.perform_detection(f_path)
            self.all_res[f_path] = res
            self.scrollbar_list.add_image(
                self.setImage, os.path.basename(f_path), res)

    def addToScrollbar(self):
        fi = self.file
        try:
            if fi not in self.all_images:
                res = detector.perform_detection(fi)
                self.all_images.append(fi)
                self.all_res[fi] = res
                self.scrollbar_list.add_image(
                    self.setImage, os.path.basename(fi), res)
                self.setRes(res)
        except:
            messagebox.showerror(
                "Error", "An error has occured while performing operation")

    def removeFromScrollbar(self):
        self.all_images = []
        self.all_res = {}

        self.scrollbar_list.grid_forget()
        self.scrollbar_list = ScrollbarList(self, width=20)
        self.scrollbar_list.grid(
            row=0, column=2, rowspan=3, sticky="nwse")

        self.main_img.grid_forget()
        self.main_img = ctk.CTkLabel(self, text="Main image")
        self.main_img.grid(row=1, column=1)

        self.setRes("")

    def arrowClick(self, mode):
        if len(self.all_images) > 0:
            if mode == "L":
                self.current -= 1
                if self.current < 0:
                    self.current = len(self.all_images)-1
            elif mode == "R":
                self.current += 1
                if self.current >= len(self.all_images):
                    self.current = 0
            self.setImage(self.all_images[self.current])
            self.setRes(self.all_res[self.all_images[self.current]])
        else:
            messagebox.showerror("Error", "No images loaded")

    def export_to_csv(self):
        filename = filedialog.asksaveasfilename(filetypes=[("Plik csv", "*.csv")], defaultextension = "*.csv")
        if filename:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                header = ("image", "result")
                writer.writerow(header)
                for row in self.all_res.items():
                    writer.writerow(row)

    def draw(self):
        # grid layout settings
        self.grid_columnconfigure(1, weight=7)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # menu
        self.menu = Menu(self, width=140)
        self.menu.grid(row=0, column=0, rowspan=4, sticky="nwse")

        # main image
        self.main_img = ctk.CTkLabel(self, text="Main image")
        self.main_img.grid(row=1, column=1)

        self.main_img_result = ctk.CTkLabel(self, text="")
        self.main_img_result.grid(row=2, column=1)

        self.image_navigation = ImageNavigation(
            self, self, fg_color="transparent")
        self.image_navigation.grid(row=3, column=1)

        # scrollbar list
        self.scrollbar_list = ScrollbarList(self, width=20)
        self.scrollbar_list.grid(
            row=0, column=2, rowspan=3, sticky="nwse")

        # start event loop
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.draw()
