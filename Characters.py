import random as rd
import slow_writing as sw
class Characters:
    def __init__(self, name , HP , MAXHP , ATK,WeaponATK,Crit,SPD,DeF):
        self.name = name
        self.HP = HP
        self.MAXHP = MAXHP
        self.ATK = ATK
        self.WeaponATK = WeaponATK
        self.Crit_list = ['Crit'] * Crit + ['Normal'] * (10 - Crit)
        self.Dodge_list = ['Dodge'] * SPD + ['Normal'] * (10-SPD)
        self.Parry_list = ['Parry']* DeF + ['Normal'] * (10-DeF)
    def Attack(self,Target):
        while True:
            try:
                print('What would you like to do?')
                print('1.Basic Attack')
                print('2.Special Attack')
                print('3. Forfeit')
                choice = int(input('Enter your choice: '))
                if choice == 3:
                    sw.print_slow('You have forfeited the battle.')
                    self.HP = 0
                    break
                elif choice>3 or choice <0:
                    sw.print_slow('Invalid input. Choose between 1 and 3')
                    continue
                critHit = False
                parry = False
                hit = True
                dodge = False
                Totaldamage = 0
                critChance = rd.choice(self.Crit_list)
                ParryChance = rd.choice(Target.Parry_list)
                DodgeChance = rd.choice(Target.Dodge_list)
                if critChance == 'Crit':
                    critHit = True
                if ParryChance == 'Parry':
                    parry = True
                if DodgeChance == 'Dodge':
                    dodge = True
                    hit = False
                if not hit or dodge:
                    sw.print_slow(f'{Target.name} dodged your attack!')
                    damage = 0
                if hit:
                    if parry:
                        if choice == 1:
                            sw.print_slow(f'{self.name} attacked {Target.name} but {Target.name} parried your attack!')
                            damage = self.ATK//2
                        elif choice == 2:
                            sw.print_slow(f'{self.name} attacked {Target.name}  but {Target.name} parried your attack!')
                            damage = self.WeaponATK//2
                    elif critHit:
                        if choice == 1:
                            sw.print_slow(f'{self.name} attacked {Target.name}')
                            sw.print_slow('CRITICAL HIT!')
                            damage = self.ATK*2
                        elif choice == 2:
                            sw.print_slow(f'{self.name} attacked {Target.name} with their special move.')
                            damage = self.WeaponATK*2
                    elif not parry and not critHit:
                        if choice == 1:
                            sw.print_slow(f'{self.name} attacked {Target.name}')
                            damage = self.ATK
                        elif choice == 2:
                            sw.print_slow(f'{self.name} attacked {Target.name} with their special move.')
                            damage = self.WeaponATK
                Totaldamage = damage
                sw.print_slow(f'{Totaldamage} was dealt out of {Target.HP}')
                Target.HP -= Totaldamage
                break
            except ValueError:
                print('Invalid input. Please enter a number.')