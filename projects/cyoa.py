"""A choose your own adventure experience in which you date Kevin G."""
"""Idk why this got so long."""
"""Okay I finished, I deeply apologize."""
"""I'm pretty sure the pay function counts as above and beyond."""

__author__ = "730429363"


points: int = 0
player: str = "y/n"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    global points
    print("Hello, " + player + "! It is a sunny day, and you've just finished watching today's Comp 110 lecture.")
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
        print("Your Kevin Points are " + str(points) + ".")
    else:
        print("Bestie... are you okay? Did you take your meds today?")
        print("I really hope you selected this one for the meme.")
        points += 5
        points = respond_email(points)
        print("Your Kevin Points are " + str(points) + ".")
    return None


def greet() -> None:
    """Function to greet the player and begin their adventure."""
    print("Hello! Welcome to the Kevin G dating simulator! This hurts me more than it hurts you :)")
    global player
    player = str(input("What is your name? "))
    return None


def ignore_email() -> None:
    """Custom procedure call when player ignores kevin's email."""
    global points
    print("After a day, Kevin emails you yet again. The email says...")
    print("\"" + player + ",")
    print("It appears that you did not recieve my first email. Would you like to go on a date?\"")
    print("You...")
    print("a) Tell him to stop bothering you. You're not interested.")
    print("b) Tell him that you accept the invite, but only because he's annoying you.")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        points += 1
        print("As you should. Men are gross anyways.")
    else:
        print("Okay, but please know that you shouldn't say yes to men just because they're bothering you.")
        print("It is important that you stand your ground, no matter how much men pester you.")
        print("Anyways... along with the dating sim!")
        points += 2
        respond_email(points)
    return None


def respond_email(number: int) -> int:
    """What occurs when you positively respond to kevin's email."""
    print("Kevin quickly responds to your email:")
    print("\"" + player + ",")
    print("Perfect! We should meet for dinner at 7 tomorrow!")
    print("Where would you like to go?\"")
    print("a) Chipotle")
    print("b) Panera")
    choice: str = str(input("Which restaurant do you choose? "))
    if choice == "a":
        number += 1
        restaurant()
    else:
        number += 3
        restaurant()
    return int(number)


def restaurant() -> None:
    """What happens at the restaurant you chose."""
    global points
    if points <= 6:
        print("You chose Chipotle!")
        points = pay(points)
        print("Unfortunately for you, Chipotle upsets Kevin's fragile little tummy.")
        print("He gets gassy, and the date ends.")
    else:
        print("You chose Panera!")
        points = pay(points)
        print("At the end of the meal, Kevin reveals to you that he thinks the date went really well.")
        print("He says he feels comfortable enough with you to reveal his deepest secret.")
        print("He unzips his fly and pulls out a leopard gecko.")
        print("He says that this is his pet that he has been hiding from the world.")
        print("The gecko's name is Jared.")
        print("You get weirded out and leave the date immediately.")
    return None


def pay(number: int) -> int:
    """What happens when you pay for your meal."""
    print("When you go to pay at the counter, Kevin offers to pay for your meal. You...")
    print("a) Accept his offer.")
    print("b) Pay for your own food.")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        number += 2
        print("Kevin likes that you let him pay for you.")
        print("He likes to show off his excessive amount of money that he earns off of your tuition.")
    else:
        number += 1
        print("This disappoints Kevin. He really wanted to show off his excessive wealth.")
        print("Because he has been charging full tuition for online school, he has plenty of money to spare.")
    return number(int)


if __name__ == "__main__":
    main()