from board import get_init_board, display_board
from player import Player
from gameContext.context import TrickyGameContext
from trickyAlgorithm import verify_tricky_winner


def init_game():
    player1 = Player(1, "X")
    player2 = Player(2, "O")
    player1.setNameWithInput()
    player2.setNameWithInput()

    print(
        "Welcome to the Tricky game. Player 1: {player1}, & Player 2: {player2} will face each other.".format(
            player1=player1.name, player2=player2.name
        )
    )
    print(
        """To play you will use the board below as a reference. At each turn you will be asked for your move,
and you must put a number from 1 to 9, where the number represents the box you want to mark.
Note: As the game progresses some boxes will already be occupied, and you only will be able to select the empty ones."""
    )
    init_board = get_init_board()
    display_board(init_board)
    play_game(player1, player2, init_board)
    # ToDo: Ask to repeat game


def play_game(player1, player2, init_board):
    player1.set_next_player(player2)
    player2.set_next_player(player1)
    game_context = TrickyGameContext(player1, player2, init_board, verify_tricky_winner)
    while game_context.is_game_active:
        game_context.play_turn()
        display_board(game_context.get_live_board)

    print(game_context.get_game_result)
    play_again = input("Are you ready to play? Enter Yes or No.").lower()[0] == "y"

    if play_again:
        init_game()


if __name__ == "__main__":
    init_game()
