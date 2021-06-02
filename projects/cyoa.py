"""A choose your own adventure experience in which you date kevin g."""

__author__ = "730429363"


points: int = 0
player: str = "y/n"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    begin_adventure()
    return None


def greet() -> None:
    """Function to greet the player and begin their adventure."""
    print("Hello! Welcome to the Kevin G dating simulator! This hurts me more than it hurts you :)")
    global player
    player = str(input("What is your name? "))
    return None

def begin_adventure() -> int:
    global points
    print("Hello, " + player + "! It is a sunny day, and you have just finished watching the latest lecture for your Comp 110 class. You are excited to get started on your homework for the day, but you decide to check your email first. You open your inbox and see a message from none other than your university's chancellor himself!")
    print("You read the email and see that Kevin wants to go on a date with you! You... ")
    print("a) Respond to the email saying that you do not want to date Kevin. This choice ends the dating simulation.")
    print("b) Tell Kevin that it is a little weird that he is asking out a member of the UNC community, and you warily accept")
    print("c) Excitedly let Kevin know that you'd love to go on a date with him!")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        print("Understandable. I would do the same. Your Kevin Points are " + str(points))
    elif choice == "b":
        print("If you know it's weird, why are you agreeing?? Kinda sus to me tbh.")
        points += 1
    else:
        print("Bestie... are you okay? Did you take your meds today? I really hope you selected this one for the meme.")
        points += 2
    return int(points)


if __name__ == "__main__":
    main()