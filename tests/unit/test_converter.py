from connect4 import converter
from connect4 import models
from tests.unit import helper
from typing import List

# converter.optional_int_to_player
def test_optional_int_to_player_none():
    assert None == converter.optional_int_to_player(None)

def test_optional_int_to_player_1():
    assert models.Player.ONE == converter.optional_int_to_player(1)

def test_optional_int_to_player_2():
    assert models.Player.TWO == converter.optional_int_to_player(2)

# converter.optional_player_to_int
def test_optional_player_to_int_none():
    assert None == converter.optional_player_to_int(None)

def test_optional_player_to_int_one():
    assert 1 == converter.optional_player_to_int(models.Player.ONE)

def test_optional_player_to_int_two():
    assert 2 == converter.optional_player_to_int(models.Player.TWO)

# converter.int_to_player
def test_int_to_player_1():
    assert models.Player.ONE == converter.int_to_player(1)

def test_int_to_player_2():
    assert models.Player.TWO == converter.int_to_player(2)

# converter.player_to_int
def test_player_to_int_one():
    assert 1 == converter.player_to_int(models.Player.ONE)

def test_player_to_int_two():
    assert 2 == converter.player_to_int(models.Player.TWO)

# TODO converter.int_to_tile
# TODO converter.player_to_tile
# TODO converter.tile_to_int

# converter.str_to_board
def test_str_to_board_empty():
    board_str = (
        "000000"
      + "000000"
      + "000000"
      + "000000"
      + "000000"
      + "000000"
      + "000000"
    )
    board = helper.get_empty_board()
    assert board == converter.str_to_board(board_str)

def test_str_to_board_one_chip():
    board_str = (
        "000000"
      + "100000"
      + "000000"
      + "000000"
      + "000000"
      + "000000"
      + "000000"
    )
    board = helper.get_empty_board()
    board[1][0] = models.Tile.ONE
    assert board == converter.str_to_board(board_str)
