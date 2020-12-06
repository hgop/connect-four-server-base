from tests.acceptance import config
from typing import List
import requests

def test_status():
    response = requests.get(config.API_URL + "/status")
    assert "Running" == response.text
