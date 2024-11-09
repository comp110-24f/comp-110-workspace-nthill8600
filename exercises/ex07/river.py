"""File to define River class."""

____author___: str = "730653429"


from ex07.fish import Fish
from ex07.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def one_river_week(self):
        days_passed = 0
        while days_passed < 7:
            self.one_river_day()
            days_passed += 1
        return None

    def check_ages(self):
        new_fish: list[str] = []

        for fish in self.fish:
            if fish.age <= 3:  # type: ignore
                new_fish.append(fish)  # type: ignore

        self.fish = new_fish  # type: ignore #

        new_bear: list[str] = []

        for bear in self.bears:
            if bear.age <= 5:
                new_bear.append(bear)  # type: ignore

        self.bear = new_bear

        return None

    def remove_fish(self, amount: int) -> None:
        for index in range(min(amount, len(self.fish))):  # type: ignore
            self.fish.pop(0)
        return None

    def bears_eating(self):
        fish_count: int = len(self.fish)
        for bear in self.bears:
            if fish_count >= 5:
                self.remove_fish(3)
                bear.eat(3)
                fish_count -= 3
            else:
                return None
        return None

    def check_hunger(self):
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)

        self.bears = surviving_bears

        return None

    def repopulate_fish(self):
        num_new_fish = len(self.fish) // 2 * 4

        for index in range(num_new_fish):  # type: ignore
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2

        for index in range(num_new_bears):  # type: ignore
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
