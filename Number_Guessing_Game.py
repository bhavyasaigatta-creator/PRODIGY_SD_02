import random

while True:
    print("\n Number Guessing Game")
    
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (1-100): ")

        if not guess.isdigit():
            print(" Invalid input! Enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f" Correct! You guessed it in {attempts} attempts.")
            break
        elif guess < number:
            print(" Too low!")
        else:
            print(" Too high!")

    # Ask to play again
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("👋 Thanks for playing!")
        break
