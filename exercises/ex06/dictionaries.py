"""Practice with dictionaries."""

__author__ = "730391001"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Switches keys and values."""
    new_dictionaries: dict[str, str] = {}

    for key in my_dict:
        if my_dict[key] in new_dictionaries:
            raise KeyError("Multiple similar key values.")
        else:
            new_dictionaries[my_dict[key]] = key
    return new_dictionaries


def main() -> None:
    """Start point."""
    print(favorite_color({"Dave": "Blue", "Sankalp": "red", "Shreyas": "green"}))


def favorite_color(my_dict: dict[str, str]) -> str:
    """Returns popular color."""
    high_count: int = 0
    favorite: str = ""
    type_of_color: str = ""

    for key in my_dict:

        count: int = 0
        type_of_color = my_dict[key]

        for i in my_dict:
            if my_dict[i] == type_of_color:
                count += 1
            if count > high_count:
                high_count = count
                favorite = type_of_color

    return favorite


def count(my_list: list[str]) -> dict[str, int]:
    """Returns a count of all entries."""
    my_dictionaries: dict[str, int] = {}

    for item in my_list:
        if item in my_dictionaries:
            my_dictionaries[item] += 1
        else:
            my_dictionaries[item] = 1
    
    return my_dictionaries