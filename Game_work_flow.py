import random
import time


class Battle_logic:
    def __init__(self, player, enemy):
        self.player = player
        if not self.player.playable:
            raise ValueError("Player is not playable")
        self.enemy = enemy
        if self.enemy.playable:
            raise ValueError("Enemy should not be playable")

    def start_battle(self):
        while self.player.is_alive and self.enemy.is_alive:
            self.take_turn(self.player, self.enemy)
            if not self.enemy.is_alive:
                break
            time.sleep(1)
            self.take_turn(self.enemy, self.player)
            if self.player.is_alive and not self.enemy.is_alive:
                print("You won")
                break
        else:
            print("You lost")

    def take_turn(self, attacker, defender):
        selected_move = None
        if attacker.playable:
            while True:
                print("Enter your Choice(e to exit)")
                for i, move in enumerate(attacker.moves):
                    print(f"{i + 1}. {move.name} ; {move.pp} turns left")
                try:
                    choice = input("Enter your choice: ")
                    if choice.lower() == "e":
                        print("You have exited the game!")
                        attacker.hp = 0
                        return
                    choice_int = int(choice)
                    if choice_int > len(attacker.moves) or choice_int < 1:
                        raise ValueError
                    else:
                        selected_move = attacker.moves[choice_int - 1]
                        if selected_move.pp == 0:
                            print("You do not have any turns left!")
                            continue
                        break
                except ValueError:
                    print("Invalid choice!")
        else:
            selected_move = random.choice(attacker.moves)
        self.execute_attack(attacker, defender, selected_move)

    def execute_attack(self, attacker, defender, selected_move):
        damage = selected_move.damage
        total_damage = 0
        dodge_chance = random.randint(1, 10)
        parry_chance = random.randint(1, 10)
        crit_chance = random.randint(1, 10)
        if dodge_chance <= defender.speed:
            print(
                f"{attacker.name} used {selected_move.name} but {defender.name} dodged it!"
            )
            return
        elif parry_chance <= defender.defence:
            print(
                f"{attacker.name} used {selected_move.name} but {defender.name} parried the attack"
            )
            total_damage = damage // 2
        elif crit_chance <= attacker.crit_rate:
            print(
                f"{attacker.name} used {selected_move.name} and dealt a critical hit!"
            )
            total_damage = damage * 2
        else:
            print(f"{attacker.name} used {selected_move.name} on {defender.name}")
            total_damage = damage
        selected_move.pp -= 1
        return defender.take_damage(total_damage)
