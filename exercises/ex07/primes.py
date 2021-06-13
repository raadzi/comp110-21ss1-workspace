"""An exercise with functions and lists."""

__author__ = "7304293963"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    number = int(input("Enter a number: "))
    is_prime(number)


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    else:
        x = 2
        remainder: int = number % x
        while (bool(remainder = 0) == False) and x < number:
            x += 1
        if bool(remainder = 0) == True:
            return False
        else:
            return True


# TODO 2: Define the list_primes function, and its logic, here.


if __name__ == "__main__":
    main()