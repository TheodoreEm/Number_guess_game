import random
import time
from art import logo
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


random_number = random.randint(1, 100)

difficulty_bool = False

# Loop to be certain that the difficulty choice is easy or hard
while not difficulty_bool:
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        difficulty_bool = True
    else:
        print(f"Wrong input: {difficulty} Try again.")
        time.sleep(3)


# Function for the choice of easy difficulty
def easy_dif():
    guesses = 10
    while guesses > 0:
        print(f"You have {guesses} guesses remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("You guessed it! You win!")
            break
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low")
        guesses -= 1
        if guesses == 0:
            print("You lose.")
            print(f"The number was {random_number}.")
            break


# Function for the choice of hard difficulty
def hard_dif():
    guesses = 5
    while guesses > 0:
        print(f"You have {guesses} guesses remaining.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("You guessed it! You win!")
            break
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low")
        guesses -= 1
        if guesses == 0:
            print("You are out of guesses. You lose.")
            print(f"The number was {random_number}.")
            break


# If statement for calling the functions based on input. Because of the while loop the only 2 choices is easy or hard
if difficulty == "easy":
    easy_dif()
else:
    hard_dif()
