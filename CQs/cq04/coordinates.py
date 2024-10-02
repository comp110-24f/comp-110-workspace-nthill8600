____author___: str = "730653429"


def get_coords(xs: str, ys: str) -> None:
    index = 0
    while index < len(xs):
        count = 0
        while count < len(ys):
            print("(" + xs[index] + ", " + ys[count] + ")")
            count += 1
        index += 1
