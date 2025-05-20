import pytest
from fastapi.testclient import TestClient
from server.main import app, client as openai_client

class DummyResponse:
    def __init__(self, content):
        self.choices = [type('Choice', (), {'message': type('Msg', (), {'content': content})})()]

def test_generate(monkeypatch):
    test_client = TestClient(app)

    async def fake_create(**kwargs):
        return DummyResponse("// swift code")

    monkeypatch.setattr(openai_client.chat.completions, 'create', fake_create)

    response = test_client.post('/generate', json={'message': 'hi'})
    assert response.status_code == 200
    assert 'code' in response.json()
