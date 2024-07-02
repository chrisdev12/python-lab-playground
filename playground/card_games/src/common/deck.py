import random

from .card import Card

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)


class Deck:

    def __init__(
        self,
        Card: Card,
    ):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

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
