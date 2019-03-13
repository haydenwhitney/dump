# Hayden Whitney
# 1/19
# Class Practice


class Account(object):
    def __init__(self, name):
        self.account_number = input("Enter your account number: ")
        self.phone_number = input("Enter your phone number: ")
        self.pin_number = 1234567
        self.balance = 0
        self.name = name

    def credit_account(self):
        get_pin = int(input("Enter your pin: "))
        while True:
            if get_pin != self.pin:
                get_pin = int(input("Enter your pin: "))
            else:
                amount = int(input("Enter the amount you would like to deposit: "))
                self.balance += amount
                break

    def debit_account(self):
        get_pin = int(input("Enter your pin: "))
        while True:
            if get_pin != self.pin:
                get_pin = int(input("Enter your pin: "))
            else:
                amount = int(input("Enter the amount you would like to withdraw: "))
                while True:
                    if amount <= self.balance:
                        self.balance -= amount
                        break
                    else:
                        print("You don't have enough money.")

hayden = Account("Hayden")

print(hayden.name)
print(hayden.account_number)
print(hayden.balance)

hayden.credit_account()
print(hayden.name)
print(hayden.account_number)
print(hayden.balance)