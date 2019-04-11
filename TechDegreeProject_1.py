"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
By Samuel Blowe
I want to do the extra credit but I cannot seem to get the
high score to work properply. Aside from that, this is my first draft!
--------------------------------

"""

import random

high_score = [] #list was ppreviously inside of while loop
def guessing_game():
    
    print("""Hello, player!
        \nWelcome to the guessing game!
        \nThe score is {} attempts!
        \nYou will be choosing a number between 1 and 10.
        """.format(high_score))
    players_choice = 0
    solution = random.randint(1,10)
    player_attempt = 0

    while solution != players_choice:
        players_choice = input("Choose a number:  ")
        player_attempt += 1

        try:
            players_choice = int(players_choice)
            if players_choice > 10:
                raise ValueError("That value is invalid! Try again.")
            elif players_choice <= 0:
                raise ValueError("That value is invalid! Try again.")
            elif players_choice < solution:
                print("Higher. Try again.")
            elif players_choice > solution:
                print("Lower. Try again.")
            else:
                print("You got the answer!")    
        except ValueError as err:
            print("Oh no! We ran into an issue. Please try again.")

    print("You attempted {} times.".format(player_attempt))
    high_score.extend([player_attempt])

    retry = input("Would you like another attempt at the game? (y/n):  ")
    if retry == str("y"):
        guessing_game()
    else:
        print("Come back again to play again soon!\nGAME OVER")

guessing_game()