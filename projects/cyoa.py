"""A choose your own adventure experience in which you date Kevin G."""
"""Idk why this got so long."""
"""Okay I finished, I deeply apologize."""
"""I'm pretty sure the pay function counts as above and beyond."""

__author__ = "730429363"


points: int = 0
player: str = "y/n"
SMILE = "\U0001F600"	
ANXIOUS = "\U0001F630"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    global points
    while points >= 0:
        print(f"Hello, {player}! It is a sunny day, and you've just finished watching today's Comp 110 lecture.")
        print("You're excited to get started on your homework for the day, but you decide to check your email first.")
        print("You open your inbox and see a message from none other than your university's chancellor himself!")
        print("You read the email and see that Kevin wants to go on a date with you! You... ")
        print("a) Respond to the email saying that you don't want to date Kevin. This choice ends the dating sim.")
        print("b) Ignore Kevin's email.")
        print("c) Excitedly let Kevin know that you'd love to go on a date with him!")
        choice: str = str(input("What do you do? "))
        if choice == "a":
            points += 1
            print(f"Understandable. I would do the same. Your Kevin Points are {points}.")
        elif choice == "b":
            print("Honestly, same. Responding to emails is so laborsome.")
            points += 2
            ignore_email()
            print(f"Your Kevin Points are {points}.")
        else:
            points += 5
            points = respond_email(points)
            restaurant()
            print(f"Your Kevin Points are {points}.")
        print("Would you like to play again?")
        print("a) yes")
        print("b) no")
        play_again: str = str(input("Answer: "))
        if play_again == "b":
            points = -1
        else:
            points = 0
    return None


def greet() -> None:
    """Function to greet the player and begin their adventure."""
    print(f"Hello! Welcome to the Kevin G dating simulator! This hurts me more than it hurts you {SMILE}")
    global player
    player = str(input("What is your name? "))
    return None


def ignore_email() -> None:
    """Custom procedure call when player ignores kevin's email."""
    global points
    print("After a day, Kevin emails you yet again. The email says...")
    print(f"\"{player},")
    print("It appears that you did not recieve my first email. Would you like to go on a date?\"")
    print("You...")
    print("a) Tell him to stop bothering you. You're not interested.")
    print("b) Tell him that you accept the invite, but only because he's annoying you.")
    choice: str = str(input("What do you do? "))
    if choice == "a":
        points += 1
        print("As you should. Men are gross anyways. This ends your dating simulation.")
    else:
        print("Okay, but please know that you shouldn't say yes to men just because they're bothering you.")
        print("It is important that you stand your ground, no matter how much men pester you.")
        print("Anyways... along with the dating sim!")
        points += 2
        points = int(respond_email(points))
        restaurant()
    return None


def respond_email(number: int) -> int:
    """What occurs when you positively respond to kevin's email."""
    print("Kevin quickly responds to your email:")
    print(f"\"{player},")
    print("Perfect! We should meet for dinner at 7 tomorrow!")
    print("Where would you like to go?\"")
    print("a) Chipotle")
    print("b) Panera")
    choice: str = str(input("Which restaurant do you choose? "))
    if choice == "a":
        number += 1  
    else:
        number += 3
    return int(number)


def restaurant() -> None:
    """What happens at the restaurant you chose."""
    global points
    if points > 6:
        print("You chose Panera!")
        points = int(pay(points))
        print("At the end of the meal, Kevin reveals to you that he thinks the date went really well.")
        print("He says he feels comfortable enough with you to reveal his deepest secret.")
        print("He unzips his fly and pulls out a leopard gecko.")
        print("He says that this is his pet that he has been hiding from the world.")
        print(geckos_name())
        print("You get weirded out and leave the date immediately.")
    else:
        print("You chose Chipotle!")
        points = int(pay(points))
        print(f"Unfortunately for you, Chipotle upsets Kevin's fragile little tummy. {ANXIOUS}")
        print("He gets gassy, and the date ends.")
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
    return int(number)


def geckos_name() -> str:
    """Determines the gecko's name."""
    from random import randint
    number: int = int(randint(1, 4))
    if number <= 2:
        if number == 1:
            return "The gecko's name is Jared."
        else:
            return "The gecko's name is Leaf Crunchy the Gecko."
    else:
        if number != 4:
            return "The gecko's name is Turnip."
        else:
            return "The gecko's name is Walter."


if __name__ == "__main__":
    main()