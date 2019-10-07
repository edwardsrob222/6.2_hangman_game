
#HANGMAN -------->

import random
#
guesses_left = 10
hangman = True

# def user_guess():



words = ["pineapple", "rocknroll", "star", "popcorn", "gladiator"]
dashes = "-" * len(words)

print(words)
words = random.choice(words)
print(words)

while hangman:
    if guesses_left > -1 and dashes != words:
        print(dashes)
        print (str(guesses_left))
        guess = input("Guess:")
#
    if guess in words:
        print ("Good guess! Letter is in secret word!")
    else:
        print ("Letter is not in the secret word!")
        guesses_left -= 1
    if guesses_left < 1:
        print("You lose. The word was: " + str(words))
        hangman = False
    # def update_dashes():

    #this adds the guess to a string if answered correct
    # for i in range(5):
    #     if [i] == rec_guess:
    #         result = result + guesses_left
    #     else:
    #         return result
