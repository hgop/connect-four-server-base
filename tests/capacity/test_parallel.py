from tests.acceptance.test_game import test_game
from tests.capacity import config
from typing import List
import requests
import pytest
import threading
import time

N = 8
X = 10

class State:
    lock: threading.Lock
    gamesPlayed: int
    failed: bool

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.gamesPlayed = 0
        self.failed = False

    def increment_games_played(self) -> None:
        with self.lock:
            self.gamesPlayed += 1


def play_games(i: int, x: int, state: State) -> None:
    try:
        for j in range(x):
            test_game()
            state.increment_games_played()
            print(f"Thread {i}: finished game number {j}.")
    except:
        state.failed = True

# Test: API_URL=http://connect-four-server-capacity.team-name.hgopteam.com/ pytest -s tests/capacity/
@pytest.mark.timeout(120)
def test_sequential():
    threads = []
    state = State()

    for i in range(N):
        thread = threading.Thread(target=play_games, args=(i, X, state))
        threads.append(thread)

    start_time = time.time()

    for thread in threads:
        thread.start()

    while True:
        all_threads_finished = True
        for thread in threads:
            all_threads_finished = thread.is_alive() == False and all_threads_finished
            
        if all_threads_finished or state.failed:
            break

    print(f"Played: {state.gamesPlayed}")
    print(f"Time: {(time.time() - start_time)}")

    for thread in threads:
        thread.join()

    assert state.failed == False
