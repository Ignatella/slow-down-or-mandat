import customtkinter as ctk
from PIL import Image


class MenuItem(ctk.CTkFrame):
    def __init__(self, *args, text, light_image, dark_image, command, **kwargs):
        super().__init__(*args, **kwargs)

        self.image = ctk.CTkImage(light_image=Image.open(
            light_image), dark_image=Image.open(dark_image), size=(20, 20))
        self.button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text=text,
                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                    image=self.image, anchor="w", command=command)
        self.button.pack(fill="both")
