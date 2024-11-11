"""File to define Bear class."""

____author___: str = "730653429"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age = 0
        self.hunger_scores = 0
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish
        return None