class Block:
    """A Block sits there. Blocks can be pushed.
    """
    character = "█"
    color = "green"
    deadly = False

    def __init__(self, position):
        self.position = position

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

    def accepts_incoming_block(self, vector, game):
        return self.try_to_move(vector, game)

    def try_to_move(self, vector, game):
        """Try to move in the direction of vector. If successful, return True.
        """
        x, y = self.position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        agent = self.get_agent_in_position(new_position, game)
        if agent:
            if agent.accepts_incoming_block(vector, game):
                self.position = new_position
                return True
        else:
            self.position = new_position
            return True

class ImmovableBlock:
    """A block that cannot move.
    """
    character = "█"
    color = "yellow"
    deadly = False

    def __init__(self, position):
        self.position = position

    def accepts_incoming_block(self, vector, game):
        return False

