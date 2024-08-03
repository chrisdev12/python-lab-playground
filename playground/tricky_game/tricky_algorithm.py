winner_moves = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def verify_tricky_winner(player_moves):
    game_has_winner = False
    for moves in winner_moves:
        if all(m in player_moves for m in moves):
            game_has_winner = True
            break

    return game_has_winner
