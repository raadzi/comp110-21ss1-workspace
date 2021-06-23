"""A class to model a basketball game."""

__author__ = "730429363"


class BBallGame:
    """BBallGame class created uwu."""
    biscuits: bool
    points: int
    winning_team: str
    losing_team: str

    def __init__(self, points: int, winning_team: str, losing_team: str):
        """Constructor of the class."""
        self.points: int = points
        self.winning_team: str = winning_team
        self.losing_team: str = losing_team
        self.biscuits: bool = False

    def check_points(self) -> None:
        """Checks if there is enough points for biscuits."""
        if self.points >= 100:
            self.biscuits: bool = True

    def winner(self) -> str:
        """Return based on whether UNC wins and if it is against Duke."""
        if self.winning_team == "UNC" and self.losing_team == "Dook":
            return str("GTHD!!")
        elif self.winning_team == "UNC":
            return str("woohoo")
        else:
            return str("daggum")

    def reset_points(self) -> int:
        """Resets the points and returns current points."""
        temp = int(self.points)
        self.points = int(0)
        return int(temp)