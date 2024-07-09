class NotEnoughtMoneyError(Exception):
    pass


class BetPocket:
    def __init__(self, total_money: int):
        self.__total_money = total_money

    @property
    def total_money(self) -> int:
        return self.__total_money

    def bet_won(self, amount_won: int) -> None:
        self.__total_money += amount_won

    def bet(self, bet_amount: int) -> int:
        if bet_amount > self.__total_money:
            raise NotEnoughtMoneyError(
                f"Requested to take {bet_amount} coins, but only {self.pocket_money} coins are left"
            )
        self.__total_money -= bet_amount

        return bet_amount
