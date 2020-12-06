from connect4 import converter
from connect4 import models
from copy import deepcopy


def make_move(game: models.Game, x: int) -> models.Game:
    result = models.Game(
        gameId=game.gameId,
        active=game.active,
        winner=game.winner,
        activePlayer=game.activePlayer,
        board=deepcopy(game.board),
    )

    for y in range(6):
        if result.board[x][y] == models.Tile.EMPTY:
            result.board[x][y] = converter.player_to_tile(result.activePlayer)
            if is_victory_move(result, x, y, result.activePlayer):
                result.winner = result.activePlayer
                result.active = False
            else:
                result.active = is_board_full(result) == False

            if result.activePlayer == models.Player.ONE:
                result.activePlayer = models.Player.TWO
            else:
                result.activePlayer = models.Player.ONE

            return result

    raise Exception("Row is full")


def is_victory_move(game: models.Game, x: int, y: int, player: models.Player) -> bool:
    return (
        is_victory_move_horizontal(game, x, y, player)
        or is_victory_move_vertical(game, x, y, player)
        or is_victory_move_diagonal(game, x, y, player)
    )


def is_victory_move_horizontal(
    game: models.Game, x: int, y: int, player: models.Player
) -> bool:
    connected = 0

    for i in range(-3, 4):
        if get_tile(game, x + i, y) == player:
            connected += 1
        else:
            connected = 0

        if connected >= 4:
            return True

    return False


def is_victory_move_vertical(
    game: models.Game, x: int, y: int, player: models.Player
) -> bool:
    connected = 0

    for i in range(-3, 4):
        if get_tile(game, x, y + i) == player:
            connected += 1
        else:
            connected = 0

        if connected >= 4:
            return True

    return False


def is_victory_move_diagonal(
    game: models.Game, x: int, y: int, player: models.Player
) -> bool:
    connected = 0

    # Diagonal NorthEast
    for i in range(-3, 4):
        if get_tile(game, x + i, y - i) == player:
            connected += 1
        else:
            connected = 0

        if connected >= 4:
            return True

    connected = 0

    # Diagonal SouthEast
    for i in range(-3, 4):
        if get_tile(game, x + i, y + i) == player:
            connected += 1
        else:
            connected = 0

        if connected >= 4:
            return True

    return False


def get_tile(game: models.Game, x: int, y: int) -> models.Tile:
    if x < 0 or 7 <= x:
        return models.Tile.EMPTY
    if y < 0 or 6 <= y:
        return models.Tile.EMPTY
    return game.board[x][y]


def is_board_full(game: models.Game) -> bool:
    for column in game.board:
        for tile in column:
            if tile == models.Tile.EMPTY:
                return False
    return True


def is_column_full(game: models.Game, column: int) -> bool:
    return game.board[column][5] != models.Tile.EMPTY
