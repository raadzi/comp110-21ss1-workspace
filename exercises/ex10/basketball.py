"""A class to model a basketball game."""

__author__ = "730429363"


class BBallGame:
    biscuits: bool
    points: int
    winning_team: str
    losing_team: str


    def __init__(self, points: int, winning_team: str, losing_team: str):
        self.biscuits: bool = False


    def check_points(self) -> None:
        if self.points >= 100:
            self.biscuits: bool = True
        

    def winner(self) -> str:
        if self.winning_team == "UNC" and self.losing_team == "Dook":
            return str("GTHD!!")
        elif self.winning_team == "UNC":
            return str("woohoo")
        else:
            return str("daggum")


    def reset_points(self) -> int:
        temp = int(self.points)
        self.points = int(0)
        return int(temp)