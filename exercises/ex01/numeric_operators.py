"""Shows the output of integers entered in python's numeric operators"""

__author__: str = "730429363"

left = input("Left-hand side: ")
left: int = int(left)
right = input("Right-hand side: ")
right: int = int(right)
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))