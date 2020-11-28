from connect4 import config
from connect4 import models
from typing import List, Optional
import psycopg2 # type: ignore
import sys
import time


def get_connection():
    return psycopg2.connect(
        user=config.DATABASE_USERNAME,
        password=config.DATABASE_PASSWORD,
        host=config.DATABASE_HOST,
        port=config.DATABASE_PORT,
        dbname=config.DATABASE_NAME,
    )


def initialize():
    for _ in range(0, 30):
        connection = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                """
            CREATE TABLE IF NOT EXISTS game
            (
                id           CHAR(32) PRIMARY KEY,
                active       BOOL NOT NULL,
                winner       INT,
                activePlayer INT NOT NULL,
                board        CHAR(42) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS player
            (
                id           CHAR(32) PRIMARY KEY,
                gameId       CHAR(32),
                number       INT,

                FOREIGN KEY (gameId) REFERENCES game(id),
                UNIQUE (gameId, number)
            );
            """
            )
            connection.commit()
            return
        except (Exception, psycopg2.Error) as error:
            print("Error: could not connect to the database.", error)
        finally:
            if connection is not None:
                cursor.close()
                connection.close()

        time.sleep(1)

    print("Error: failed to initialize database.")
    sys.exit(1)


# SQL injectable code that you will fix in week 2.


def create_game(
    gameId: str, active: bool, winner: Optional[int], activePlayer: int, board: str
) -> None:
    connection = None
    try:
        winner_str = "NULL"
        if winner is not None:
            winner_str = str(int(winner))
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        INSERT INTO game
                    (id,
                    active,
                    winner,
                    activePlayer,
                    board)
        VALUES      ('{gameId}',
                    {str(active).lower()},
                    {winner_str},
                    {activePlayer},
                    '{board}');
        """
        )
        connection.commit()
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def add_player_to_game(playerId: str, gameId: str, number: int) -> None:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        INSERT INTO Player
                    (id,
                    gameId,
                    number)
        VALUES      ('{playerId}',
                    '{gameId}',
                    {number});
        """
        )
        connection.commit()
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def get_game(gameId: str) -> Optional[models.GameEntity]:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT id, active, winner, activePlayer, board
        FROM Game
        WHERE id = '{gameId}';
        """
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return models.GameEntity(
            gameId=row[0],
            active=row[1],
            winner=row[2],
            activePlayer=row[3],
            board=row[4],
        )
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def get_players(gameId: str) -> List[models.PlayerEntity]:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT id, gameId, number
        FROM Player
        WHERE gameId = '{gameId}';
        """
        )

        rows = cursor.fetchall()

        players = []
        for row in rows:
            player = models.PlayerEntity(playerId=row[0], gameId=row[1], number=row[2])
            players.append(player)

        return players
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def get_player(gameId: str, playerId: str) -> Optional[models.PlayerEntity]:
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT id, gameId, number
        FROM Player
        WHERE id = '{playerId}' AND gameId = '{gameId}';
        """
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return models.PlayerEntity(playerId=row[0], gameId=row[1], number=row[2])
    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def update_game(
    gameId: str, active: bool, winner: Optional[int], activePlayer: int, board: str
) -> None:
    connection = None
    try:
        winner_str = "NULL"
        if winner is not None:
            winner_str = str(int(winner))
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"""
        UPDATE Game
        SET active = {str(active).lower()},
            winner = {winner_str},
            activePlayer = {activePlayer},
            board = '{board}'
        WHERE id = '{gameId}';
        """
        )
        connection.commit()
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
