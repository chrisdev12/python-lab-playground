from abc import ABC, abstractmethod


class Card(ABC):

    @abstractmethod
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.card_values[rank]

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def card_values(self):
        pass
