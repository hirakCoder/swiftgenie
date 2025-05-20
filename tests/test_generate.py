import pytest
from fastapi.testclient import TestClient
from server.main import app, client

class DummyResponse:
    def __init__(self, content):
        self.choices = [type('obj', (), {'message': type('msg', (), {'content': content})})]

@pytest.fixture(autouse=True)
def patch_openai(monkeypatch):
    async def fake_create(**kwargs):
        return DummyResponse("// swift code")
    monkeypatch.setattr(client.chat.completions, "create", fake_create)


def test_generate_endpoint():
    with TestClient(app) as test_client:
        resp = test_client.post("/generate", json={"message": "hello"})
        assert resp.status_code == 200
        assert "code" in resp.json()
