"""An exercise in computing the factorial of an int."""

__author__ = "730429363"


number: int = int(input("Choose a number: "))
factorial = number
while number > 1:
    number = number - 1
    factorial = number * factorial
print("Factorial: " + str(factorial))