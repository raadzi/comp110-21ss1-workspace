"""Tar Heels exercise redux as a structured program."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels())
    tar_heels(choice: int)
    return None

def tar_heels(choice: int) -> str:
    if choice % 2 == 0:
        if choice % 7 == 0:
            return "TAR HEELS"
        else:
            return "TAR"
    else:
        if choice % 7 == 0:
            return "HEELS"
        else:
            return "CAROLINA"


if __name__ == "__main__":
    main()