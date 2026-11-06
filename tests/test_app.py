from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_version():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json) == 3


def test_not_found():
    client = app.test_client()
    response = client.get("/inconnue")
    assert response.status_code == 404