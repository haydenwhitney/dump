def calculate(exp):
    add = int(input("Enter the amount of experience points earned: "))
    exp += add
    if 0 > exp < 300:
        level = 1
        proficiency_bonus = 2
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 300 <= exp < 900:
        level = 2
        proficiency_bonus = 2
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 900 <= exp < 2700:
        level = 3
        proficiency_bonus = 2
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 2700 <= exp < 6500:
        level = 4
        proficiency_bonus = 3
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 6500 <= exp < 14000:
        level = 5
        proficiency_bonus = 3
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 14000 <= exp < 23000:
        level = 6
        proficiency_bonus = 3
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 23000 <= exp < 34000:
        level = 7
        proficiency_bonus = 3
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 34000 <= exp < 48000:
        level = 8
        proficiency_bonus = 3
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 48000 <= exp < 64000:
        level = 9
        proficiency_bonus = 4
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 64000 <= exp < 85000:
        level = 10
        proficiency_bonus = 4
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 85000 <= exp < 100000:
        level = 11
        proficiency_bonus = 4
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 100000 <= exp < 120000:
        level = 12
        proficiency_bonus = 4
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 120000 <= exp < 140000:
        level = 13
        proficiency_bonus = 5
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 140000 <= exp < 165000:
        level = 14
        proficiency_bonus = 5
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 165000 <= exp < 195000:
        level = 15
        proficiency_bonus = 5
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 195000 <= exp < 225000:
        level = 16
        proficiency_bonus = 5
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 225000 <= exp < 265000:
        level = 17
        proficiency_bonus = 6
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 265000 <= exp < 305000:
        level = 18
        proficiency_bonus = 6
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif 305000 <= exp < 355000:
        level = 19
        proficiency_bonus = 6
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")
    elif exp >= 355000:
        level = 20
        proficiency_bonus = 6
        print("You are level " + str(level) + " with a proficiency bonus of +" + str(proficiency_bonus) + ".")


exp = 0
calculate(exp)
