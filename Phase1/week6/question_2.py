class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit, amount must be more than zero")
        else:
            self.__balance += amount
            print("Deposited", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal, amount must be more than zero")
        elif amount > self.__balance:
            print("Not enough money in the account")
        else:
            self.__balance -= amount
            print("Withdrew", amount)

    def get_balance(self):
        print("Balance is", self.__balance)


account = BankAccount("Abel", 1000)

account.get_balance()
account.deposit(500)
account.deposit(-100)
account.withdraw(300)
account.withdraw(5000)
account.withdraw(-50)
account.get_balance()

# try to change balance directly, it does not work
account.__balance = 999999
account.get_balance()


# Answers

# 1 What is encapsulation
# Encapsulation means putting data and methods together in one class
# and controlling how the data is used

# 2 Why do we use private attributes
# To protect important data so nobody can change it in the wrong way
# The balance can only change using deposit and withdraw

# 3 What is name mangling
# Python changes the name of an attribute that starts with two underscores
# __balance becomes _BankAccount__balance
# This makes it hard to change from outside by mistake

# 4 Public protected and private
# public name is open to everyone, example account_holder
# protected _name means please do not use it outside the class
# private __name is hidden using name mangling