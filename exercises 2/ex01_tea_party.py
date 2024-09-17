""""I am writing a program to plan a tea party! """

__author__: str = "730653429"


def main_planner(guests: int) -> None:
    """A cozy tea party for two!"""
    print("Planning a Tea Party")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats needed: " + str(treats(guests)))
    print("Total cost: $" + str(round(cost(tea_bags(guests), treats(guests)), 2)))
    return None


def tea_bags(people: int) -> int:
    """To count how many tea bags we need depending on the amount of guests."""
    return int(people * 2)


def treats(people: int) -> int:
    """To measure how many treats we need based on the number of people."""
    return int(tea_bags(people) * 1.5)


def cost(tea_bags: int, treats: int) -> float:
    """To calculate the price of tea bags and treats combined!"""
    return float(tea_bags * 0.5 + treats * 0.75)


if __name__ == "__main__":
    main_planner(int(input("How many guests are attending your tea party?")))
