"""River simulation!"""

__author__: str = "730653429"

from exercises.ex07.river import River

my_river: River = River(num_fish=10, num_bears=2)


my_river.view_river()  # to view the number of days and population counts

my_river.one_river_week()  # to call one week of time
