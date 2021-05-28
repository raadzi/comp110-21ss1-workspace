"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print("Now, go spread positive vibes!")


def fortune_cookie -> str:
    print("Your fortune cookie says...")
    number: int = int(randint(1, 4))
    if number <= 2:
        if number == 1:
            print("You will take many nice naps this week.")
        else:
            print("Both sides of your pillow will be cold for the next month.")
    else:
        if number != 4:
            print("You will succeed in Comp 110.")
        else:
            print("You will have a very slow day at work tomorrow, and no one will yell at you.")
    print("Now, go spread positive vibes!")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()