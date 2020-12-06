from connect4 import app_logic, models
from unittest.mock import patch
from tests.unit import helper
from unittest.mock import Mock

def test_index():
    message, code = app_logic.index()
    assert message == "Game Server"
    assert code == 200

def test_status():
    message, code = app_logic.status()
    assert message == "Running"
    assert code == 200

@patch("connect4.database.create_game")
@patch("connect4.database.add_player_to_game")
@patch("connect4.tokens.generate_token")
def test_create_game(mock_generate_token, mock_add_player_to_game, mock_create_game):
    mock_generate_token.side_effect = ["token1", "token2"]
    mock_create_game.return_value = None
    mock_add_player_to_game.return_value = None
    message, code = app_logic.create_game({})
    print(message)
    assert {
        "gameId": "token1", 
        "active": True, 
        "playerId": "token2", 
        "winner": None, 
        "playerNumber": models.Player.ONE, 
        "activePlayer": models.Player.ONE, 
        "playerCount": 1, 
        "board": helper.get_empty_board()
    } == message
    assert code == 201
