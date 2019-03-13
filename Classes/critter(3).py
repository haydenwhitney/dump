# Hayden Whitney
# 1/19
# Class Practice


class Critter(object):
    def __init__(self, name):
        print("A new critter has been born!")
        # Public Attribute
        self.name = name
        # Private Attribute
        self.__mood = mood

    def talk(self):
        print("\nI'm", self.name)
        print("Right now, I feel", self.__mood, "\n")

    @staticmethod
    def __private_method(self):
        print("This is a private method.")

    @staticmethod
    def public_method(self):
        print("This is a public method.")


critter_1 = Critter("Bob")
print(critter_1)
critter_2 = Critter("Frank")
print(critter_2)