"""Repeating a beat in a loop."""

__author__ = "730429363"


beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it: "))
if number <= 0:
    print("No beat...")
else:
    while number >= 1:
        print(beat + " ")
        number -= 1