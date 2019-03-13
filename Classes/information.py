# Hayden Whitney
# 2/19
# Test Question


class Information(object):
    def __init__(self, name, location, number):
        self.number = number.title()
        self.location = location.title()
        self.name = name.title()

    def display(self, name, location, number):
        print("Name:", name)
        print("Location:", location)
        print("Phone Number:", number)
