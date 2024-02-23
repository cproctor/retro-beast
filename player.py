from retro.agent import ArrowKeyAgent

class Player:
    character = '@'
    name = 'player'
    position = (1, 1)

    direction_vectors = {
        "KEY_RIGHT": [1, 0],
        "KEY_UP": [0, -1],
        "KEY_LEFT": [-1, 0],
        "KEY_DOWN": [0, 1]
    }

    def __init__(self, position):
        self.position = position

    def handle_keystroke(self, keystroke, game):
        """The player is controlled with the arrow keys. 
        The Player can freely move into empty spaces, 
        and can push blocks when there is empty space at the
        end of the block sequence being pushed.
        """
        if keystroke.name in self.direction_vectors:
            vector = self.direction_vectors[keystroke.name]
            self.try_to_move(vector, game)

    def try_to_move(self, vector, game):
        """Try to move in the direction of vector. If successful, return True.
        """
        x, y = self.position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        agent = self.get_agent_in_position(new_position, game)
        if agent:
            if agent.deadly:
                game.state['message'] = "Ooh... You don't want to walk into beasts..."
                game.end()
            if agent.accepts_incoming_block(vector, game):
                self.position = new_position
                return True
        else:
            self.position = new_position
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

