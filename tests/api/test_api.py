import pytest
from fastapi import status
from fastapi.testclient import TestClient

from python_template.main import app


@pytest.fixture
def client():
    """
    Create a test client using the FastAPI app
    """
    return TestClient(app)


# Test the root endpoint
def test_root(client):
    """
    Test the root endpoint
    """
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK


def test_health(client):
    """
    Test the health endpoint
    """
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
