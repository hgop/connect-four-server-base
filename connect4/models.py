from enum import IntEnum
from typing import Any, Dict, List, Optional

# Models


class Player(IntEnum):
    ONE = 1
    TWO = 2


class Tile(IntEnum):
    EMPTY = 0
    ONE = Player.ONE
    TWO = Player.TWO


class Game:
    gameId: str
    active: bool
    winner: Optional[Player]
    activePlayer: Player
    board: List[List[Tile]]

    def __init__(
        self,
        gameId: str,
        active: bool,
        winner: Optional[Player],
        activePlayer: Player,
        board: List[List[Tile]],
    ) -> None:
        self.gameId = gameId
        self.active = active
        self.winner = winner
        self.activePlayer = activePlayer
        self.board = board


# Requests & Responses


class BaseGameResponse:
    gameId: str
    active: bool
    playerId: str
    winner: Optional[Player]
    playerNumber: Player
    activePlayer: Player
    playerCount: int
    board: List[List[Tile]]

    def __init__(
        self,
        gameId: str,
        active: bool,
        playerId: str,
        winner: Optional[Player],
        playerNumber: Player,
        activePlayer: Player,
        playerCount: int,
        board: List[List[Tile]],
    ) -> None:
        self.gameId = gameId
        self.active = active
        self.playerId = playerId
        self.winner = winner
        self.playerNumber = playerNumber
        self.activePlayer = activePlayer
        self.playerCount = playerCount
        self.board = board

    def to_json(self) -> dict:
        return self.__dict__


class CreateGameRequest:
    def __init__(self, json: dict) -> None:
        pass


class CreateGameResponse(BaseGameResponse):
    pass


class JoinGameRequest:
    gameId: str

    def __init__(self, json: dict) -> None:
        self.gameId = json["gameId"]


class JoinGameResponse(BaseGameResponse):
    pass


class GetGameRequest:
    gameId: str
    playerId: str

    def __init__(self, json: dict) -> None:
        self.gameId = json["gameId"]
        self.playerId = json["playerId"]


class GetGameResponse(BaseGameResponse):
    pass


class MakeMoveRequest:
    gameId: str
    playerId: str
    column: int

    def __init__(self, json: dict) -> None:
        self.gameId = json["gameId"]
        self.playerId = json["playerId"]
        self.column = json["column"]


class MakeMoveResponse(BaseGameResponse):
    pass


# Database Entities


class GameEntity:
    gameId: str
    active: bool
    winner: Optional[int]
    activePlayer: int
    board: str

    def __init__(
        self,
        gameId: str,
        active: bool,
        winner: Optional[int],
        activePlayer: int,
        board: str,
    ) -> None:
        self.gameId = gameId
        self.active = active
        self.winner = winner
        self.activePlayer = activePlayer
        self.board = board


class PlayerEntity:
    playerId: str
    gameId: str
    number: int

    def __init__(self, playerId: str, gameId: str, number: int) -> None:
        self.playerId = playerId
        self.gameId = gameId
        self.number = number
