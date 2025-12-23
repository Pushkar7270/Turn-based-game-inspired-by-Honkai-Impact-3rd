from dataclasses import dataclass

import customtkinter as ctk
from PIL import Image

from Entites import Entity


@dataclass(frozen=True)
class Selectionstyle:  # color/format pallette (just defined the formatting of the GUI)
    Bg_Navy: str = "#000033"
    Box_white: str = "#FFFFFF"
    Text_dark: str = "#000000"
    Border_color: str = "#FFFFFF"
    Btn_navy: str = "#000055"
    Font_header: tuple = ("Times New Roman", 28, "bold")
    Font_stats: tuple = ("Arial", 14, "bold")


class SelectionWindow(ctk.CTk):
    def __init__(self, entities: list[Entity], title_text: str):
        super().__init__()
        self.cfg = Selectionstyle()

        # window config
        self.title(title_text)
        self.geometry("1000x750")
        self.configure(fg_color=self.cfg.Bg_Navy)
        self.entities = entities
        self.final_choice = None

        # 1Page title
        self.title_label = ctk.CTkLabel(
            self, text=title_text, font=self.cfg.Font_header, text_color="white"
        )
        self.title_label.pack(pady=20)
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self, fg_color="transparent", width=950, height=600
        )
        self.scrollable_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Config of 2 coloumn grid
        self.scrollable_frame.grid_columnconfigure((0, 1), weight=1)
        self.generate_profiles()

    def generate_profiles(self):
        for i, entity in enumerate(self.entities):
            profile_box = ctk.CTkFrame(
                self.scrollable_frame,
                fg_color=self.cfg.Box_white,
                border_color=self.cfg.Border_color,
                border_width=2,
                corner_radius=12,
            )
            profile_box.grid(row=i // 2, column=i % 2, padx=20, pady=20, sticky="nsew")
            profile_box.grid_columnconfigure((0, 1), weight=1)

            try:
                pil_image = Image.open(entity.image_path)
                ctk_image = ctk.CTkImage(pil_image, size=(180, 220))
                img_label = ctk.CTkLabel(profile_box, image=ctk_image, text="")
                img_label.grid(row=0, column=0, padx=15, pady=15)
            except Exception:
                placeholder = ctk.CTkLabel(
                    profile_box, text="[NO IMAGE]", text_color="gray"
                )
                placeholder.grid(row=0, column=0, padx=15, pady=15)

            stats_side = ctk.CTkFrame(profile_box, fg_color="transparent")
            stats_side.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

            stats_info = (
                f"Name: {entity.name.upper()}\n\n"
                f"Hp : {entity.max_hp}\n"
                f"Speed : {entity.speed}\n"
                f"Defence : {entity.defence}\n"
                f"Crit Rate: {entity.crit_rate}\n"
            )
            stats_label = ctk.CTkLabel(
                stats_side,
                text=stats_info,
                font=self.cfg.Font_stats,
                text_color=self.cfg.Text_dark,
                justify="left",
            )
            stats_label.pack(pady=(10, 20), anchor="w")

            # the select button
            select_button = ctk.CTkButton(
                stats_side,
                text="Select",
                font=self.cfg.Font_stats,
                fg_color=self.cfg.Btn_navy,
                hover_color=self.cfg.Btn_navy,
                command=lambda e=entity: self.on_select(e),
            )
            select_button.pack(side="bottom", fill="x", pady=10)

    def on_select(self, entity: Entity):
        self.final_choice = entity
        self.destroy()

    def get_result(self):
        self.mainloop()
        return self.final_choice
