import runpy


def test_integration():
    namespace = runpy.run_path("app/app.py")
    app = namespace["app"]  
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200