from connect4 import game_logic
from connect4 import models
from tests.unit import helper
from typing import List

# game_logic.make_move
def test_make_move_returns_new_object():
    game_input = helper.get_initial_game_state()

    game_output = game_logic.make_move(game_input, 0)

    assert game_input != game_output

def test_make_move_set_tile_one():
    game_input = helper.get_initial_game_state()

    game_output = game_logic.make_move(game_input, 0)

    assert models.Tile.ONE == game_output.board[0][0]

def test_make_move_set_tile_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = models.Player.TWO

    game_output = game_logic.make_move(game_input, 0)

    assert models.Tile.TWO == game_output.board[0][0]

def test_make_move_horizontal_win_one():
    game_input = helper.get_initial_game_state()
    game_input.board[0][0] = models.Tile.ONE
    game_input.board[1][0] = models.Tile.ONE
    game_input.board[2][0] = models.Tile.ONE
    
    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert models.Player.ONE == game_output.winner

def test_make_move_horizontal_win_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = models.Player.TWO
    game_input.board[0][0] = models.Tile.TWO
    game_input.board[1][0] = models.Tile.TWO
    game_input.board[2][0] = models.Tile.TWO
    
    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert models.Player.TWO == game_output.winner

def test_make_move_vertical_win_one():
    game_input = helper.get_initial_game_state()
    game_input.board[0][0] = models.Tile.ONE
    game_input.board[0][1] = models.Tile.ONE
    game_input.board[0][2] = models.Tile.ONE
    
    game_output = game_logic.make_move(game_input, 0)

    assert False == game_output.active
    assert models.Player.ONE == game_output.winner

def test_make_move_vertical_win_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = models.Player.TWO
    game_input.board[0][0] = models.Tile.TWO
    game_input.board[0][1] = models.Tile.TWO
    game_input.board[0][2] = models.Tile.TWO
    
    game_output = game_logic.make_move(game_input, 0)

    assert False == game_output.active
    assert models.Player.TWO == game_output.winner

# TODO test diagonal wins

# game_logic.is_column_full
def test_is_column_full_empty():
    game_input = helper.get_initial_game_state()

    is_column_full = game_logic.is_column_full(game_input, 0)

    assert False == is_column_full

def test_is_column_full_full():
    game_input = helper.get_initial_game_state()
    for y in range(6):
        game_input.board[0][y] = models.Tile.ONE

    is_column_full = game_logic.is_column_full(game_input, 0)

    assert True == is_column_full