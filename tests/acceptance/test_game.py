from connect4 import models
from tests.acceptance import config, helper
from typing import List
import requests

def test_game():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)

    assert state.active == False
    assert state.winner == models.Player.ONE
