from strategy import (
    random_move,
    move_toward_player,
)

class Beast:
    """A Beast is a monster which tries to eat the player.
    The goal of the game is to squash all the Beasts.
    """
    character = "H"
    color = "red"
    deadly = True
    speed = 15

    def __init__(self, position):
        self.position = position

    def play_turn(self, game):
        if game.turn_number % self.speed == 0:
            move = move_toward_player(self.position, game)
            if move:
                x, y = self.position
                dx, dy = move
                self.position = (x + dx, y + dy)
                if self.position == game.get_agent_by_name("player").position:
                    game.state['message'] = "Yum."
                    game.end()

    def accepts_incoming_block(self, vector, game):
        x, y = self.position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        if self.get_agent_in_position(new_position, game):
            game.remove_agent(self)
            return True

    def get_agent_in_position(self, position, game):
        """Returns an agent at the position, or returns None. 
        game.get_agents_by_position always returns a list, which may
        contain zero, one, or multiple agents at the given position. 
        In the Beast game, we never allow more than one agent to be in 
        a position.
        """
        agents = game.get_agents_by_position()[position]
        if agents:
            return agents[0]
