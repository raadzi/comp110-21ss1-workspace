"""A program to determine top favorite colors."""

__author__ = "730429363"


def favorite_color(students: dict[str, str]) -> str:
    """Determines the most popular color."""
    colors: list[str] = []
    for student in students:
        colors.append(students[student])
    popularity: dict[str, int] = {}
    for color in colors:
        if color in popularity:
            popularity[color] += 1
        else:
            popularity[color] = 1
    result = colors[0]
    for color in colors:
        if popularity[color] > popularity[result]:
            result = color
    return result