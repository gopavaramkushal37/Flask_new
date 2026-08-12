from app import app

def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello World!"

def test_about():
    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200
    assert response.data == b"About Page"

def test_contact():
    client = app.test_client()

    response = client.get("/contact")

    assert response.status_code == 200
    assert response.data == b"Contact Page"