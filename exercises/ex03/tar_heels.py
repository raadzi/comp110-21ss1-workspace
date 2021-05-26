"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


number: int = input("Enter an int: ")
if number > 2:
    if number !=1:
        print("You will take many nice naps this week.")
    else:
        print("Both sides of your pillow will be cold for the next month.")
else:
    if number < 2:
        print("You will succeed in Comp 110.")
    else:
        print("You will have a very slow day at work tomorrow, and no one will yell at you.")
print("Now, go spread positive vibes!")