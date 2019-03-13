# Hayden Whitney
# 1/19
# Class Practice


class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi. I'm", self.name)


critter_1 = Critter("Bob")
print(critter_1)
critter_2 = Critter("Frank")
print(critter_2)