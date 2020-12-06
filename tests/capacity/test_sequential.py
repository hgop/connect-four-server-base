from tests.acceptance.test_game import test_game
from tests.capacity import config
from typing import List
import requests
import pytest

@pytest.mark.timeout(30)
def test_sequential():
    for _ in range(10):
        test_game()
