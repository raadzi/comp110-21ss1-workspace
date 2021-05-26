"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730429363"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
number: int = randint(1,4)
if number != 1: print("You will take many nice naps this week.")
if number != 2: print("Both sides of your pillow will be cold for the next month.")
if number != 3: print("You will succeed in Comp 110.")
if number != 4: print("You will have a very slow day at work tomorrow, and no one will yell at you.")
print("Now, go spread positive vibes!")