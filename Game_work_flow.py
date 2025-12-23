import random


class Battle_logic:
    def __init__(self, player, enemy):
        self.player = player
        if not self.player.playable:
            raise ValueError("Player is not playable")
        self.enemy = enemy
        if self.enemy.playable:
            raise ValueError("Enemy should not be playable")

    def execute_attack(self, attacker, defender, selected_move):
        damage = selected_move.damage
        total_damage = 0
        dodge_chance = random.randint(1, 10)
        parry_chance = random.randint(1, 10)
        crit_chance = random.randint(1, 10)
        if dodge_chance <= defender.speed:
            msg = f"{attacker.name} used {selected_move.name} but {defender.name} dodged it!"
        elif parry_chance <= defender.defence:
            msg = f"{attacker.name} used {selected_move.name} but {defender.name} parried the attack"
            total_damage = damage // 2
            if selected_move.pp > 0:  # Only decrement if not infinite
                selected_move.pp -= 1
        elif crit_chance <= attacker.crit_rate:
            msg = f"{attacker.name} used {selected_move.name} and dealt a critical hit!"
            total_damage = damage * 2
            if selected_move.pp > 0:  # Only decrement if not infinite
                selected_move.pp -= 1
        else:
            msg = f"{attacker.name} used {selected_move.name} on {defender.name}"
            total_damage = damage
            if selected_move.pp > 0:  # Only decrement if not infinite
                selected_move.pp -= 1
        if total_damage > 0:
            defender.take_damage(total_damage)
        if not defender.is_alive:
            msg += f"\n{defender.name} has been defeated!"
        print(msg)
        return msg
