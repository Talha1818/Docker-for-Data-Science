from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World from Muhammad Talha" in response.data
