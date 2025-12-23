from dataclasses import dataclass
import random

import customtkinter as ctk
from PIL import Image

from Entites import Entity
from Game_work_flow import Battle_logic


@dataclass(frozen=True)
class Battlestyle:
    Bg_navy: str = "#000033"
    Hp_bar_green: str = "#2ecc71"
    HP_bar_red: str = "#e74c3c"
    Font_names: tuple = ("Times New Roman", 22, "bold")
    Font_log: tuple = ("Courier New", 14)
    Btn_move: str = "#1a1a4d"
    Portrait_size: tuple = (100, 100)
    Box_border: str = "#FFFFFF"


class Battlewindow(ctk.CTk):
    def __init__(self, player: Entity, boss: Entity):
        super().__init__()
        self.cfg = Battlestyle()

        self.title(f"Battle {player.name} VS {boss.name}")
        self.geometry("800x600")
        self.configure(fg_color=self.cfg.Bg_navy)
        self.player = player
        self.boss = boss
        self.engine = Battle_logic(player, boss)

        # Grid
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=6)
        self.grid_columnconfigure(0, weight=1)

        # North area
        self.north_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.north_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.north_frame.grid_columnconfigure((0, 1), weight=1)
        self.player_ui = self.create_hp_block(
            self.player, column=0, color=self.cfg.Hp_bar_green
        )
        self.boss_ui = self.create_hp_block(
            self.boss, column=1, color=self.cfg.HP_bar_red
        )

        # south area
        self.south_frame = ctk.CTkFrame(
            self, border_color=self.cfg.Box_border, border_width=2
        )
        self.south_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=30)
        self.south_frame.grid_rowconfigure(0, weight=4)  # Moves display
        self.south_frame.grid_rowconfigure(1, weight=1)  # Logs display
        self.south_frame.grid_columnconfigure(0, weight=1)

        # button grid
        self.moves_container = ctk.CTkFrame(self.south_frame, fg_color="transparent")
        self.moves_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.moves_container.grid_columnconfigure((0, 1), weight=1)
        self.moves_container.grid_rowconfigure((0, 1), weight=1)
        self.create_move_buttons()

        # Action log
        self.action_log = ctk.CTkLabel(
            self.south_frame,
            text="It is your turn...",
            font=self.cfg.Font_log,
            text_color="white",
            anchor="w",
            justify="left",
        )
        self.action_log.grid(row=1, column=0, sticky="sw", padx=20, pady=10)

    def create_hp_block(self, entity, column, color):
        container = ctk.CTkFrame(self.north_frame, fg_color="transparent")
        container.grid(row=0, column=column, padx=10, sticky="nsew")

        # Portrait
        try:
            img = ctk.CTkImage(
                Image.open(entity.image_path), size=self.cfg.Portrait_size
            )
            ctk.CTkLabel(container, image=img, text="").pack(side="left", padx=10)
        except Exception:
            ctk.CTkLabel(container, text="[IMG]", width=100, height=100).pack(
                side="left", padx=10
            )

        # Text and Bar area
        stats_box = ctk.CTkFrame(container, fg_color="transparent")
        stats_box.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(
            stats_box, text=entity.name.upper(), font=self.cfg.Font_names
        ).pack(anchor="w")

        # Progress Bar
        bar = ctk.CTkProgressBar(stats_box, progress_color=color, width=250)
        bar.set(entity.hp / entity.max_hp)
        bar.pack(pady=5, anchor="w")

        # HP Text Label (e.g., "4500/5600")
        hp_text = ctk.CTkLabel(
            stats_box, text=f"{entity.hp}/{entity.max_hp}", font=("Arial", 12)
        )
        hp_text.pack(anchor="w")

        return {"bar": bar, "text": hp_text}

    def create_move_buttons(self):
        for i, move in enumerate(self.player.moves[:]):
            pp_text = "∞" if move.pp < 0 else str(move.pp)
            button = ctk.CTkButton(
                self.moves_container,
                text=f"{move.name.upper()}\n(PP: {pp_text})",
                font=("Arial", 14, "bold"),
                fg_color=self.cfg.Btn_move,
                command=lambda m=move: self.handle_click(m),
            )
            button.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

    def handle_click(self, move):
        """Handles player move and manages turn sequence."""
        if self.player.hp <= 0 or self.boss.hp <= 0:
            return  # Battle is over
            
        # Check if move has PP left (allow -1 for infinite PP)
        if move.pp == 0:
            self.type_message(f"{move.name} is out of PP!")
            return
            
        # 1. Player's turn
        result = self.engine.execute_attack(self.player, self.boss, move)
        self.type_message(result)
        self.update_bars()
        self.update_move_buttons()  # Update PP display
        
        # 2. Check if boss is defeated
        if self.boss.hp <= 0:
            self.after(2000, lambda: self.type_message(f"Victory! {self.boss.name} has been defeated!"))
            self.disable_buttons()
            self.after(4000, self.destroy)  # Close window after 4 seconds
            return
            
        # 3. Boss's turn (after a delay)
        self.after(2000, self.boss_turn)
        
    def boss_turn(self):
        """Executes boss's turn."""
        if self.boss.hp <= 0:
            return
            
        # Boss picks a random move
        boss_move = random.choice(self.boss.moves)
        result = self.engine.execute_attack(self.boss, self.player, boss_move)
        self.type_message(result)
        self.update_bars()
        
        # Check if player is defeated
        if self.player.hp <= 0:
            self.after(2000, lambda: self.type_message(f"Defeat! {self.player.name} has been defeated!"))
            self.disable_buttons()
            self.after(4000, self.destroy)  # Close window after 4 seconds
            
    def update_move_buttons(self):
        """Updates move button text to show current PP."""
        for i, widget in enumerate(self.moves_container.winfo_children()):
            if isinstance(widget, ctk.CTkButton) and i < len(self.player.moves):
                move = self.player.moves[i]
                pp_text = "∞" if move.pp < 0 else str(move.pp)
                widget.configure(text=f"{move.name.upper()}\n(PP: {pp_text})")
                # Only disable button if PP is exactly 0 (not negative)
                if move.pp == 0:
                    widget.configure(state="disabled")
                    
    def disable_buttons(self):
        """Disables all move buttons when battle ends."""
        for widget in self.moves_container.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(state="disabled")

    def type_message(self, full_text, current_index=0):
        if current_index <= len(full_text):
            self.action_log.configure(text=f"> {full_text[:current_index]}")
            self.after(30, self.type_message, full_text, current_index + 1)

    def update_bars(self):
        """Refreshes HP stats on GUI."""
        self.player_ui["bar"].set(self.player.hp / self.player.max_hp)
        self.player_ui["text"].configure(text=f"{self.player.hp}/{self.player.max_hp}")

        self.boss_ui["bar"].set(self.boss.hp / self.boss.max_hp)
        self.boss_ui["text"].configure(text=f"{self.boss.hp}/{self.boss.max_hp}")

    def start(self):
        self.mainloop()
