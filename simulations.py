import copy
import random

import File_handler as fh
from Game_work_flow import Battle_logic
from New_main import get_game_entities


def pick_move(character):
    if not character.moves:
        return None
    return random.choice(character.moves)


def self_extrapolate(times=100):
    original_characters, original_bosses = get_game_entities("Characters.json")
    if not original_characters or not original_bosses:
        print("Error finding characters!")
        return None

    all_battles = []
    print("Starting self_extrapolation.")

    for i in range(times):
        player = copy.deepcopy(random.choice(original_characters))
        enemy = copy.deepcopy(random.choice(original_bosses))

        battle_log = {
            "battle_id": i + 1,
            "match_up": f"{player.name} vs {enemy.name}",
            "player_stats": {
                "name": player.name,
                "hp": player.max_hp if hasattr(player, "max_hp") else player.hp,
                "speed": player.speed,
                "crit_rate": player.crit_rate,
            },
            "winner": None,
            "turns": [],
        }

        engine = Battle_logic(player, enemy)
        turn_count = 0

        while player.hp > 0 and enemy.hp > 0:
            turn_count += 1

            if player.hp > 0:
                move = pick_move(player)
                result_message = engine.execute_attack(player, enemy, move)
                battle_log["turns"].append(
                    {
                        "turn": turn_count,
                        "actor": "Player",
                        "move_used": move.name,
                        "damage_base": move.damage,
                        "result_log": result_message,
                        "boss_hp_remaining": max(0, enemy.hp),
                    }
                )

            if enemy.hp <= 0:
                break

            if enemy.hp > 0:
                boss_move = pick_move(enemy)
                if not boss_move:
                    print(
                        f"ERROR: Boss {enemy.name} has no moves! Check Characters.json"
                    )
                    break

                result_msg = engine.execute_attack(enemy, player, boss_move)
                battle_log["turns"].append(
                    {
                        "turn": turn_count,
                        "actor": "Boss",
                        "move_used": boss_move.name,
                        "damage_base": boss_move.damage,
                        "result_log": result_msg,
                        "player_hp_remaining": max(0, player.hp),
                    }
                )

        winner = player.name if player.hp > 0 else enemy.name
        battle_log["winner"] = winner
        battle_log["total_turns"] = turn_count
        all_battles.append(battle_log)

    fh.save_data(all_battles, "simulation_data.json")
    print("\nSimulation complete. Data saved to simulation_data.json")


if __name__ == "__main__":
    self_extrapolate(100)
