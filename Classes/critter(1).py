# Hayden Whitney
# 1/19
# Class Practice


class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):
        rep = "Critter Object\n"
        rep += "Name: " + self.name
        return rep


crit1 = Critter("Bob")
print(crit1)
crit2 = Critter("Frank")
print(crit2)
