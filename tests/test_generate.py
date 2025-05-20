from fastapi.testclient import TestClient
from server.main import app, client
from types import SimpleNamespace
from unittest.mock import AsyncMock


def test_generate_endpoint(monkeypatch):
    dummy_resp = SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="Hello"))])
    monkeypatch.setattr(client.chat.completions, "create", AsyncMock(return_value=dummy_resp))

    with TestClient(app) as test_client:
        response = test_client.post("/generate", json={"message": "hi"})

    assert response.status_code == 200
    assert response.json() == {"code": "Hello"}
