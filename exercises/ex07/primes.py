"""An exercise with functions and lists."""

__author__ = "7304293963"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("This program will evaluate which prime numbers exist between two integers. This includes the first integer, but not the second.")
    first_choice = int(input("Choose your first integer: "))
    second_choice = int(input("Choose your second integer: "))
    print(is_prime(number))


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    else:
        x = 2
        remainder: int = number % x
        while (bool(remainder == 0) == False) and x < number:
            x += 1
        if bool(remainder == 0) == True:
            return False
        else:
            return True


def list_primes(first_choice: int, second_choice: int) -> list[int]:
    number = first_choice
    primes: list[int]
    while number < second_choice:
        if bool(is_prime(number) == True):
            primes.append(number)
        number += 1
    return primes

if __name__ == "__main__":
    main()