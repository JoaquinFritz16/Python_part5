import random
def GuessGame():
    secret_number=random.randint(1,100)
    while True:
        try:
            guess = int(input("Enter a number and see if you can guess the number I'm thinking of: "))
            if guess == secret_number:
                print(f"You've guessed it! The number was indeed {secret_number}")
                break
            elif guess < secret_number:
                print("Too small! Try a bigger number!")
            else:
                print("Too big! Try a smaller number!")
        except ValueError:
            print("Invalid input! Please enter a number!")


if __name__ == "__main__":
    GuessGame()