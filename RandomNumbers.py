# Program to generate random numbers

import random

def main():

  #randint()
  #Generates random numbers between 1 and end inclusive
  random_number = 0
  random_number = random.randint(1,10)
  print (random_number)

  #Randrange()
  #Generators random number between 2 and 20 not inclusive
  random_number = random.randrange(2,20)
  print (random_number)

  random_number = random.randrange(30)
  #This one is between 0 and 29
  print (random_number)

  random_number = random.randrange(100,201,10)
  #This one has a step value so only does multiples
  # of 10 in this case
  print (random_number)

  random_number = random.random()
  print(random_number)

  random_number = random.uniform(1.0, 10.0)
  #uniform between those two inclusive
  print (random_number)
main()
