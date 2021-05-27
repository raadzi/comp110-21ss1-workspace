"""An exercise in computing the factorial of an int."""

__author__ = "730429363"


number: int = int(input("Choose a number: "))
while number > 1:
    number = number - 1
    factorial = number * (number + 1)
print("Factorial: " + str(factorial))