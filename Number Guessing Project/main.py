import art
import random

print(art.logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n")
number = random.randint(1,100)
turns = set_difficulty()


guess = 0
while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a Guess: "))

    turns = check_answer(guess, number, turns)
    if turns == 0:
        print("You've run out of guesses. You lose.")
        break
    elif guess != number:
        print("Guess again")