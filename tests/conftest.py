from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parent.parent
APP_FILE = ROOT / "app" / "app.py"


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="session", autouse=True)
def web_server(base_url: str):
    if os.getenv("USE_EXTERNAL_BASE_URL") == "1":
        yield
        return

    port = _free_port()
    host = f"http://127.0.0.1:{port}"
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["PORT"] = str(port)

    process = subprocess.Popen(
        [sys.executable, str(APP_FILE)],
        cwd=str(ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    deadline = time.time() + 20
    healthy = False
    while time.time() < deadline:
        try:
            response = requests.get(f"{host}/health", timeout=1)
            if response.ok:
                healthy = True
                break
        except Exception:
            time.sleep(0.5)

    if not healthy:
        output = ""
        if process.stdout:
            output = process.stdout.read()
        process.kill()
        raise RuntimeError(f"Flask app did not start. Output:\n{output}")

    os.environ["BASE_URL"] = host
    yield

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url: str):
    resolved_base_url = os.getenv("BASE_URL", base_url)
    return {
        **browser_context_args,
        "base_url": resolved_base_url,
        "ignore_https_errors": True,
        "viewport": {"width": 1440, "height": 900},
    }
