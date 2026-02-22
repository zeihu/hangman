import random
import os


def setup():
    # defining list of words
    natureWords = "mountain water valley summit gorge ocean lake river waterfall stream jungle forest meadow beach coast cave cliff island peninsula horizon clouds sunshine lightning thunder blizzard breeze moon stars nebula galaxy wildlife wilderness sapling wildflower bloom oak willow birch"
    # turning string into list (split by whitespace)
    natureList = natureWords.split(" ")
    # randomly selecting an item from the list to be the word
    word = random.choice(natureList)

    return word

# clearing terminal screen


def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ASCII art of hangman for each attempt


def hang(attempts):
    if attempts == 8:
        print('''






=========''')

    if attempts == 7:
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

    if attempts == 6:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')

    if attempts == 5:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

    if attempts == 4:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')

    if attempts == 3:
        print('''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''')

    if attempts == 2:
        print('''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''')

    if attempts == 1:
        print('''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''')

    return

# messages printed to user depending on whether they win or lose


def victory(win):
    if win == True:
        clear()
        hang(attempts)
        print('''\n*-*-*-*-*-*-*-*-*-*-*-*-*-*
|Congratulations, you win!|
*-*-*-*-*-*-*-*-*-*-*-*-*-*\n''')
        print(f"The word was: {word}\n")
    else:
        clear()
        hang(attempts)
        print('''\n*-*-*-*-*-*-*-*-*-*
|Sorry, you lose !|
*-*-*-*-*-*-*-*-*-*\n''')
        print(f"The word was: {word}\n")

### SETUP ###


word = setup()
correct = ""  # initializing list for correct letters guessed
guesses = ""  # initializing list for all letters guessed
win = False  # initializes win variable as false

clear()
print("Nature Themed Hangman!")
# prints blank spaces
for letter in word:
    print("_", end=" ")

attempts = 8  # initializes attempts to 8

### GAME ###

# loops while the user still has attempts and hasn't yet won
while attempts > 1 and win == False:
    print("\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    guess = str(input("\nEnter a letter to guess: "))  # user enters guess

    # validating input, returns to beginning of loop if invalid
    if len(guess) > 1:
        print("Your guess must be one character")
        continue
    elif not guess.isalpha():
        print("Your guess must be a letter of the alphabet")
        continue
    elif guess in guesses:
        print("You already guessed this letter")
        continue

    # incorrect guesses
    if guess not in word:
        clear()
        guesses += guess  # adds to string of guesses
        print("Wrong!\n")
        attempts -= 1  # takes away an attempt
        # calls hang function which prints the ASCII art for the attempt
        hang(attempts)

    # correct guesses
    if guess in word:
        clear()
        print("Good guess!\n")
        hang(attempts)
        guesses += guess  # adds to string of guesses
        # checks how many times letter occurs in word, and adds it to correct guesses that many times
        occurrences = word.count(guess)
        correct += guess * occurrences
        # if the length of correct letters and the word are the same then win is changed to True
        if len(correct) == len(word):
            win = True

    # prints correctly guessed letters and blank spaces
    for char in word:
        if char in correct:
            print(char, end=" ")
        else:
            print("_", end=" ")

    print(f"\n\n Guessed letters: {guesses}")

# calls victory function which prints output depending on if win variable is True or False
victory(win)
