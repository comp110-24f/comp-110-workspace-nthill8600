"""File to define Bear class."""

__author__: str = "730653429"


class Bear:
    """To initiate the Bear population class."""

    age: int
    hunger_score: int

    def __init__(self):
        """To initiate the attributes of a bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """To simulate how the bear changes over a day."""
        # in one day, the bears age increases by one
        self.age += 1
        self.hunger_score -= 1  # the hunger score decreases by 1
        return None

    def eat(self, num_fish: int) -> None:
        """To simulate the bear eating."""
        self.hunger_score += num_fish  # hunger score increases by eating fish
        return None
