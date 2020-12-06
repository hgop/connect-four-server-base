from connect4 import models
from typing import List

def get_empty_board() -> List[List[models.Tile]]:
    return [
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY],
        [models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY, models.Tile.EMPTY]
    ]

def get_initial_game_state() -> models.Game:
    return models.Game(
        gameId = "",
        active = True,
        winner = None,
        activePlayer = models.Player.ONE,
        board = get_empty_board()
    )