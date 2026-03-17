import os

import requests


def test_health_endpoint() -> None:
    base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000")
    response = requests.get(f"{base_url}/health", timeout=5)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
