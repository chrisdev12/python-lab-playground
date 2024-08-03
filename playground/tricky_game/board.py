def display_board(board):
    print("   |   | ")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("   |   |")
    print("-----------")
    print("   |   | ")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |")


def get_init_board():
    return list(range(1, 10))
