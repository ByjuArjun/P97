import random

random_number = random.randint(1, 9)
attempts = 5

print("Welcome to the Guess the Number Game!")
print("You have 5 chances to guess the number between 1 and 9.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The number was {random_number}.")