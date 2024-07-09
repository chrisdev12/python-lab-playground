from ..common.card import Card

"""
special rules

- Face cards (Jack, Queen, King) count as a value of 10
- Aces can count as either 1 or 11 whichever value is preferable to the player
"""


class BlackJackCard(Card):

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.__value = self.card_values[rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}, with value { self.__value if self.__value != self.multi_value_card else self.card_values[f"{self.rank}_{self.multi_value_card}"] }"

    @property
    def value(self) -> int:
        if self.__value == self.multi_value_card:
            return self.__get_multi_value_from_card()

        return self.__value

    @property
    def multi_value_card(self) -> str:
        return "multi_value"

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
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": self.multi_value_card,
            f"Ace_{self.multi_value_card}": (1, 11),
        }

    def __get_multi_value_from_card(self) -> int:
        chosen_value = None
        while True:
            try:
                dict_key = f"{self.rank}_{self.multi_value_card}"
                print(f"{self.rank} value has multiple-values")
                chosen_value = int(input(f"which {self.rank} value do you want to use: {self.card_values[dict_key]}: "))
            except ValueError:
                print(f"Please input a number that be {self.card_values[dict_key]}")
            else:
                break

        return chosen_value
