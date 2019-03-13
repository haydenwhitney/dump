# Hayden Whitney
# 2/19
# Class Practice


class Player(object):
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()


class Alien(object):
    def die(self):
        print("The alien gasps and says, 'Oh, this is it. This is the big one.",
              "\nYes, it's getting dark now. Tell my 1.6 million larvae that I loved them...'",
              "\nGoodbye, cruel universe.")


print("THE DEATH OF AN ALIEN\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")