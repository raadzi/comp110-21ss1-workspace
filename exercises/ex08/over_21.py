"""A program to determine names over 21."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    students: dict[str, int] = {"Isabelle": 2001, "Mae": 1999, "Riley": 2002, "Jean": 2000}
    print(over_21(students))


def over_21(students: dict[str, int]) -> list[str]:
    """Determines which students are over 21."""
    drinking_age: list[str] = []
    for student in students:
        if students[student] < 2000:
            drinking_age.append(student)
    return drinking_age


if __name__ == "__main__":
    main()