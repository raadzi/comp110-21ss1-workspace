"""A program that draws some dudes woth some swords !!"""
"""Break up complex function: line and rectangle."""
"""I named my turtle after my cat."""

__author__ = "730429363"

from turtle import Turtle, colormode, done
colormode(255)


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


def top_hat(turtle: Turtle, x: float, y: float) -> None:
    teleport(turtle, x, y)
    return None


def triangle_hat(turtle: Turtle, x: float, y: float) -> None:
    teleport(turtle, x, y)
    return None


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    soupy: Turtle = Turtle()
    ground(soupy, 0, 0)
    soupy.left(90)
    dude(soupy, 45, 220)
    soupy.left(90)
    dude(soupy, 200, 220)
    sword(soupy, 110, 140)
    sword(soupy, 265, 140)
    done()
    return None


if __name__ == "__main__":
    main()