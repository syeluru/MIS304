# Class die
import random

class Die:

    # Constructor or initializer when creating an object
    # self has to be called because it means this class
    def __init__ (self):
        self.__sideup = 1

    # Accessor Methods, Get Methods, or Getters
    def getSideUp(self):
        return self.__sideup

    # Mutator method, Set method, or Setter
    def roll(self):
        self.__sideup = random.randint(1,6)
