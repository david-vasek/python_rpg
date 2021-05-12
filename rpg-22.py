class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power 

    def attack(self, enemy):
        # do attack stuff
        enemy.health -= self.power

    def alive(self, enemy):
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            dirty_dan.attack(pin_head_larry)
            print("You do %d damage to the goblin." % dirty_dan.power)
            if pin_head_larry.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power 
    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self, enemy):
        if pin_head_larry.health > 0:
            # Goblin attacks hero
            pin_head_larry.attack(dirty_dan)
            print("The goblin does %d damage to you." % pin_head_larry.health)
            if dirty_dan.health <= 0:
                print("You are dead.")

dirty_dan = Hero(10, 5)
pin_head_larry = Goblin(6, 2)


def main():

    while pin_head_larry.alive() and dirty_dan.alive():
        print("You have %d health and %d power." % (dirty_dan.health, dirty_dan.power))
        print("The goblin has %d health and %d power." % (pin_head_larry.health, pin_head_larry.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
       


main()