"""A program to determine top favorite colors."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    students: dict[str, str] = {"Isabelle": "brown", "Mae": "purple", "Riley": "purple", "Jean": "green"}
    print(favorite_color(students))


def favorite_color(students: dict[str, str]) -> str:
    """Determines the most popular color."""
    colors: list[str, int] = []
    for student in students:
        if str(favorite_color[student]) in colors:
            colors[str(favorite_color[student])] += 1
        else:
            colors.append([str(favorite_color[student]), 1])
    most_popular: int = colors[0]
    for color in colors:
        if color > most_popular:
            most_popular = color
    return most_popular


if __name__ == "__main__":
    main()