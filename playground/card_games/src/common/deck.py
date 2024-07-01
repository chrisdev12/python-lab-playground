import random

##TODO : DECOUPLE DECK FROM CARD - Pass the card obj in the constructor instead
from .card import Card, default_values


class Deck:

    def __init__(
        self,
        suits: tuple[str, ...],
        ranks: tuple[str, ...],
        card_values: dict[str, int] = default_values,
    ):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank, card_values))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

    def init_match(self):
        print(
            """
        --------------------
        All cards available
        --------------------
            """
        )

        for card in self.all_cards:
            print(card)

        print(
            """
        -------------------------------------
        Shuffle perfomed - New cards position
        -------------------------------------
            """
        )

        self.shuffle()

        for card_after_suffle in self.all_cards:
            print(card_after_suffle)
