from abc import ABC, abstractmethod
from ..common.card import Card


class Player(ABC):

    def __init__(self):
        self.__match_cards: list[Card] = []

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def show_hand(self) -> None:
        pass

    @property
    def match_cards(self) -> list[Card]:
        return self.__match_cards

    def get_hand_value(self) -> int:
        total_cards_value = sum([card.value for card in self.__match_cards])

        return total_cards_value

    def is_busted(self) -> bool:
        return self.get_hand_value() > 21

    def reset_match_cards(self) -> None:
        self.__match_cards = []

    def add_cards(self, new_cards) -> None:
        if type(new_cards) == type([]):
            self.__match_cards.extend(new_cards)
        else:
            self.__match_cards.append(new_cards)
