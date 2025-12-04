import random as rd
import slow_writing as sw
class Characters:
    def __init__(self, name , HP , MAXHP , BasicATK,Move1,Move2,Move3,Crit,SPD,DeF,pp1,pp2,pp3,move1_name,move2_name,move3_name):
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
        self.pp1 = pp1
        self.pp2 = pp2
        self.pp3 = pp3
        self.move1_name = move1_name
        self.move2_name = move2_name
        self.move3_name = move3_name
    def Attack(self,Target):
        while True:
            try:
                print('What would you like to do?')
                print('1.Basic Attack')
                print(f'2.{self.move1_name}:{self.pp1} turns left')
                print(f'3.{self.move2_name}:{self.pp2} turms left')
                print(f'4. {self.move3_name}:{self.pp3} turns left')
                print('5. Forfeit')
                choice = int(input('Enter your choice: '))
                if choice == 5:
                    sw.print_slow('You have forfeited the battle.')
                    self.HP = 0
                    break
                elif choice>5 or choice <=0:
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
                            damage = self.BasicATK//2
                        elif choice == 2:
                            if self.pp1 !=0:
                                sw.print_slow(f'{self.name} used {self.move1_name} on {Target.name}  but {Target.name} parried your attack!')
                                damage = self.Move1//2
                                self.pp1 -=1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                        elif choice == 3:
                            if self.pp2 !=0:           
                                sw.print_slow(f'{self.name} used {self.move2_name} on {Target.name}  but {Target.name} parried your attack!')
                                damage = self.Move2//2
                                self.pp2 -=1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                        elif choice == 4:
                            if self.pp3 != 0:
                                sw.print_slow(f'{self.name} used {self.move3_name} on {Target.name}  but {Target.name} parried your attack!')
                                damage = self.Move3//2
                                self.pp3 -= 1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                    elif critHit:
                        if choice == 1:
                            sw.print_slow(f'{self.name} attacked {Target.name}')
                            print('CRITICAL HIT!')
                            damage = self.BasicATK*2
                        elif choice == 2:
                            if self.pp1 !=0:
                                sw.print_slow(f'{self.name} used {self.move1_name} on {Target.name} !')
                                print('CRITICAL HIT!')
                                damage = self.Move1*2
                                self.pp1 -=1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                        elif choice == 3:
                            if self.pp2 != 0:
                                sw.print_slow(f'{self.name} used {self.move2_name} on {Target.name}!')
                                print('CRITICAL HIT!')
                                damage = self.Move2*2
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                            self.pp2 -=1
                        elif choice == 4:
                            if self.pp3 != 0:
                                sw.print_slow(f'{self.name} used {self.move3_name} on {Target.name}!')
                                print('CRITICAL HIT!')
                                damage = self.Move3*2
                                self.pp3 -= 1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                    elif not parry and not critHit:
                        if choice == 1:
                            sw.print_slow(f'{self.name} attacked {Target.name}')
                            damage = self.BasicATK
                        elif choice == 2:
                            if self.pp1 !=0:
                                sw.print_slow(f'{self.name} used {self.move1_name} on {Target.name}!')
                                damage = self.Move1
                                self.pp1 -=1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                        elif choice == 3:
                            if self.pp2 != 0:
                                sw.print_slow(f'{self.name} used {self.move2_name} on {Target.name}!')
                                damage = self.Move2
                                self.pp2 -=1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                        elif choice == 4:
                            if self.pp3 != 0:
                                sw.print_slow(f'{self.name} used {self.move3_name} on {Target.name}!')
                                damage = self.Move3
                                self.pp3 -= 1
                            else:
                                sw.print_slow('You do not have any turns left!')
                                continue
                Totaldamage = damage
                sw.print_slow(f'{Totaldamage} was dealt out of {Target.HP}')
                Target.HP -= Totaldamage
                break
            except ValueError:
                print('Invalid input. Please enter a number.')