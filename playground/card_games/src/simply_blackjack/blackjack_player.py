from .bet_pocket import BetPocket
from .player import Player


class BlackJackPlayer(Player):

    def __init__(self, name, BetPocket: BetPocket):
        self.name = name
        self.__pocket = BetPocket
        super().__init__()

    def __str__(self):
        return (
            f"Player {self.name} has {self.__pocket.total_money} money in the pocket."
        )

    def show_hand(self) -> None:
        print("---------------------------------------------")
        print(f"Player {self.name}, this is your hand:")
        for card in self.match_cards:
            print(f"- {card}")
        print("---------------------------------------------")

    def request_bet(self) -> int:
        while True:
            try:
                money_amount = int(
                    input("How much do you want to bet in this round ? ")
                )
            except ValueError:
                print("Please write value that be a number")
            else:
                break
        return self.__pocket.bet(money_amount)

    def bet_win(self, money_amount: int) -> None:
        self.__pocket.bet_won(money_amount)

    def show_total_cash(self) -> int:
        return self.__pocket.total_money
