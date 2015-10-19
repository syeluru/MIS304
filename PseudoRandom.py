# Program Pseudorandom

import random


def main():

    random.seed(random.randint(1,10))
    for i in range (10):
        print (random.randint(1,10), end = ' ' )

    print ()

    city = 'Washington'
    for ch in city:
        print(city[random.randint(0,len(city)-1)], end=' ')
    print ()

main()
