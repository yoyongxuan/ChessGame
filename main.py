
from chess import Board
import curses
# def testGame():
#     import os
#     os.system('python3 -m unittest -v test_chess.TestCoreReqs')
#     os.system('python3 -m unittest -v test_chess.TestBonusReqs')
# testGame()

from Interfaces import ConsoleInterface, TextInterface

ui = TextInterface()
game = Board(inputf=ui.get_player_input,
             printf=ui.set_msg,
             set_board=ui.set_board
             )

game.start()
while game.winner is None:
    game.display()
    start, end = game.prompt()
    game.update(start, end)
    game.next_turn()
game.printf(f'Game over. {game.winner} player wins!')
