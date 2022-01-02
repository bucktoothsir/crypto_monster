"""
App test
"""

import json
import pytest

from backend.app import create_app

PLAINTEXT = 'If he had anything confidential to say.'
CIPHERTEXT = 'Pm ol ohk hufaopun jvumpkluaphs av zhf.'
KEY = 7


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_post_caesar_encode(client):
    url = '/cipher/caesar/encode'
    mock_request_data = {
        'request_id': '123',
        'plaintext': PLAINTEXT,
        'key': KEY
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    assert json.loads(response.get_data())['ciphertext'] == CIPHERTEXT
    assert response.status_code == 200
