from app.core.config import settings
from fastapi import status
from fastapi.testclient import TestClient


def test_status(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1}/status/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Alive!"}
