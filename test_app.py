from app import login

def test_login():
    assert login("admin","wrong") == False
