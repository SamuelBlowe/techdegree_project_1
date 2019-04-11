"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
By Samuel Blowe
I want to do the extra credit but I decided to leave out the high score list sorting.
I deleted all of the high score list parts from my code.
--------------------------------

"""

import random

def guessing_game():
    
    print("""Hello, player! 
        \nWelcome to the guessing game!
        \nYou will be choosing a number between 1 and 10.
        """) #text header wecoming player to game.
    players_choice = 0
    solution = random.randint(1,10)
    player_attempt = 0

    while solution != players_choice:
        players_choice = input("Choose a number:  ")
        player_attempt += 1

        try: # a try to catch errors while playing the game.
            players_choice = int(players_choice)
            if players_choice > 10:
                raise ValueError("That value is invalid! Try again.")
            elif players_choice <= 0:
                raise ValueError("That value is invalid! Try again.")
            elif players_choice < solution:
                print("Higher. Try again.") #promt user for a guess and if answer is higher
            elif players_choice > solution:
                print("Lower. Try again.") #prompt user for a guess and if answer is lower
            else:
                print("You got the answer!")    
        except ValueError as err: # an except to report error to use in meaningful way
            print("Oh no! We ran into an issue. Please try again.")

    print("You attempted {} times.".format(player_attempt)) #number of attempts to be displayed

    retry = input("Would you like another attempt at the game? (y/n):  ")
    if retry == str("y"):
        guessing_game()
    else:
        print("Come back to play again soon!\nGAME OVER")

guessing_game()