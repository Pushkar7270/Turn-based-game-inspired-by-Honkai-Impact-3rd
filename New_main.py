import File_handler as fh
from Entites import Entity, Move
from Game_work_flow import Battle_logic


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
        )

    playable_characters = [dict_to_entity(char) for char in entities["Characters"]]
    boss = [dict_to_entity(boss) for boss in entities["Boss"]]
    return playable_characters, boss


def main():
    characters, bosses = get_game_entities("Characters.json")
    if not characters or not bosses:
        print("No characters or bosses found")
        return False
    while True:
        print("\n--- Welcome to the turn based rpg---")
        print("Choose your valkyrie")
        for i, character in enumerate(characters):
            print(
                f"{i + 1}. {character.name}, {character.hp},{character.moves}, {character.speed} , {character.defence}, {character.crit_rate},"
            )
        print(f"{len(characters) + 1}. exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number only")
            continue
        if choice == (len(characters) + 1):
            print("Exiting the game...")
            break
        if choice < 1 or choice > len(characters):
            print("Invalid Valkyrie choice! Please pick a number from the list.")
            continue
        while True:
            print("Choose your boss")
            for i, boss in enumerate(bosses):
                print(f"{i + 1}. {boss.name}")
            print(f"{len(bosses) + 1}. Back to Valkyrie Selection")
            try:
                boss_choice = int(input("Enter your choice: "))
                if boss_choice == (len(bosses) + 1):
                    break
                if 1 <= boss_choice <= len(bosses):
                    Battle = Battle_logic(
                        characters[choice - 1], bosses[boss_choice - 1]
                    )
                    Battle.start_battle()
                    characters, bosses = get_game_entities("Characters.json")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, please enter a number only")


if __name__ == "__main__":
    main()
