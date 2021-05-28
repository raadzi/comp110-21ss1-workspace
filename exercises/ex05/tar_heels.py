"""Tar Heels exercise redux as a structured program."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    tar_heels(choice)
    print(tar_heels())
    return None

def tar_heels(number: int) -> str:
    number == choice
    if number % 2 == 0:
        if number % 7 == 0:
            return "TAR HEELS"
        else:
            return "TAR"
    else:
        if number % 7 == 0:
            return "HEELS"
        else:
            return "CAROLINA"


if __name__ == "__main__":
    main()