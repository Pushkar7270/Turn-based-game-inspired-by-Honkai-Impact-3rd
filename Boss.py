import random
import slow_writing as sw
class Boss:
    def __init__(self, name , HP , MAXHP , BasicATK,Move1,Move2,Move3,Crit,SPD,DeF,move1_name,move2_name,move3_name):
            self.name = name
            self.HP = HP
            self.MAXHP = MAXHP
            self.BasicATK = BasicATK
            self.Move1 = Move1 
            self.Move2 = Move2
            self.Move3 = Move3
            self.Crit_list = ['Crit'] * Crit + ['Normal'] * (10 - Crit)
            self.Dodge_list = ['Dodge'] * SPD + ['Normal'] * (10-SPD)
            self.Parry_list = ['Parry']* DeF + ['Normal'] * (10-DeF)
            self.move1_name = move1_name
            self.move2_name = move2_name
            self.move3_name = move3_name
    def Attack(self,Target):
        choices = [1,2,3,4]
        choiced = random.choice(choices)
        critHit = False
        parry = False
        hit = True
        dodge = False
        TotalDamage = 0
        critchance = random.choice(self.Crit_list)
        parrychance = random.choice(Target.Parry_list)
        dodgechance = random.choice(Target.Dodge_list)
        if critchance == 'Crit':
            critHit = True
        if parrychance == 'Parry':
            parry = True
        if dodgechance == 'Dodge':
            dodge = True
            hit = False
        if dodge or not hit:
            sw.print_slow(f'{Target.name} dodged the attack!')
            damage = 0
        if hit:
            if parry:
                if choiced == 1:
                    sw.print_slow(f'{self.name} attacked {Target.name} but {Target.name} parried the attack!')
                    damage = self.BasicATK//2
                elif choiced == 2:
                    sw.print_slow(f'{self.name} used {self.move1_name} on {Target.name} but {Target.name} parried the attack')
                    damage = self.Move1//2
                elif choiced == 3:
                    sw.print_slow(f'{self.name} used {self.move2_name} on {Target.name} but {Target.name} parried the attack')
            elif critHit:
                if choiced == 1:
                    sw.print_slow(f'{self.name} attacked {Target.name}')
                    sw.print_slow('CRITICAL HIT!')
                    damage = self.ATK*2
                elif choiced == 2:
                    sw.print_slow(f'{self.name} stabbed {Target.name} with its weapon')
                    sw.print_slow('CRITICAL HIT!')
                    damage = self.WeaponATK*2
            elif not parry and not critHit:
                if choiced == 1:
                    sw.print_slow(f'{self.name} attacked {Target.name}')
                    damage = self.BasicATK
                elif choiced == 2:
                    sw.print_slow(f'{self.name} stabbed {Target.name} with its weapon')
                    damage = self.WeaponATK
            TotalDamage = damage
            sw.print_slow(f'{TotalDamage} was dealt out of {Target.HP}')
            Target.HP -= TotalDamage