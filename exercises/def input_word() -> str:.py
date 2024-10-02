def input_word() -> str:
    # Gather input from the user
    word = input("Enter a 5-character word: ")

    # Check the length of the input word
    if len(word) != 5:
        # Print error message if length is not 5
        print("Error: Word must contain 5 characters.")

    # Return the input word regardless of its length
    return word


# Example usage (for interactive testing):
if __name__ == "__main__":
    print(input_word())  # For interactive testing
