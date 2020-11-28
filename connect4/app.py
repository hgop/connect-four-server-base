from connect4 import app_logic
from connect4 import config
from connect4 import database
from connect4 import exceptions
from flask import Flask, request
from flask_cors import CORS # type: ignore
from typing import Any, Callable, Tuple

database.initialize()

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

def call_wrapper(action: Callable[[], Tuple[Any, int]]) -> Tuple[Any, int]:
    try:
        return action()
    except exceptions.ApiException as ex:
        return {
            "error": ex.message,
        }, ex.status_code
    except Exception:
        return {
            "error": "Internal Server Error",
        }, 500


@app.route("/", methods=["GET"])
def index() -> Tuple[str, int]:
    return call_wrapper(
        lambda: app_logic.index()
    )


@app.route("/status", methods=["GET"])
def status() -> Tuple[str, int]:
    return call_wrapper(
        lambda: app_logic.status()
    )


@app.route("/create_game", methods=["POST"])
def create_game() -> Tuple[dict, int]:
    return call_wrapper(
        lambda: app_logic.create_game(request.json)
    )

@app.route("/join_game", methods=["POST"])
def join_game() -> Tuple[dict, int]:
    return call_wrapper(
        lambda: app_logic.join_game(request.json)
    )

@app.route("/get_game", methods=["GET"])
def get_game() -> Tuple[dict, int]:
    gameId = request.args.get("gameId", "")
    playerId = request.args.get("playerId", "")
    return call_wrapper(
        lambda: app_logic.get_game(gameId, playerId)
    )


@app.route("/make_move", methods=["POST"])
def make_move() -> Tuple[dict, int]:
    return call_wrapper(
        lambda: app_logic.make_move(request.json)
    )


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
