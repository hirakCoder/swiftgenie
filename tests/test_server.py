import os
import types
from fastapi.testclient import TestClient

# Ensure API key for import
os.environ.setdefault("OPENAI_API_KEY", "test")

from server.main import app, client

# Patch the OpenAI client to avoid real API calls
async def fake_create(*args, **kwargs):
    class FakeResp:
        choices = [types.SimpleNamespace(message=types.SimpleNamespace(content="print('hello')"))]
    return FakeResp()

client.chat.completions.create = fake_create


def test_generate_endpoint():
    test_client = TestClient(app)
    resp = test_client.post("/generate", json={"message": "test"})
    assert resp.status_code == 200
    data = resp.json()
    assert "code" in data
    assert data["code"].startswith("print")
