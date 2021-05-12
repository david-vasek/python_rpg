class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power 
        self.name = name

    def alive(self):
        return self.health > 0

    def print_status(self): 
        print("%s has %s health." % (self.health, self.power))

    def attack(self, enemy):
        # do attack stuff
        enemy.health -= self.power


class Hero(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name 



class Goblin(Character):
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name


class Zombie(Character):
    def alive(self):
        return True
        

dirty_dan = Hero(10, 5, "Dirty Dan")
pin_head_larry = Goblin(6, 2, "Pin Head Larry")
dead_dude = Zombie(25, 10, "Dead Dude")

def main():

    while dirty_dan.alive() and dead_dude.alive():
        print("You have %d health and %d power." % (dirty_dan.health, dirty_dan.power))
        print("Dead Dude has %d health and %d power." % (dead_dude.health, dead_dude.power))
        print()
        print("What do you want to do, My dude?")
        print("1. Fight Dead Dude?")
        print("2. just hang out?")
        print("3. act like a wuss and run?")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            dirty_dan.attack(dead_dude)
            dead_dude.print_status()
            print("You do %d damage to the goblin." % dirty_dan.power)
            if dead_dude.alive(): == False:
                print("Dead Dude is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if dead_dude.alive():
            dead_dude.attack(dirty_dan)
            dirty_dan.print_status()
            print("Dead Dude does %d damage to you." % dead_dude.health)
            if dirty_dan.alive() == False:
                print("You are dead.")

main()