"""A program that draws some dudes woth some swords !!"""
"""Break up complex function: line and rectangle."""
"""Methinks that time of day is the other aboe and beyond."""
"""I named my turtle after my cat."""

__author__ = "730429363"

from turtle import Turtle, colormode, done
colormode(255)
from random import randint


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    soupy: Turtle = Turtle()
    soupy.speed(0)
    time_of_day: int = randint(0, 1)
    if time_of_day == 0:
        day(soupy, 0, 0)
    else:
        night(soupy, 0, 0)
    ground(soupy, 0, 0)
    flower(soupy, 2.5, 70)
    soupy.left(90)
    dude(soupy, 45, 220)
    soupy.left(90)
    dude(soupy, 200, 220)
    sword(soupy, 110, 140)
    sword(soupy, 265, 140)
    done()
    return None


def teleport(turtle: Turtle, x: float, y: float) -> None:
    """Moves the turtle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    return None


def rectangle(turtle: Turtle, horizontal: float, vertical: float) -> None:
    """Draws a rectangle."""
    turtle.forward(horizontal)
    turtle.left(90)
    turtle.forward(vertical)
    turtle.left(90)
    turtle.forward(horizontal)
    turtle.left(90)
    turtle.forward(vertical)
    return None


def line(turtle: Turtle, start_x: float, start_y: float, end_x: float, end_y: float) -> None:
    teleport(turtle, start_x, start_y)
    turtle.goto(end_x, end_y)
    return None


def day(turtle: Turtle, x: float, y: float) -> None:
    teleport(turtle, x, y)
    turtle.pencolor(133, 214, 226)
    turtle.fillcolor(133, 214, 226)
    turtle.begin_fill()
    rectangle(turtle, 400, 400)
    turtle.pencolor("black")
    turtle.fillcolor("yellow")
    teleport(turtle, 100, 350)
    turtle.begin_fill()
    rectangle(turtle, 50, 50)
    turtle.end_fill()
    return None


def night(turtle: Turtle, x: float, y: float) -> None:
    teleport(turtle, x, y)
    turtle.pencolor(53, 0, 147)
    turtle.fillcolor(53, 0, 147)
    turtle.begin_fill()
    rectangle(turtle, 400, 400)
    turtle.pencolor("black")
    turtle.fillcolor("white")
    teleport(turtle, 100, 350)
    turtle.begin_fill()
    rectangle(turtle, 50, 50)
    turtle.end_fill()
    turtle.pensize(5)
    turtle.pencolor("white")
    i: int = 0
    while i <= 40:
        star_x: int = randint(1, 399)
        star_y: int = randint(71, 399)
        teleport(turtle, star_x, star_y)
        i += 1
    return None


def flower (turtle: Turtle, x: float, y: float) -> None:
    while x <= 397.5:
        teleport(turtle, x, y)
        turtle.pencolor("green")
        line(turtle, x, y, x, y + 10)
        turtle.pencolor("pink")
        turtle.pensize(5)
        line(turtle, x - 2.5, y + 7.5, x + 2.5, y + 12.5)
        line(turtle, x - 2.5, y + 12.5, x + 2.5, y + 7.5)
        turtle.pensize(1)
        x += 12
    turtle.pencolor("black")
    return None


def ground(turtle: Turtle, x: float, y: float) -> None:
    """Draws the ground of the scene."""
    teleport(turtle, x, y)
    turtle.color("green", "green")
    turtle.begin_fill()
    rectangle(turtle, 400, 70)
    turtle.end_fill()
    return None


def dude(turtle: Turtle, x: float, y: float) -> None:
    """Draws a lil dude."""
    teleport(turtle, x, y)
    turtle.pencolor("black")
    turtle.fillcolor(233, 209, 173)
    turtle.begin_fill()
    rectangle(turtle, 60, 60)
    turtle.end_fill()
    line(turtle, x + 30, y, x + 30, y - 80)
    line(turtle, x + 30, y - 10, x - 5, y - 80)
    line(turtle, x + 30, y - 10, x + 65, y - 80)
    line(turtle, x + 30, y - 80, x - 5, y - 150)
    line(turtle, x + 30, y - 80, x + 65, y - 150)
    return None


def sword(turtle: Turtle, x: float, y: float) -> None:
    teleport(turtle, x, y)
    turtle.fillcolor("gray")
    turtle.begin_fill()
    line(turtle, x, y, x + 10, y + 80)
    line(turtle, x + 4, y - 4, x + 14, y + 76)
    line(turtle, x, y, x + 4, y - 4)
    line(turtle, x + 10, y + 80, x + 12, y + 84)
    line(turtle, x + 14, y + 76, x + 12, y + 84)
    turtle.end_fill()
    return None


if __name__ == "__main__":
    main()