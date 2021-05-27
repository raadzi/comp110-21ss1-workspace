"""An exercise in computing the factorial of an int."""

__author__ = "730429363"


number: int = int(input("Choose a number: "))
if number <= 1:
    factorial = 1
else:
    factorial = number
    while number > 1:
        number = number - 1
        factorial = number * factorial
print("Factorial: " + str(factorial))