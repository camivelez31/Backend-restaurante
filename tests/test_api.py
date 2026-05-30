from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_docs_disponible():
    response = client.get("/docs")
    assert response.status_code == 200


def test_login_exitoso():
    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "Admin123*"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_clientes_sin_token_no_autorizado():
    response = client.get("/clientes/")
    assert response.status_code == 401


def test_clientes_con_token():
    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "Admin123*"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/clientes/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_pedidos_con_token():
    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "Admin123*"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/pedidos/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200