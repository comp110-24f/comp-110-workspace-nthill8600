"""Practicing with dictionary functions!"""

____author___: str = "730653429"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """To invert a dictionary"""
    inverted_dict = {}  # start an empty dictionary

    for key in dictionary:
        value = dictionary[key]
        if value in inverted_dict:  # if duplicate key raise error
            raise KeyError("Duplicate value found.")
        inverted_dict[value] = key
    return inverted_dict  # return the new dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """To determine the most popular color in a dictionary"""
    if dictionary == {}:
        return ""  # return empty string if dictionary is empty

    color_counter = {}  # start an empty dict to count colors
    order_of_appearance = []  # start an empty dict to maintain order of appearance

    for name in dictionary:
        color = dictionary[name]

        if color not in color_counter:
            order_of_appearance.append(color)  # first appearance
            color_counter[color] = 0

        color_counter[color] += 1

    most_popular = order_of_appearance[
        0
    ]  # define new variable thats equal to first order of appearance
    max_count = color_counter[most_popular]

    # find color with the maximum count
    for color in order_of_appearance:
        if color_counter[color] > max_count:
            most_popular = color
            max_count = color_counter[color]

    return most_popular  # return the most popular


def count(values: list[str]) -> dict[str, int]:
    """To count the frequency of items in a list"""
    result_dict: dict[str, int] = {}  # start an empty dict for result

    for item in values:
        if item in result_dict:
            result_dict[item] += 1  # if present add count
        else:
            result_dict[item] = 1  # start count for new item
    return result_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Order words by their first letter"""
    result: dict[str, list[str]] = {}  # start an empty dict for the result

    for word in words:
        first_letter = word[0].lower()  # to change first letter to lowercase
        if first_letter not in result:
            result[first_letter] = []  # create a new list if the letter is not present
        result[first_letter].append(word)  # add word to the list
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day_of_week: str, student: str
) -> None:
    """To update the attendance log for a student"""
    if day_of_week in attendance_log:
        if student not in attendance_log[day_of_week]:
            attendance_log[day_of_week].append(
                student
            )  # add students attendance to that day
    else:
        attendance_log[day_of_week] = [student]  # adds students attendance to a new day
