"""An exercise with functions and lists."""

__author__ = "7304293963"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("This program will evaluate which prime numbers exist between two integers.")
    print("This includes the first integer, but not the second.")
    first_choice = int(input("Choose your first integer: "))
    second_choice = int(input("Choose your second integer: "))
    print(list_primes(first_choice, second_choice))


def is_prime(number: int) -> bool:
    """Determines whether or not a number is prime."""
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        x = 2
        remainder: int = number % x
        while (bool(remainder == 0) is False) and x < number:
            remainder = number % x
            x += 1
        if bool(remainder == 0) is True:
            return False
        else:
            return True


def list_primes(first_choice: int, second_choice: int) -> list[int]:
    """Determines whether the numbers between two integers are prime."""
    number = first_choice
    primes: list[int]
    primes = []
    if bool(is_prime(number)) is True:
        primes.append(number)
    number += 1
    while number < second_choice:
        if bool(is_prime(number)) is True:
            primes.append(number)
        number += 1
    return primes


if __name__ == "__main__":
    main()