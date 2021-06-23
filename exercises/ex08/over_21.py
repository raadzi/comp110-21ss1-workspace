"""A program to determine names over 21."""

__author__ = "730429363"


def over_21(students: dict[str, int]) -> list[str]:
    """Determines which students are over 21."""
    drinking_age: list[str] = []
    for student in students:
        if students[student] <= 2000:
            drinking_age.append(student)
    return drinking_age