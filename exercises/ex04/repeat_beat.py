"""Repeating a beat in a loop."""

__author__ = "730429363"


beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
if number <= 0:
    print("No beat...")
else:
    one_beat = beat
    while number > 1:
        number -= 1
        beat_space = beat + " "
        beat = beat_space + one_beat
    print(beat)