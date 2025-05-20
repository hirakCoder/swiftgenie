import pytest
from fastapi.testclient import TestClient

from server.main import app, client

@pytest.fixture(autouse=True)
def override_openai(monkeypatch):
    async def fake_create(*args, **kwargs):
        class Choice:
            message = type("obj", (), {"content": "// swift code"})()
        return type("obj", (), {"choices": [Choice()]})()

    monkeypatch.setattr(client.chat.completions, "create", fake_create)


def test_generate_endpoint():
    test_client = TestClient(app)
    response = test_client.post("/generate", json={"message": "test"})
    assert response.status_code == 200
    assert response.json() == {"code": "// swift code"}
