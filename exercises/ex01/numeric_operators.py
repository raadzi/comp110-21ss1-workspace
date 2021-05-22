"""This program shows the output of integers entered in python's numeric operators."""

__author__: str = "730429363"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))