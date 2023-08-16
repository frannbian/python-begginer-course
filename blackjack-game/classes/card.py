class Card:
    def __init__(self, suit: str, rank: dict) -> None:
        self.suit = suit
        self.rank = rank
    def __str__(self) -> str:
        return f"{self.rank['rank']} of {self.suit}"