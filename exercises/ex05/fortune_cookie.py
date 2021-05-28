"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None


def fortune_cookie() -> str:
    number: int = int(randint(1, 4))
    if number <= 2:
        if number == 1:
            return "You will take many nice naps this week."
        else:
            return "Both sides of your pillow will be cold for the next month."
    else:
        if number != 4:
            return "You will succeed in Comp 110."
        else:
            return "You will have a very slow day at work tomorrow, and no one will yell at you."   


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()