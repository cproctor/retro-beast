from retro.game import Game
from random import sample
from player import Player
from beast import Beast
from block import Block, ImmovableBlock
from layout import (
    board_edges, 
    inner_board,
    random_empty_position,
)

board_size = (40, 20)
num_beasts = 10
num_blocks = 200

block_positions = sample(inner_board(board_size), num_blocks)
blocks = [Block(position) for position in block_positions]
edges = [ImmovableBlock(position) for position in board_edges(board_size)]
state = {}

game = Game(blocks + edges, state, board_size)
game.add_agent(Player(random_empty_position(game)))
for b in range(num_beasts):
    game.add_agent(Beast(random_empty_position(game)))
game.play()
