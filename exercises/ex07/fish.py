"""File to define Fish class."""

__author__: str = "730653429"


class Fish:
    """To initiate the Fish population class."""

    age = int

    def __init__(self):
        """To initiate the attributes of a fish."""
        self.age = 0  # initiate the fish being born with age zero
        return None

    def one_day(self):
        """To simulate how a fish changes over a day."""
        self.age += 1  # type: ignore # the fish ages 1 by a day
        return None
