"""File to define River class."""

__author__: str = "730653429"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

"""To import the fish and bear classes to the river."""


class River:
    """Defining the river that has fish and bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def one_river_week(self):
        """To go through seven days of the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def check_ages(self):
        """Checks the age the animals, as animals die with age."""
        surviving_fish = []  # start a new list of surviving fish

        for fish in self.fish:
            if fish.age <= 3:  # type: ignore # if the fish are over 3 they dont survive
                surviving_fish.append(
                    fish
                )  # add the fish under 3 to the surviving list

        surviving_bears = []  # new list of surviving bears
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(
                    bear
                )  # add bears to list if they are under 5 yrs old

        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """To remove an amount of fish from the river."""
        if len(self.fish) >= amount:
            self.fish = self.fish[amount:]  # remove the amount of fish
        else:
            self.fish = []  # if there are no fish left
        return None

    def bears_eating(self):
        """To simulate a bear eating 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # the bear ate 3 fish
                bear.eat(3)  # call the eat function in the Bear class
            else:
                return None
        return None

    def check_hunger(self):
        """To check if the bears are starved to death."""
        surviving_bears: list[Bear] = []  # make a new list of surviving bears
        for bear in self.bears:
            if bear.hunger_score >= 0:  # if the bear isnt starved
                surviving_bears.append(bear)  # add to surviving bears list

        self.bears = surviving_bears

        return None

    def repopulate_fish(self):
        """To simulate the breeding of fish."""
        num_fish = len(self.fish)  # the current number of fish
        num_pairs = num_fish // 2  # number of fish divided by 2 b/c of mating

        for _ in range(num_pairs * 4):  # each pair produces 4 offspring
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """To simulate the breeding of bears."""
        num_bears = len(self.bears)  # the current number of bears
        num_pairs = num_bears // 2  # the number of bears divided by 2 b/c of mating

        for _ in range(0, num_pairs):
            self.bears.append(Bear())  # add one bear to the population
        return None

    def view_river(self):
        """To check how many fish and bears there are on a certain day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
