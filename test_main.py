from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_read_widget():
    response = client.post("/widgets/", json={"name": "Test Widget", "number_of_parts": 5})
    assert response.status_code == 200
    widget = response.json()
    assert widget["name"] == "Test Widget"

    get_response = client.get(f"/widgets/{widget['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == widget["id"]
