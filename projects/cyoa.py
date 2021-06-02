"""A choose your own adventure experience in which you date kevin g."""

__author__ = "730429363"


points: int = 0
player: str = "y/n"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    global points
    print("Hello, " + player + "! It is a sunny day, and you've just finished watching the latest lecture for your Comp 110 class.")
    print("You're excited to get started on your homework for the day, but you decide to check your email first.")
    print("You open your inbox and see a message from none other than your university's chancellor himself!")
    print("You read the email and see that Kevin wants to go on a date with you! You... ")
    print("a) Respond to the email saying that you do not want to date Kevin. This choice ends the dating simulation.")
    print("b) Ignore Kevin's email.")
    print("c) Excitedly let Kevin know that you'd love to go on a date with him!")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        points += 1
        print("Understandable. I would do the same. Your Kevin Points are " + str(points) + ".")
    elif choice == "b":
        print("Honestly, same. Responding to emails is so laborsome.")
        points += 2
        ignore_email()
    else:
        print("Bestie... are you okay? Did you take your meds today? I really hope you selected this one for the meme.")
        points += 5
        respond_email(points)
    return None


def greet() -> None:
    """Function to greet the player and begin their adventure."""
    print("Hello! Welcome to the Kevin G dating simulator! This hurts me more than it hurts you :)")
    global player
    player = str(input("What is your name? "))
    return None


def ignore_email() -> None:
    global points
    print("After a day, Kevin emails you yet again. The email says...")
    print("\"" + player + ",")
    print("It appears that you did not recieve my first email. Would you like to go on a date?")
    print("You...")
    print("a) Tell him to stop bothering you. You're not interested.")
    print("b) Tell him that you accept the invite, but only because he's annoying you.")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        points += 1
        print("As you should. Men are gross anyways. Your Kevin Points are " + str(points) + ".")
    else:
        print("Okay, but please know that you shouldn't say yes to men just because they're bothering you.")
        print("It is important that you stand your ground, no matter how much men pester you.")
        points += 2
        respond_email()
    return None


def respond_email(number: int) -> int:
    global points

if __name__ == "__main__":
    main()