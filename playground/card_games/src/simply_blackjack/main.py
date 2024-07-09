"""
Milestone Project 2 - Blackjack Game simplified version

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

- You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses, or busts, etc...
- The Blackjack steps are described in the game_context.py file:

special rules

- Face cards (Jack, Queen, Kind) count as a value of 10
- Aces can count as either 1 or 11 whichever value is preferable to the player
"""

from ..common.deck import Deck
from .blackjack_card import BlackJackCard
from .game_context import GameContext
from .bet_pocket import BetPocket
from .blackjack_dealer import BlackJackDealer
from .blackjack_player import BlackJackPlayer


def main():
    new_deck = Deck(BlackJackCard)
    player_name = input("Please put the player name: ")
    while True:
        try:
            player_init_bucket_money = int(input("Please put your bet pocket amount: "))
        except ValueError:
            print("Please input that be a number")
        else:
            break
    bet_pocket = BetPocket(player_init_bucket_money)
    player = BlackJackPlayer(player_name, bet_pocket)
    dealer = BlackJackDealer()
    print(player)
    dealer = GameContext(new_deck, player, dealer)
    dealer.start_game()
