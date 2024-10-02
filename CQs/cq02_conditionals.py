____author___: str = "730653429"


def guess_a_number() -> None:
    "Guessing a secret number!"
    secret_number = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess) + ".")
    if guess == secret_number:
        print("You got it!")
    elif guess < secret_number:
        print("Your guess was too low! The secret number is " + str(secret_number))
    else:
        print("Your guess was too high! The secret number is " + str(secret_number))


if __name__ == "__main__":
    guess_a_number()
