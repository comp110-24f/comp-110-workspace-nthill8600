__author__: str = "730653429"


def input_guess(secret_word_len: int) -> str:
    while True:  # this function is having the user enter a word
        # checking the word to make sure it is the correct lenghth
        guess = input(f"Enter a {secret_word_len} character word:")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again:")
            # the function will keep asking for another
            # word till it is the right amount of characters


def contains_char(secret_word: str, char_guess: str) -> bool:
    "this function tests each index to see if it matches our second parameter"
    assert len(char_guess) == 1
    for char in secret_word:
        if char == char_guess:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """this function matches emojis to let the user know
    if a letter is in the right positon (green), yellow if
    is in the word but not in the right spot, or red if
    not in the word at all"""

    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index = 0  # start at the first index
    result = ""  # we will add to this blank string as we add emoji boxes

    while index in range(len(guess)):
        if (
            guess[index] == secret[index]
        ):  # seeing if there is an exact match at that index
            result += GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # checking for the character within the whole word
            result += YELLOW_BOX
        else:  # if the character isn't in the word at all it will print a white box
            result += WHITE_BOX
        index += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # the main function is to count the amount of
    # turns and check if they have won the game
    max_turns = 6
    turns = 0
    won = False

    while turns < max_turns and not won:  # game will continue to run
        # if it hasn't been 6 turns and the game hasn't been won
        turns += 1
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:  # if the guess is right the variable won will become true
            won = True

    if won:
        print(
            f"You won in {turns}/6 turns!"
        )  # printing a message that the game has been won
    else:
        print("X/6 - Sorry, try again tomorrow!")  # at first i didn't catch in the
        # instructions that it should return X/6 if lost


if __name__ == "__main__":
    main(secret="dogs")
