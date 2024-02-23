from random import choice

direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def possible_moves(position, game):
    "Returns a list of vectors to empty spaces"
    agents_by_position = game.get_agents_by_position()
    possible_moves = []
    for vector in direction_vectors:
        x, y = position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        if not agents_by_position[new_position]:
            possible_moves.append(vector)
    return possible_moves

def random_move(position, game):
    "Returns a random vector representing a move to an empty space from position"
    moves = possible_moves(position, game)
    if moves:
        return choice(moves)

def distance(p0, p1):
    """Returns the 'manhattan distance' from one position to another
    The 'manhattan distance' describes the distance from one point to another
    on a city grid, where you can only go horizontally and vertically, not
    diagonally.
    """
    x0, y0 = p0
    x1, y1 = p1
    return abs(x1 - x0) + abs(y1 - y0)

def move_toward_player(position, game):
    "Returns a move which will come closest to the player"
    player_position = game.get_agent_by_name("player").position
    moves = possible_moves(position, game)
    moves_with_distance = []
    for vector in moves:
        x, y = position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        distance_to_player = distance(new_position, player_position)
        moves_with_distance.append((distance_to_player, vector))
    if moves_with_distance:
        shortest_distance, best_move = sorted(moves_with_distance)[0]
        return best_move

def move_to_player(position, game):
    player_position = game.get_agent_by_name("player").position
    for vector in direction_vectors:
        x, y = position
        dx, dy = vector
        new_position = (x + dx, y + dy)
        if new_position == player_position:
            return vector


