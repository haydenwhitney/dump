# Hayden Whitney
# 1/19
# Class Practice


class Human(object):
    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def introduce_self(self):
        print("Hello, my name is " + self.name)

    def describe_self(self):
        print("I have", self.hair_color, "hair")
        print("I have", self.eye_color, "eyes")
        print("I am", self.height, "inches tall")
        print("I weigh", self.weight, "lbs")
        print("I am a ", self.race, self.gender, "with an iq of", self.iq)

    def evaluate_self(self):
        bmi_height = (self.height * 0.025) * (self.height * 0.025)
        bmi_weight = self.weight * 0.45
        bmi = bmi_weight / bmi_height
        bmi = round(bmi, 1)
        print("I have a bmi of", bmi)
        if bmi < 18.5:
            print("I am underweight.")
        elif bmi >= 25:
            print("I am overweight.")


hayden = Human("Hayden", "Brown", "Hazel", 73, 132, 300, "Male", "White")
jacob = Human("Jacob", "Brown", "Hazel", 79, 348, 27, "Male", "White")
eric = Human("Eric", "Brown", "Hazel", 79, 348, 27, "Male", "White")

hayden.introduce_self()
hayden.describe_self()
hayden.evaluate_self()

print()

jacob.introduce_self()
jacob.describe_self()
jacob.evaluate_self()

print()

eric.introduce_self()
eric.describe_self()
eric.evaluate_self()
