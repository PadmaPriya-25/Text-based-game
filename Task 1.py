import random

# Generate random number
number_to_guess = random.randint(1, 100)

# Initialize attempts
attempts = 5

print("Welcome to Cognifyz Guessing Game!")
print("Guess a number between 1 and 100.")

while attempts > 0:
    # Get user input
    user_guess = int(input("Enter your guess: "))

    # Check if guess is valid
    if user_guess < 1 or user_guess > 100:
        print("Invalid guess. Please try again.")
        continue

    # Check if guess is correct
    if user_guess == number_to_guess:
        print("Congratulations! You won!")
        break

    # Provide feedback
    elif user_guess < number_to_guess:
        print("Higher")
    else:
        print("Lower")

    # Decrement attempts
    attempts -= 1
    print(f"Attempts remaining: {attempts}")

# Game over
if attempts == 0:
    print(f"Game over! The number was {number_to_guess}.")