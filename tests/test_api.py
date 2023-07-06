from backend.app import app
import json

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

def test_get_data():
    response = app.test_client().get('/data')
    res = json.loads(response.data.decode('utf-8')).get("Data")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['id'] == 1
    assert res[1]['id'] == 2
    assert res[0]['dummy_value_1'] == 'Test'
    assert res[1]['dummy_value_1'] == "Definitely not a test"
    assert response.status_code == 200
    assert type(res) is list