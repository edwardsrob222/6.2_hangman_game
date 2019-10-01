


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
