import tkinter as tk
import customtkinter as ctk
import os

from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from menu import Menu
from scrollbarlist import ScrollbarList
from imagenavigation import ImageNavigation

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Slow down or mandat - AO")
        self.geometry(f"{800}x{600}")
        self.all_images = []
        self.all_res = []
        self.current = 0
        self.size = (400, 300)
  
    def openfile(self):
        self.main_img.grid_forget()
        self.file = filedialog.askopenfilename(title="Open file", filetypes=[
            ("PNG files", "*.png"),
            ("JPG files", "*.jpg")])
        try:
            im = Image.open(self.file)
            im.thumbnail(self.size, Image.Resampling.LANCZOS)
            self.img = ctk.CTkImage(im, size=im.size)
            self.main_img = ctk.CTkLabel(self, text=None, image=self.img)
            self.main_img.grid(row=1, column=1)
        except Exception as e:
            print(e)
            messagebox.showerror(
                "Error", "An error has occured while opening the file")
            
    def loadfilesfromdir(self):
        dir = filedialog.askdirectory()
        fi = filter(lambda f: f.endswith(("png", "jpg")), os.listdir(dir))
        for f in fi:
            self.scrollbar_list.add_image(f)
            # addToScrollable(f'{dir}/{f}')

    # def addToScrollable(self, fi=""):
    #     try:
    #         if fi != "":
    #             self.allImages.append(fi)
    #         else:
    #             self.allImages.append(self.file)
    #         self.allRes.append(1)
    #         self.msview = msv.MyScrollableView(self.lff)
    #         self.msview.showimages(self.allImages, self.allRes)
    #         self.msview.display(0, 0)
    #     except:
    #         messagebox.showerror(
    #             "Error", "An error has occured while performing operation")

    # def arrowClick(self, mode):
    #     if len(self.allImages) > 0:
    #         if mode == "L":
    #             self.current -= 1
    #             if self.current < 0:
    #                 self.current = len(self.allImages)-1
    #         elif mode == "R":
    #             self.current += 1
    #             if self.current >= len(self.allImages):
    #                 self.current = 0
    #         im = Image.open(self.allImages[self.current])
    #         im.thumbnail(self.size, Image.Resampling.LANCZOS)
    #         self.img = ImageTk.PhotoImage(im)
    #         self.mainImg = Label(self.mff, image=self.img, bg="white")
    #         self.mainImg.grid(row=0, column=0)
    #     else:
    #         messagebox.showerror("Error", "No images loaded")
        
    def draw(self):
        # grid layout settings
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # menu
        self.menu = Menu(self, width=140)
        self.menu.grid(row=0, column=0, rowspan=4, sticky="nwse")
        
        # main image
        self.main_img = ctk.CTkLabel(self, text="Main image")
        self.main_img.grid(row=1, column=1)
        
        self.image_navigation = ImageNavigation(self, fg_color="transparent")
        self.image_navigation.grid(row=2, column=1)
        
        # scrollbar list
        self.scrollbar_list = ScrollbarList(self, width=20)
        self.scrollbar_list.grid(row=0, column=2, rowspan=3, sticky="nwse")
        
        # start event loop
        self.mainloop()
        
        
        
        
if __name__ == "__main__":
    app = App()
    app.draw()    