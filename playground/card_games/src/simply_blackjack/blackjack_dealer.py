from abc import ABC, abstractmethod
from .player import Player


class Dealer(ABC):

    @abstractmethod
    def show_partial_hand(self) -> None:
        pass


class BlackJackDealer(Player, Dealer):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.__name

    def show_hand(self) -> None:
        print("---------------------------------------------")
        print(f"Dealer all hand:")
        for card in self.match_cards:
            print(f"- {card}")
        print("---------------------------------------------")

    def show_partial_hand(self) -> None:
        print("---------------------------------------------")
        print(f"Dealer partial hand - 1 hidden and 1 shown :")
        print(f"- {self.match_cards[0]}")
        print("---------------------------------------------")
