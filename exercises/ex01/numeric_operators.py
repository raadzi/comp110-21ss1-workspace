"""Shows the output of integers entered in python's numeric operators"""

__author__: str = "730429363"

left = input("Left-hand side: ")
left: int = int(left)
right:int = int(input("Right-hand side: "))
print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))