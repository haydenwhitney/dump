# Hayden Whitney
# 1/19
# Class Practice


class Critter(object):
    total = 0

    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = "Critter Object\n"
        rep += "Name: " + self.name
        return rep

    def talk(self):
        print("Hi. I'm", self.name, "\n")

    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)


critter_1 = Critter("Bob")
print(critter_1)
critter_2 = Critter("Frank")
print(critter_2)

print("Accessing the class attribute Critter.total:", end=" ")
print(Critter.total)