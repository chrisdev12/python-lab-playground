class TrickyGameContext:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """
    _is_game_active = True
    _player_state = None
    _game_tied_state = "Game ends in a tie"
    
    """
    A reference to the current state of the Context.
    """

    def __init__(self, player1, player2, init_board, tricky_winner_algorithm):
        self._player1 = player1
        self._player2 = player2
        self._current_board = init_board
        self._tricky_winner_algorithm = tricky_winner_algorithm
        self.transition_to_state(self._player1)

    def transition_to_state(self, player_state):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {player_state.name}")
        self._player_state = player_state
        self._player_state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def play_turn(self):
        if self._is_game_active:
            movement = self._player_state.play_turn(self.get_game_occupied_boxes)
            self._current_board[movement - 1] = self._player_state.label
            self.__verify_game_status()
            self._player_state.next_turn()

    def __verify_game_status(self):
        player_turn_result = self._tricky_winner_algorithm(self._player_state.movements)
        if player_turn_result:
            self._is_game_active = False
            self._player_state.is_winner = True
            return
        if len(self.get_game_occupied_boxes) == 9:
            self._is_game_active = False
            return

    @property
    def get_game_occupied_boxes(self):
        return self._player1.movements + self._player2.movements

    
    @property  
    def get_live_board(self):
        return self._current_board

    @property
    def is_game_active(self):
        return self._is_game_active
    
    @property
    def get_game_result(self):
        winner_name = self._player1.name if self._player1.is_winner else self._player2.name if self._player2.is_winner else None 
        return "the game has ended and the winner is " + winner_name if winner_name != None else self._game_tied_state
