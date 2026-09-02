import json

from app import app


def test_root_page_serves_html():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert b'Life Insurance Application' in response.data


def test_submit_route_saves_json():
    client = app.test_client()
    payload = {
        'fullName': 'Test User',
        'dateOfBirth': '1990-01-01',
        'address': '123 Main St',
        'gender': 'male',
        'occupation': 'Engineer',
        'income': '50000',
        'maritalStatus': 'single',
        'dependants': '0'
    }

    response = client.post('/submit', json=payload)
    body = json.loads(response.data)

    assert response.status_code == 200
    assert body['status'] == 'success'
    assert 'filename' in body
