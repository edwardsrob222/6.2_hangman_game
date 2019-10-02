
#HANGMAN -------->

import random

def user_guess():
    guesses_left = 10
    dashes = "-" * len(words)

words: ["pineapple", "rocknroll", "star", "popcorn", "gladiator"]




while guesses_left > -1 and dashes != words:
    print(dashes)
    print (str(guesses_left))
    guess = input("Guess:")

    if user_guess in words:
        print ("Good guess! Letter is in secret word!")
    else:
        print ("Letter is not in the secret word!")
        guesses_left -= 1
    if guesses_left < 0:
    print ("You lose. The word was: " + str(words)

    def update_dashes():
