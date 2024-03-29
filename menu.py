import customtkinter as ctk
from menuitem import MenuItem


class Menu(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = args[0]
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.logo_label = ctk.CTkLabel(
            self, text="Menu", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.menu_button_1 = MenuItem(self, text="Open file", light_image="./assets/icons8-open-document-48.png",
                                      dark_image="./assets/icons8-open-document-dark-mode-48.png", command=self.root.load_file, fg_color="transparent")
        self.menu_button_1.grid(row=1, column=0, sticky="ew")
        self.menu_button_2 = MenuItem(self, text="Export to CSV", light_image="./assets/icons8-export-csv-48.png",
                                      dark_image="./assets/icons8-export-csv-dark-mode-48.png", command=self.root.export_to_csv, fg_color="transparent")
        self.menu_button_2.grid(row=2, column=0, sticky="ew")
        self.menu_button_3 = MenuItem(self, text="Load from directory", light_image="./assets/icons8-numbers-input-form-48.png",
                                      dark_image="./assets/icons8-numbers-input-form-dark-mode-48.png", command=self.root.load_files_from_dir, fg_color="transparent")
        self.menu_button_3.grid(row=3, column=0, sticky="ew")
        self.menu_button_4 = MenuItem(self, text="Add to scrollbar", light_image="./assets/icons8-add-new-48.png",
                                      dark_image="./assets/icons8-add-new-dark-mode-48.png", command=self.root.add_to_scrollbar, fg_color="transparent")
        self.menu_button_4.grid(row=4, column=0, sticky="ew")
        self.menu_button_5 = MenuItem(self, text="Remove from scrollbar", light_image="./assets/icons8-trash-can-48.png",
                                      dark_image="./assets/icons8-trash-can-dark-mode-48.png", command=self.root.remove_from_scrollbar, fg_color="transparent")
        self.menu_button_5.grid(row=5, column=0, sticky="ew")
        self.appearance_mode_label = ctk.CTkLabel(
            self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self, values=["Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(
            row=8, column=0, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
