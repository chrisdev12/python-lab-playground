from abc import ABC


class PlayerState(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    name = ""
    next_player = None

    def set_next_player(self, nextPlayer):
        self.next_player = nextPlayer

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    def next_turn(self) -> None:
        self._context.transition_to_state(self.next_player)
