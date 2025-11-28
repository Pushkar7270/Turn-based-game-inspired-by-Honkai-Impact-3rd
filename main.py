import time
import Characters as ch
import Boss as bs
import slow_writing as sw
def main():
    kiana = ch.Characters('Kiana',3000,3000,480,680,5,4,3)
    mei = ch.Characters('Mei', 2900,2900,460,550,4,5,3)
    bronya =ch.Characters('Bronya', 2800,2800,470,700,3,2,5)
    Boss_enemy = bs.Boss('Husk:Nihilus', 7000 , 7000 , 500 , 700 , 2 , 3 , 3)
    try:
        while True:
            print('Welcome to the simulation fight')
            print('Choose your character!')
            print(f'1.{kiana.name},HP {kiana.HP},ATK {kiana.ATK},weapon attack {kiana.WeaponATK}, crit 50% , SPD 40 DEF 30')
            print(f'2.{mei.name},HP {mei.HP},ATK {mei.ATK},weapon attack {mei.WeaponATK}, crit 40% , SPD 50 DEF 30' )
            print(f'3.{bronya.name},HP {bronya.HP},ATK {bronya.ATK},weapon attack {bronya.WeaponATK}, crit 40% , SPD 50 DEF 30')
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
                sw.print_slow(f'{Boss_enemy.name}\'s hp:{Boss_enemy.HP}')
                if turn == player:
                    sw.print_slow('Your turn')
                    player.Attack(Boss_enemy)
                    turn = Boss_enemy
                    print('------------------------------\n')
                    time.sleep(1)
                elif turn == Boss_enemy:
                    Boss_enemy.Attack(player)
                    turn = player
                    print('------------------------------\n')
                    time.sleep(1)
                if player.HP <= 0:
                    sw.print_slow('You Lost!')
                    break
                elif Boss_enemy.HP <=0:
                    sw.print_slow('You Won!')
                    break  
    except ValueError:
        print('Invalid input. Please enter a number!')   

if __name__ == '__main__':
    main()        