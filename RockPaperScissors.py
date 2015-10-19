# Program Rock, Paper, Scissors using randint

import random

#Global Constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
    result = TIE
    while (result == TIE):
        # Get the computer number between 1 and 3
        computer = random.randint(1,3)

        # Get the number from the player
        player - int(input("Enter 1 for ROCK,"\
        "2 for Paper, 3 for Scissors: "))

    print ("Computer played: ", choiceString(computer))
    print ("You played: ", choiceString(player))

def rockPaperScissors(computer, player):
    if (computer == player):
        return TIE
    if computer == ROCK:
        if player == PAPER:
            return PLAYER_WINS
        if player == SCISSORS:
            return COMPUTER_WINS
def choiceString(choice):
    if choice == ROCK:
        return 'ROCK'
    if choice == PAPER:
        return 'PAPER'
    if choice == SCISSORS:
        return 'SCISSORS'



main()
