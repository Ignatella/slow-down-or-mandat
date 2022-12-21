import customtkinter as ctk
from PIL import Image

class ImageNavigation(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.left_arrow_image = ctk.CTkImage(light_image=Image.open("./assets/icons8-less-than-48.png"), dark_image=Image.open("./assets/icons8-less-than-dark-mode-48.png"), size=(30, 30))
        self.left_arrow_button = ctk.CTkButton(self, corner_radius=0, width=30, height=30, border_spacing=10, text=None,
                                       fg_color="transparent", image=self.left_arrow_image, anchor="w", command=None)
        self.left_arrow_button.grid(row=0, column=0, padx=20)
        self.right_arrow_image = ctk.CTkImage(light_image=Image.open("./assets/icons8-more-than-48.png"), dark_image=Image.open("./assets/icons8-more-than-dark-mode-48.png"), size=(30, 30))
        self.right_arrow_button = ctk.CTkButton(self, corner_radius=0, width=30, height=30, border_spacing=10, text=None,
                                       fg_color="transparent", image=self.right_arrow_image, anchor="w", command=None)
        self.right_arrow_button.grid(row=0, column=2, padx=20)