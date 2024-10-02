"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730653429"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if (
        len(word) != 5
    ):  # if the length of the word isn't 5 a print message will saw error
        print("Error: Word must contain 5 characters.")
        exit(1)
        # exits the function so that if the word doesn't have
        # 5 characters it won't continue
    return word  # if it is 5 letters it will return/print the word


def input_letter() -> str:
    character = input("Enter a single character: ")
    if len(character) != 1:  # follows the same function as above
        print("Error: Character must be a single character.")
        exit(1)
    return character


def contains_char(input_word: str, input_letter: str) -> None:
    print("Searching for " + str(input_letter) + " in " + str(input_word))
    # for all inputs it will return the searching for print statement
    count = 0  # our count starts with zero and
    # each letter match found will add one to the count
    if (
        input_letter == input_word[0]
    ):  # since we aren't using a loop we have to write out each if
        print(str(input_letter) + " found at index 0")
        count += 1
    if input_letter == input_word[1]:
        print(str(input_letter) + " found at index 1")
        count += 1
    if input_letter == input_word[2]:
        print(str(input_letter) + " found at index 2")
        count += 1
    if input_letter == input_word[3]:
        print(str(input_letter) + " found at index 3")
        count += 1
    if input_letter == input_word[4]:
        print(str(input_letter) + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + str(input_letter) + " found in " + str(input_word))
    elif count == 1:
        # i kept forgetting this line of code, we need this
        # because the else has instances (plural)
        print("1 instance of " + str(input_letter) + " found in " + str(input_word))
    else:
        print(
            str(count)
            + " instances of "
            + str(input_letter)
            + " found in "
            + str(input_word)
        )


# I am still confused why my print statement won't stay in one line, but it still runs


def main() -> None:  # I kept forgetting I need to define the return value as none
    word = input_word()
    character = input_letter()
    contains_char(word, character)


if __name__ == "__main__":
    main()  # similar formatt to calling our main planner in the first exercise
