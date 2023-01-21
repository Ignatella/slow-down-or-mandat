import customtkinter as ctk
import os


class ScrollbarList(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.images_list = []
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.scrollbar_label = ctk.CTkLabel(
            self, text="Your images", font=ctk.CTkFont(size=20, weight="bold"))
        self.scrollbar_label.grid(
            row=0, column=0, padx=20, pady=20, sticky="nswe")
        self.canvas = ctk.CTkCanvas(self, width=140, highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nswe")
        self.canvas.grid_columnconfigure(0, weight=1)
        self.scrollbar = ctk.CTkScrollbar(self, command=self.canvas.yview)
        self.scrollbar.grid(row=1, column=1, sticky="nswe")
        self.inner_frame = ctk.CTkFrame(self.canvas, corner_radius=0)
        self.inner_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame = self.canvas.create_window(
            (0, 0), window=self.inner_frame, anchor="center")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", self.resize_frame)
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # ctk.CTkLabel(self.inner_frame, text="no images").grid(row=0, column=0, sticky="nswe")
        # for i in range(100):
        #     ctk.CTkButton(self.inner_frame, corner_radius=0, border_spacing=5, text=f"image-name{i}.png",
        #                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30")).pack(fill="both")

    def add_image(self, setImage, image, res=""):
        self.images_list.append(ctk.CTkButton(self.inner_frame, corner_radius=0, border_spacing=5, text=f'{os.path.basename(image)} {res}',
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), command=lambda: setImage(image)))
        self.images_list[-1].pack(fill="both")

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def resize_frame(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
        if event.height > self.inner_frame.winfo_height():
            self.canvas.itemconfig(self.canvas_frame, height=event.height)
