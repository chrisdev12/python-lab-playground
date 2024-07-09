from ..common.deck import Deck
from .blackjack_dealer import BlackJackDealer
from .blackjack_player import BlackJackPlayer

"""
- Create a deck of 52 cards
- Shuffle the deck
- Ask the Player for their bet
- Make sure that the Player's bet does not exceed their available chips
- Deal two cards to the Dealer and two cards to the Player
- Show only one of the Dealer's cards, the other remains hidden
- Show both of the Player's cards
- Ask the Player if they wish to Hit, and take another card
- If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
- If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
- Determine the winner and adjust the Player's chips accordingly
- Ask the Player if they'd like to play again
"""


class GameContext:

    def __init__(
        self,
        deck: Deck,
        player: BlackJackPlayer,
        dealer: BlackJackDealer,
        dealer_max_val_criteria: int = 17,
    ):
        self.__deck: Deck = deck
        self.__player: BlackJackPlayer = player
        self.__dealer: BlackJackDealer = dealer
        self.__deck.shuffle()
        self.__dealer_max_val_criteria = dealer_max_val_criteria
        self.__bet_pot = 0

    def start_game(self):
        is_game_active = True
        while is_game_active:
            self.play_match()
            ask_play_again = input(
                f"Do you want to play again Player: {self.__player.name}? : "
            )

            if ask_play_again.lower() == "no":
                is_game_active = False

    def play_match(self):
        print("playing a new match/round")
        player_bet = self.__player.request_bet()
        dealer_bet = player_bet * 0.7
        self.__bet_pot += player_bet + dealer_bet
        self.__first_card_deal()
        is_player_busted = self.__play_player_hand(self.__player)
        is_dealer_busted = False
        if not is_player_busted:
            is_dealer_busted = self.__play_dealer_hand()
        self.__resolve_match_result(is_player_busted, is_dealer_busted)
        self.__reset_match()

    def __first_card_deal(self):
        dealer_cards = [self.__deck.deal_one() for _ in range(2)]
        self.__dealer.add_cards(dealer_cards)
        player_cards = [self.__deck.deal_one() for _ in range(2)]
        self.__player.add_cards(player_cards)
        self.__dealer.show_partial_hand()
        self.__player.show_hand()

    def __play_player_hand(self, player: BlackJackPlayer) -> bool:
        is_busted = False
        while True:
            player_choice_stand = self.__is_user_standing()
            if player_choice_stand:
                break
            player.add_cards(self.__deck.deal_one())
            player.show_hand()
            if player.is_busted():
                print(f"Ops ! seems that {player.name} has Busted !")
                is_busted = True
                break

        return is_busted

    def __play_dealer_hand(self) -> bool:
        is_busted = False
        while True:
            self.__dealer.show_hand()
            if self.__dealer.is_busted():
                print(f"Ops ! seems that the dealer/house has Busted !")
                is_busted = True
                break
            if self.__dealer.get_hand_value() >= self.__dealer_max_val_criteria:
                print(f"Dealer Max hand-value criteria has been reached")
                break
            self.__dealer.add_cards(self.__deck.deal_one())

        return is_busted

    def __is_user_standing(self):
        user_choice_stand = False
        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
            if x[0].lower() == "h":
                break
            elif x[0].lower() == "s":
                print("Player stands. Dealer is playing.")
                user_choice_stand = True
            else:
                print("Sorry, please try again.")
                continue
            break

        return user_choice_stand

    def __reset_match(self):
        self.__player.reset_match_cards()
        self.__dealer.reset_match_cards()
        self.__bet_pot = 0

    def __resolve_match_result(self, is_player_busted: bool, is_dealer_busted: bool):
        is_player_winner = self.__is_player_winner(is_player_busted, is_dealer_busted)
        dealer_winner_message = f"oh sorry, player {self.__player.name} you have lost your bet. The house has won the bet pot {self.__bet_pot}"
        player_winner_message = f"Congrats player {self.__player.name} you have win the bet pot {self.__bet_pot}. House lost"
        if is_player_winner:
            print(player_winner_message)
            self.__player.bet_win(self.__bet_pot)
            return
        else:
            print(dealer_winner_message)
            return

    def __is_player_winner(self, is_player_busted: bool, is_dealer_busted: bool):
        if is_player_busted:
            return False
        if is_dealer_busted:
            return True
        dealer_count = 21 - self.__dealer.get_hand_value()
        player_count = 21 - self.__player.get_hand_value()

        return player_count < dealer_count
