from connect4 import models, converter
from tests.acceptance import config
from typing import List
import requests

class InitializedGame:
    gameId: str
    playerOneId: str
    playerTwoId: str

    def __init__(
        self,
        gameId: str,
        playerOneId: str,
        playerTwoId: str
    ) -> None:
        self.gameId = gameId
        self.playerOneId = playerOneId
        self.playerTwoId = playerTwoId

def initialize_game() -> InitializedGame:
    response = requests.post(config.API_URL + "/create_game")
    assert response.status_code == 201

    json = response.json()
    gameId = json["gameId"]
    playerOneId = json["playerId"]

    response = requests.post(config.API_URL + "/join_game", json={
        "gameId": gameId
    })
    assert response.status_code == 202

    json = response.json()
    playerTwoId = json["playerId"]

    return InitializedGame(
        gameId=gameId,
        playerOneId=playerOneId,
        playerTwoId=playerTwoId
    )

def make_move(gameId: str, playerId: str, column: int) -> models.MakeMoveResponse:
    response = requests.post(config.API_URL + "/make_move", json={
        "gameId": gameId,
        "playerId": playerId,
        "column": column
    })
    assert response.status_code == 202

    json = response.json()
    return models.MakeMoveResponse(
        gameId=json["gameId"],
        active=json["active"],
        playerId=json["playerId"],
        winner=converter.optional_int_to_player(json["winner"]),
        playerNumber=converter.int_to_player(json["playerNumber"]),
        activePlayer=converter.int_to_player(json["activePlayer"]),
        playerCount=json["playerCount"],
        board=converter.str_to_board(converter.board_to_str(json["board"])),
    )
