"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

welcome_message = "Welcome to GuessNumber3000!"
prompt1 = "Guess the magic number between 1 and 10!  "
lower = "      ***It's lower. Try again***  "
higher = "      ***It's higher. Try again***  "
end = "Play again to see if you can beat your high score?"
NIR = "***GuessNumber3000 only uses numbers 1 - 10.***"
compute = "Hmm.. DOES NOT COMPUTE.. Try 1 - 10 again.  "
yay = "Hurray! GuessNumber3000 is happy! :)"
sad = "GuessNumber3000 is sad to see you go. :("
HS = "***New High Score! Welcome to the record books!***"
tie = "***You tied your high score!***"

print (welcome_message)

def start_game():
    magic_number = random.randint(1,10)
    guess_count = 1
    high_score = 10
    while True:
        try:
            guess = int(input(prompt1))
            if guess < 1 or guess > 10:
                print (NIR)
                continue
        except ValueError:
            print (compute)
        else:
            if guess < magic_number:
                guess_count += 1
                print (higher)
            elif guess > magic_number:
                guess_count += 1
                print (lower)
            elif guess == magic_number:
                break
    print ("Got It! It took you {} guesses.".format(guess_count)) #insert here
    if guess_count < high_score:
        high_score = int("{}".format(guess_count))
        print (HS)
    elif guess_count == high_score:
        print (tie)
    print (end)
    play_again = str(input("press Y to play again.  "))
    if play_again.upper() == "Y":
        print (yay)
        print ("Enter the GuessNumber3000 hall of fame by beating {} guesses.".format(high_score))
        start_game()
    else:
        sys.exit(sad)
start_game()