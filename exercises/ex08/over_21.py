"""A program to determine names over 21."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Write the names and birth years of the students that you want to know are over 21 or not.")
    print("Format this entry with their name in quotes followed by a colon and their birth year.")
    print("Separate each entry with a comma. Eaxample:")
    print("\"Isabelle\": 2001, \"Jason\": 1999, \"Caroline\": 2002, \"Riley\": 2000")
    students = dict[str, int](input(""))
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