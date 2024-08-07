from ..common.card import Card


class WarGameCard(Card):

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.card_values[rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    @property
    def card_values(self):
        return {
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14,
        }
