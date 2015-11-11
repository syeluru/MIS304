# Class BankAccount

class BankAccount:

    # Constructor or initializer
    def __init__(self, initial_balance=0.0):
        self.__balance = initial_balance

    # Setter, Mutator, Set method
    def deposit(self, amount):
        self.__balance += amount
    # Setter, Mutator, Set method)
    def withdraw(self, amount):
        self.__balance -= amount
