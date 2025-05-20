import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from server.main import app, client

client_app = TestClient(app)

@pytest.mark.asyncio
async def test_generate_endpoint():
    mock_resp = AsyncMock()
    mock_resp.choices = [type('obj', (object,), {'message': type('m', (object,), {'content': 'swift code'})()})]

    async def fake_create(*args, **kwargs):
        return mock_resp

    with patch.object(client.chat.completions, 'create', new=AsyncMock(side_effect=fake_create)):
        response = client_app.post('/generate', json={'message': 'hello'})
        assert response.status_code == 200
        assert response.json() == {'code': 'swift code'}
