import os
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "test-key"

from server.main import app


def test_generate_endpoint():
    client = TestClient(app)
    fake_response = MagicMock()
    fake_response.choices = [MagicMock(message=MagicMock(content="fake code"))]
    with patch("server.main.openai.ChatCompletion.create", return_value=fake_response):
        resp = client.post("/generate", json={"message": "Hello"})
        assert resp.status_code == 200
        assert resp.json()["code"] == "fake code"

