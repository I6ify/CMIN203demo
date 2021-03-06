import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll
from monster import Lich


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
                        Goblin(),
                        Troll(),
                        Dragon(),
                        Lich()]

        self.monster = self.get_next_monster()


    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if input("Dodge? Y/N ").lower() == 'y':
                if self.player.dodge:
                    print("you dodged the attack!")
                else:
                    if self.monster == Lich():
                        print("The Lich stretches his fingers and arcane bolts arc into your chest!")
                        self.player.hit_points -= 4
                    if self.monster != Lich():
                        print("Not fast enough! You got hit!")
                        self.player.hit_points -= 1
            else:
                print("{} hit you for 1 hit point!".format(self.monster))
                self.player.hit_points -= 1
        else:
            print("{} is not attacking this turn.".format(self.monster))

    def player_turn(self):
        player_choice = input("[A]ttack,[R]est,[Q]uit? ").lower()
        if player_choice == 'a':
            print("You're attacking {}".format(self.monster))

            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))  # ()?
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    if self.player.weapon == 'magic':
                        self.monster.hit_points -= 6
                        print("FIREBALL!")
                    else:
                        self.monster.hit_points -= 1
                    print("you hit {} with your {}".format(self.monster, self.player.weapon))
            else:
                print("You missed!")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()


    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)

        if self.player.hit_points:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!")
        sys.exit()

Game()
