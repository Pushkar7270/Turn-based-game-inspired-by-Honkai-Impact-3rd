from collections import Counter

import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import File_handler as fh


def get_game_entities(filename):
    from Entites import Entity, Move

    entities = fh.load_data(filename)
    if not entities:
        return None, None

    def dict_to_entity(entity_dict):
        moves_list = [
            Move(name=m["name"], damage=m["damage"], pp=m["pp"])
            for m in entity_dict["moves"]
        ]
        return Entity(
            name=entity_dict["name"],
            hp=entity_dict["hp"],
            moves=moves_list,
            crit_rate=entity_dict["crit_rate"],
            speed=entity_dict["speed"],
            defence=entity_dict["defence"],
            playable=entity_dict["playable"],
            image_path=entity_dict.get("image_path"),
        )

    playable_characters = [dict_to_entity(char) for char in entities["Characters"]]
    bosses = [dict_to_entity(b) for b in entities["Boss"]]
    return playable_characters, bosses


class DataAnalysisWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Game Data Analysis")
        self.state("zoomed")  # Full screen on Windows
        self.configure(fg_color="#1a1a2e")

        # Load data
        self.sim_data = fh.load_data("simulation_data.json") or []
        self.player_data = fh.load_data("player_data.json") or []
        self.characters, self.bosses = get_game_entities("Characters.json")

        self.setup_ui()

    def setup_ui(self):
        # Main scrollable frame
        main_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title_label = ctk.CTkLabel(
            main_frame,
            text="BATTLE DATA ANALYSIS BY CHARACTER",
            font=("Arial", 28, "bold"),
            text_color="white",
        )
        title_label.pack(pady=20)

        # Characters section
        char_title = ctk.CTkLabel(
            main_frame,
            text="VALKYRIES",
            font=("Arial", 24, "bold"),
            text_color="#4ECDC4",
        )
        char_title.pack(pady=(20, 10))

        for character in self.characters:
            self.create_character_frame(main_frame, character, "Character")

        # Bosses section
        boss_title = ctk.CTkLabel(
            main_frame, text="BOSSES", font=("Arial", 24, "bold"), text_color="#FF6B6B"
        )
        boss_title.pack(pady=(40, 10))

        for boss in self.bosses:
            self.create_character_frame(main_frame, boss, "Boss")

    def create_character_frame(self, parent, entity, entity_type):
        # Main character frame
        char_frame = ctk.CTkFrame(parent, fg_color="#00FFFF", corner_radius=15)
        char_frame.pack(fill="x", pady=20, padx=10)

        # Header with image and name
        header_frame = ctk.CTkFrame(char_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=20)

        # Character image
        img_label = ctk.CTkLabel(
            header_frame, text="", width=80, height=80, corner_radius=10
        )
        try:
            from PIL import Image

            img_path = entity.image_path
            pil_img = Image.open(img_path)
            ctk_img = ctk.CTkImage(pil_img, size=(80, 80))
            img_label.configure(image=ctk_img)
        except Exception:
            img_label.configure(
                text=entity.name[:3].upper(),
                fg_color="#2C3E50",
                font=("Arial", 16, "bold"),
                text_color="white",
            )
        img_label.pack(side="left", padx=(0, 20))

        # Character name and stats
        info_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True)

        name_label = ctk.CTkLabel(
            info_frame,
            text=entity.name.upper(),
            font=("Arial", 20, "bold"),
            text_color="white",
        )
        name_label.pack(anchor="w")

        stats_text = f"HP: {entity.max_hp} | Speed: {entity.speed} | Crit: {entity.crit_rate}% | Defense: {entity.defence}"
        stats_label = ctk.CTkLabel(
            info_frame, text=stats_text, font=("Arial", 12), text_color="#BDC3C7"
        )
        stats_label.pack(anchor="w")

        # Charts container
        charts_frame = ctk.CTkFrame(char_frame, fg_color="#FFFFFF")
        charts_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        charts_frame.grid_columnconfigure((0, 1), weight=1)

        # Create charts for this character
        self.create_character_charts(charts_frame, entity.name, entity_type)

    def create_character_charts(self, parent, char_name, entity_type):
        if entity_type == "Boss":
            # For bosses, filter battles where they appear as opponents in match_up
            sim_battles = [
                b
                for b in self.sim_data
                if char_name in b.get("match_up", "")
                and b.get("player_stats", {}).get("name") != char_name
            ]
            player_battles = [
                b
                for b in self.player_data
                if char_name in b.get("match_up", "")
                and b.get("player_stats", {}).get("name") != char_name
            ]
        else:
            # For characters, filter battles where they are players
            sim_battles = [
                b
                for b in self.sim_data
                if b.get("player_stats", {}).get("name") == char_name
            ]
            player_battles = [
                b
                for b in self.player_data
                if b.get("player_stats", {}).get("name") == char_name
            ]

        # Move usage chart
        self.create_move_usage_chart(
            parent, char_name, sim_battles, player_battles, 0, 0, entity_type
        )

        # Performance chart
        self.create_performance_chart(
            parent, char_name, sim_battles, player_battles, 0, 1, entity_type
        )

    def create_move_usage_chart(
        self, parent, char_name, sim_battles, player_battles, row, col, entity_type
    ):
        frame = ctk.CTkFrame(parent, fg_color="#FFFFFF")
        frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.patch.set_facecolor("#FFFFFF")

        # Determine actor type based on entity type
        actor_type = "Boss" if entity_type == "Boss" else "Player"

        # Simulation moves
        sim_moves = []
        for battle in sim_battles:
            for turn in battle.get("turns", []):
                if turn["actor"] == actor_type:
                    sim_moves.append(turn["move_used"])

        sim_counter = Counter(sim_moves)
        if sim_counter:
            colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57", "#FF9FF3"]
            wedges, texts, autotexts = ax1.pie(
                sim_counter.values(),
                labels=sim_counter.keys(),
                autopct="%1.1f%%",
                colors=colors[: len(sim_counter)],
            )
            ax1.set_title(
                f"{char_name} - Simulation Moves", color="black", fontsize=12, pad=20
            )
        else:
            ax1.text(
                0.5,
                0.5,
                "No Data",
                ha="center",
                va="center",
                color="black",
                fontsize=14,
            )
            ax1.set_title(
                f"{char_name} - Simulation Moves", color="black", fontsize=12, pad=20
            )

        # Player moves
        player_moves = []
        for battle in player_battles:
            for turn in battle.get("turns", []):
                if turn["actor"] == actor_type:
                    player_moves.append(turn["move_used"])

        player_counter = Counter(player_moves)
        if player_counter:
            colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57", "#FF9FF3"]
            wedges, texts, autotexts = ax2.pie(
                player_counter.values(),
                labels=player_counter.keys(),
                autopct="%1.1f%%",
                colors=colors[: len(player_counter)],
            )
            title_suffix = "Real Game" if entity_type == "Boss" else "Player"
            ax2.set_title(
                f"{char_name} - {title_suffix} Moves",
                color="black",
                fontsize=12,
                pad=20,
            )
        else:
            ax2.text(
                0.5,
                0.5,
                "No Data",
                ha="center",
                va="center",
                color="black",
                fontsize=14,
            )
            title_suffix = "Real Game" if entity_type == "Boss" else "Player"
            ax2.set_title(
                f"{char_name} - {title_suffix} Moves",
                color="black",
                fontsize=12,
                pad=20,
            )

        for ax in [ax1, ax2]:
            ax.tick_params(colors="black")

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    def create_performance_chart(
        self, parent, char_name, sim_battles, player_battles, row, col, entity_type
    ):
        frame = ctk.CTkFrame(parent, fg_color="#FFFFFF")
        frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.patch.set_facecolor("#FFFFFF")

        # Win rates (for bosses, count when they win)
        sim_wins = len([b for b in sim_battles if b["winner"] == char_name])
        sim_total = len(sim_battles)
        player_wins = len([b for b in player_battles if b["winner"] == char_name])
        player_total = len(player_battles)

        categories = ["Simulation", "Real Game"]
        win_rates = [
            (sim_wins / sim_total * 100) if sim_total > 0 else 0,
            (player_wins / player_total * 100) if player_total > 0 else 0,
        ]

        bars = ax1.bar(categories, win_rates, color=["#FF6B6B", "#4ECDC4"])
        ax1.set_title(f"{char_name} - Win Rate Comparison", color="black", fontsize=12)
        ax1.set_ylabel("Win Rate (%)", color="black")
        ax1.set_ylim(0, 100)
        ax1.set_facecolor("#FFFFFF")
        ax1.tick_params(colors="black")

        # Add value labels
        for bar, rate in zip(bars, win_rates):
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 2,
                f"{rate:.1f}%",
                ha="center",
                va="bottom",
                color="black",
            )

        # Average damage comparison
        actor_type = "Boss" if entity_type == "Boss" else "Player"

        sim_damages = []
        for battle in sim_battles:
            battle_dmg = [
                turn["damage_base"]
                for turn in battle.get("turns", [])
                if turn["actor"] == actor_type
            ]
            if battle_dmg:
                sim_damages.extend(battle_dmg)

        player_damages = []
        for battle in player_battles:
            battle_dmg = [
                turn["damage_base"]
                for turn in battle.get("turns", [])
                if turn["actor"] == actor_type
            ]
            if battle_dmg:
                player_damages.extend(battle_dmg)

        avg_damages = [
            np.mean(sim_damages) if sim_damages else 0,
            np.mean(player_damages) if player_damages else 0,
        ]

        bars2 = ax2.bar(categories, avg_damages, color=["#FF6B6B", "#4ECDC4"])
        ax2.set_title(f"{char_name} - Average Damage", color="black", fontsize=12)
        ax2.set_ylabel("Average Damage", color="black")
        ax2.set_facecolor("#FFFFFF")
        ax2.tick_params(colors="black")

        # Add value labels
        for bar, dmg in zip(bars2, avg_damages):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + max(avg_damages) * 0.02,
                f"{dmg:.0f}",
                ha="center",
                va="bottom",
                color="black",
            )

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)


def show_analysis():
    app = DataAnalysisWindow()
    app.mainloop()


if __name__ == "__main__":
    show_analysis()
