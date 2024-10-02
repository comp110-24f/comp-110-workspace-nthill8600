# creating an empty lists

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(1.5)
print(my_numbers)

# strign analogy
# my_name: str = "" # literal
# my_name: str = str() constructor

game_points: list[int] = [102, 86, 94]
print(game_points)

# subscripption notation/indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# modifying game points
game_points[1] = 72
