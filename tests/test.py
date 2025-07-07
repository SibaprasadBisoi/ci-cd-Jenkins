from app import app
def test_index():
    client = app.test_client()
    respone = client.get('/')
    assert respone.statu_code == 200