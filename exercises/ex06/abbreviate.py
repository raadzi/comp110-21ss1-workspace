"""A function to abbreviate strings."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: str = str(input("Write some text with some uppercase letters: "))
    print("The abbreviation is'" + abbreviate(choice) +"'")
    return None


def abbreviate(text: str) -> str:
    position = -1
    while position <= len(text):
        position += 1 
        if text[position].isupper():
            return text[position]


if __name__ == "__main__":
    main()