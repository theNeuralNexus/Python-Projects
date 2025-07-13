import random
import sys


def main() -> None:
    """Main part of the program."""
    print("           ===== Number Guessing Game =====          ")

    random_number: int = random.randint(1, 100)
    tries: int = 0

    while tries < 10:
        user_guess = get_guess()
        if user_guess < random_number:
            print("Guess higher. Your guess is lower than random number.")
            tries += 1
        elif user_guess > random_number:
            print("Guess lower. Your guess is higher than random number")
            tries += 1
        else:
            print("\nYou won. Your guess is correct.")
            tries += 1
            print(f"You guess in {tries} tries.")
            break
    else:
        print(f"\nGame over. The number was {random_number}")


def get_guess() -> int:
    """
    Get the guess from the user.

    Returns:
        int: Guess of the user
    """
    try:
        guess: int = int(input("\nGuess the number between 1 and 100: "))
    except ValueError:
        sys.exit("\nIt is not a valid int. Please provide a valid int.")

    return guess


if __name__ == "__main__":
    main()
