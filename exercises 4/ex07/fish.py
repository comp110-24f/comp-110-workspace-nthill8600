"""File to define Fish class."""

____author___: str = "730653429"


class Fish:
    age = int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1  # type: ignore
        return None
