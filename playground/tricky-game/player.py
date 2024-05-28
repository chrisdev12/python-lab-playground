from inputUser import player_input
from gameContext.playerState import PlayerState

class Player(PlayerState):
    name = ""
    __winner = False

    def __init__(self, number, label):
        self.number = number
        self.label = label
        self._movements = []
    
    def setNameWithInput(self):
        self.name = input("Please put the player {pnumber} name: ".format(pnumber = self.number))
    
    
    @property
    def is_winner(self):
        return self.__winner
    
    @is_winner.setter
    def is_winner(self, winner_state):
        self.__winner = winner_state
    
    @property
    def movements(self):
        return self._movements

    def addMovement(self, newMove) -> None:
        self._movements.append(newMove)
    
    def play_turn(self, board_status):
        movement = player_input(board_status, self.name)
        self.addMovement(movement)
        
        return movement

