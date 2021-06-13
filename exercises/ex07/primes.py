"""An exercise with functions and lists."""

__author__ = "7304293963"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Test your functions here


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    else:
        x = 2
        remainder = number % x
        while bool(remainder = 0) == False and x < number:
            x += 1


# TODO 2: Define the list_primes function, and its logic, here.


if __name__ == "__main__":
    main()