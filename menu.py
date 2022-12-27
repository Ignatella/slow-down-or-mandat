import customtkinter as ctk
from menuitem import MenuItem


class Menu(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = args[0]
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.logo_label = ctk.CTkLabel(
            self, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.menu_button_1 = MenuItem(self, text="Open file", light_image="./assets/icons8-open-document-48.png",
                                      dark_image="./assets/icons8-open-document-dark-mode-48.png", command=self.root.openfile, fg_color="transparent")
        self.menu_button_1.grid(row=1, column=0, sticky="ew")
        self.menu_button_2 = MenuItem(self, text="Export to CSV", light_image="./assets/icons8-export-csv-48.png",
                                      dark_image="./assets/icons8-export-csv-dark-mode-48.png", command=None, fg_color="transparent")
        self.menu_button_2.grid(row=2, column=0, sticky="ew")
        self.menu_button_3 = MenuItem(self, text="Load from directory", light_image="./assets/icons8-numbers-input-form-48.png",
                                      dark_image="./assets/icons8-numbers-input-form-dark-mode-48.png", command=self.root.loadfilesfromdir, fg_color="transparent")
        self.menu_button_3.grid(row=3, column=0, sticky="ew")
        self.menu_button_4 = MenuItem(self, text="Add to scrollbar", light_image="./assets/icons8-licence-plate-48.png",
                                      dark_image="./assets/icons8-licence-plate-48.png", command=self.root.addToScrollbar, fg_color="transparent")
        self.menu_button_4.grid(row=4, column=0, sticky="ew")
        self.appearance_mode_label = ctk.CTkLabel(
            self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self, values=["Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(
            row=6, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
