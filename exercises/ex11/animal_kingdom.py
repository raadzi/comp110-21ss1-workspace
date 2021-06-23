"""A program that explores the animal kingdom."""

from __future__ import annotations

__author__ = "730429363"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    

class Animal:
    species: str
    danger_level: int
    emoji: str

    def __init__(self, species: str, danger_level: int, emoji: str):
        self.species: str = species
        self.danger_level: str = danger_level
        self.emoji: str = emoji
    
    def fight(self, opponent: Animal) -> Animal:
        if self.danger_level > opponent.danger_level:
            return self
        else:
            return opponent

class Team:
    team_name: str
    animals: list[Animal]
    score: int

    def __init__(self, team_name: str, animals: list[Animal]):
        self.team_name: str = team_name
        self.animals: list[Animal] = animals
        self.score: int = 0

    def battle(self, opponent: Team) -> list[Animal].battle:
        i = 0
        winners: list[Animal] = []
        while i < len(self.animals) and i < opponent.animals:
            if self.animals[i].fight(self, opponent.animals[i]) == self.animals[i]:
                self.score += 1
                winners.append(self.animals[i])
            else:
                opponent.score += 1
                winners.append(opponent.animals[i])
            i += 1
        return winners

    def who_won(self, opponent: Team) -> str.who_won:
        if self.score == 0 and opponent.score == 0:
            return str("The battle hasn't happened yet")
        elif self.score == opponent.score:
            return str("It was a tie!")
        elif self.score >= opponent.score:
            return str(f"Team {self.team_name} won!")
        else:
            return str(f"Team {opponent.team_name} won!")

if __name__ == "__main__":
    main()