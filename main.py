import time
import Characters as ch
import Boss as bs
import slow_writing as sw
def main():
    kiana = ch.Characters('Kiana',5600,5600,440,490,500,800,5,4,2,10,10,5,'Subspace lance','Neko Charm','Shamash Unleashed')
    mei = ch.Characters('Mei', 5500,5500,470,480,500,780,3,5,4,10,10,5,'Searing slash','7 Thunders:Rumble','Fate cutter')
    bronya =ch.Characters('Bronya', 6000,6000,550,500,570,800,3,2,5,10,10,5,'Cognitive destruction','Selene','Quasi-black hole')
    boss_enemy = bs.Boss('Sa',9000,9000,230,300,450,620,1,3,3,'Matter erasure','Time acceleration','Power of Samsara')
    try:
        while True:
            print('Welcome to the simulation fight')
            print('Choose your character!')
            print(f'1.{kiana.name},HP {kiana.HP},ATK {kiana.BasicATK},{kiana.move1_name}:{kiana.Move1},{kiana.move2_name}:{kiana.Move2},{kiana.move3_name}:{kiana.Move3} crit 50% , SPD 40 DEF 20')
            print(f'2.{mei.name},HP {mei.HP},ATK:{mei.BasicATK},{mei.move1_name}:{mei.Move1},{mei.move2_name}:{mei.Move2},{mei.move3_name}:{mei.Move3}, crit 30% , SPD 50 DEF 40' )
            print(f'3.{bronya.name},HP {bronya.HP},ATK {bronya.BasicATK},{bronya.move1_name}:{bronya.Move1},{bronya.move2_name}:{bronya.Move2},{bronya.move3_name}:{bronya.Move3}, crit 30% , SPD 20 DEF 50' )
            print('4. Exit')
            choice = int(input('Enter your choice: '))
            player = None
            if choice == 1:
                player = kiana
                break
            elif choice == 2:
                player = mei
                break
            elif choice == 3:
                player = bronya
                break
            elif choice == 4:
                break
            else:
                print('Invalid choice')
                break
        if player != None:
            turn = player
            while True:
                sw.print_slow(f'{player.name}\'s hp:{player.HP}')
                sw.print_slow(f'{boss_enemy.name}\'s hp:{boss_enemy.HP}')
                if turn == player:
                    sw.print_slow('Your turn')
                    player.Attack(boss_enemy)
                    turn = boss_enemy
                    print('------------------------------\n')
                    time.sleep(1)
                elif turn == boss_enemy:
                    boss_enemy.Attack(player)
                    turn = player
                    print('------------------------------\n')
                    time.sleep(1)
                if player.HP <= 0:
                    sw.print_slow('You Lost!')
                    break
                elif boss_enemy.HP <=0:
                    sw.print_slow('You Won!')
                    break  
    except ValueError:
        print('Invalid input. Please enter a number!')   

if __name__ == '__main__':
    main()