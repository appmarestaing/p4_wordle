import random

possible_words = ["great", "swift", "slime", "break", "quake"]


# variable to store word user guesses
word = random.choice(possible_words)
print(word)

# colors for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

# function to generate hint with correct letter colors
def generate_hint(guess):
    color = default
    hint = ""
    # loops 5 times once for each letter guess[i] is the current letter
    for i in range(5):
        if guess[i] == word[i]:
            color = green
        elif guess[i] in word:
            color = yellow
        else:
            color = default
        # adds letter with correct color to hint word
        hint = hint + color + guess[i] + default
    return hint

# function that loops 6 times once for each guess
def game_loop():
    user_guess = ""
    for i in range(6):
        user_guess = input("give a guess: ")
        print(generate_hint(user_guess))
        # if user guesses correct word, exit the loop
        if user_guess == word:
            print("congratulations!!!")
            break

game_loop()
