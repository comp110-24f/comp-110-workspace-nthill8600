""""I am writing a program to plan a tea party! """

__author__: str = "730653429"


def main_planner(guests: int) -> None:
    """A cozy tea party!"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(round(cost(tea_bags(guests), treats(guests)), 2)))
    return None


"""The main issue I had with the main planner was that"""
"""I had punctuation and spacing errors this made it so"""
"""the autograder wasn't giving me full points. I went to office hours"""
"""and the TA pointed it out. In the next exercise I'll be sure to make sure"""
"""there are no simple errors in my code."""


def tea_bags(people: int) -> int:
    """To count how many tea bags we need depending on the amount of guests."""
    return int(people * 2)


"""This was definitely the easiest function to define since it """
"""didn't call to another function. This was like the ones we have"""
"""been doing in class and it didn't take me very long"""
"""to figure out."""


def treats(people: int) -> int:
    """To measure how many treats we need based on the number of people."""
    return int(tea_bags(people=people) * 1.5)


"""For this return I kept wanting to just put people"""
"""* 1.5 but I was missing the fact that we needed to call"""
"""back ot the tea bags function first. I also had just"""
"""put people not people=people so the autograder was """
"""taking off points. The TA in office hours helped"""
"""me figure out this error."""


def cost(tea_bags: int, treats: int) -> float:
    """To calculate the price of tea bags and treats combined!"""
    return float(tea_bags * 0.5 + treats * 0.75)


"""This function actually was the easiest to"""
"""think of and didn't really take me longer than 2 minutes. """
"""It didn't really give me any trouble."""


if __name__ == "__main__":
    main_planner(int(input("How many guests are attending your tea party?")))


"""For this part I was missing the integer part for some"""
"""time and also had errors with the parentheses. """
"""I didn't even realize there was a problems section """
"""on the terminal till I was basically done with the """
"""assignment but now I know for next time because it is """
"""super helpful in detecting the issues."""
