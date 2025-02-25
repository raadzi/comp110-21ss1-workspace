"""A function to abbreviate strings."""

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: str = str(input("Write some text with some uppercase letters: "))
    print("The abbreviation is \"" + abbreviate(choice) + "\".")
    return None


def abbreviate(text: str) -> str:
    """Function to abbreviate a string of text based on capitalization."""
    position: int = int(-1)
    abbreviation = ""
    while position <= (len(text) - 2):
        position += 1 
        if text[position].isupper():
            abbreviation += text[position]
    return str(abbreviation)


if __name__ == "__main__":
    main()