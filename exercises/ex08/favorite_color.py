"""A program to determine top favorite colors."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    students: dict[str, str] = {"Isabelle": "brown", "Mae": "purple", "Riley": "purple", "Jean": "green"}
    print(favorite_color(students))


def favorite_color(students: dict[str, str]) -> str:
    """Determines the most popular color."""
    colors: dict[str, int] = []
    for student in students:
        if students[student] in colors:
            colors[students[student]] += 1
        else:
            colors.append([students[student], 1])
    for color in colors:
        most_popular: int(colors[color])
        if colors[color] > most_popular:
            most_popular = str(color)
    return most_popular


if __name__ == "__main__":
    main()