import File_handler as fh
from Entites import Entity, Move
from UI.Battle_window import Battlewindow
from UI.selection_window import SelectionWindow


def get_game_entities(filename):
    entities = fh.load_data(filename)
    if not entities:
        print("No data found")
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
            # Ensure your JSON includes this key pointing to the assets folder
            image_path=entity_dict.get("image_path", "assets/placeholder.png"),
        )

    playable_characters = [dict_to_entity(char) for char in entities["Characters"]]
    bosses = [dict_to_entity(b) for b in entities["Boss"]]
    return playable_characters, bosses


def main():
    # 1. Load Data
    characters, bosses = get_game_entities("Characters.json")
    if not characters or not bosses:
        return

    # 2. GUI Flow: Valkyrie Selection
    # This pauses until the user clicks 'SELECT' or closes the window
    valk_menu = SelectionWindow(characters, "SELECT YOUR VALKYRIE")
    selected_valk = valk_menu.get_result()

    if not selected_valk:
        print("Valkyrie selection cancelled.")
        return

    # 3. GUI Flow: Boss Selection
    boss_menu = SelectionWindow(bosses, "SELECT YOUR TARGET")
    selected_boss = boss_menu.get_result()

    if not selected_boss:
        print("Boss selection cancelled.")
        return

    # 4. GUI Flow: Start Battle Interface
    print(f"Starting Battle: {selected_valk.name} vs {selected_boss.name}")
    battle_ui = Battlewindow(selected_valk, selected_boss)
    battle_ui.start()


if __name__ == "__main__":
    main()
