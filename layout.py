from random import randint

def board_edges(board_size):
    """Returns a list of positions for the edges of the board.
    """
    x, y = board_size
    positions = []
    top = [(i, 0) for i in range(x)]
    bottom = [(i, y-1) for i in range(x)]
    left = [(0, j) for j in range(1, y-1)]
    right = [(x-1, j) for j in range(1, y-1)]
    return top + bottom + left + right

def inner_board(board_size):
    """Returns a list of positions not on the edges.
    """
    x, y = board_size
    positions = []
    for i in range(1, x-1):
        for j in range(1, y-1):
            positions.append((i, j))
    return positions

def random_empty_position(game):
    """Returns a random empty position.
    """
    agents_by_position = game.get_agents_by_position()
    while True:
        x, y = game.board_size
        i = randint(0, x-1)
        j = randint(0, y-1)
        if not agents_by_position[(i, j)]:
            return (i, j)
