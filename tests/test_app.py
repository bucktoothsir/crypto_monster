"""
App test
"""

import json
import pytest

from backend.app import create_app


PLAINTEXT = 'If he had anything confidential to say.'
CIPHERTEXT = 'Pm ol ohk hufaopun jvumpkluaphs av zhf.'
CAESAR_KEY = 7
LINEAR_A = 1
LINEAR_B = 7
VIGENERE_PLAINTEXT = "As temperatures drop and daylight hours decrease, it's not unusual for people to express dread about the dark days ahead. Many of us also continue to work from home and spend much of our time indoors."\
                     "Without the change of environment and personal interactions that workplaces can provide, it's even more difficult to escape the winter blues. For many, though, this time of year marks the onset of a "\
                     "more serious condition. Seasonal affective disorder, or SAD, is a type of depression that usually gets worse during the fall and winter."
VIGENERE_CIPHERTEXT = "Cj rtfxmtrrjkma fime tvl frwabopv ymjka lgtpttam, kk'q chb cplqjtt nqi nthxtg km tqxzgjq skmif rzdnb bjv bpks lcpq pamif. Dycr wn wj yalw kqerxgcm vf udks ntfk whum ceb himvf dsra wn qlp ibum kebdhza."\
                      "Yzrwhcb vyc raiviv mu xvdkimcfmvv rls imzuflpe qvvvppvbqqeq iaib yfpzitievq rtv xtftxwm, qv'j ckxv uqic sbnnktsam bw gjapim bjv uxgbmt sjjxa. Nqi kpgg, bjfsva, bpkj rxfm wh pcpk uitbq iam wpjci hn i ofpt "\
                      "lmzkfsh vwvfzrxhv. Agrqdgit cwdtvbqxv bxlwzfvp, dk AIF, zq p mgxg fd sxxzgjqxhv bjrr jlcincw vxba yfphx lctzlv mpm hrja tvl yzlixz."
VIGENERE_KEY = "cryptii"
VIGENERE_KEY_LEN = len(VIGENERE_KEY)


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
        'key': CAESAR_KEY
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    assert json.loads(response.get_data())['ciphertext'] == CIPHERTEXT
    assert response.status_code == 200


def test_post_caesar_decode_with_key(client):
    url = '/cipher/caesar/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': CIPHERTEXT,
        'key': CAESAR_KEY
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == PLAINTEXT
    assert response.status_code == 200


def test_post_caesar_decode_without_key(client):
    url = '/cipher/caesar/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': CIPHERTEXT,
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == PLAINTEXT
    assert data['key'] == CAESAR_KEY
    assert response.status_code == 200


def test_post_linear_encode(client):
    url = '/cipher/linear/encode'
    mock_request_data = {
        'request_id': '123',
        'plaintext': PLAINTEXT,
        'a': LINEAR_A,
        'b': LINEAR_B,
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['ciphertext'] == CIPHERTEXT
    assert response.status_code == 200


def test_post_linear_decode_with_key(client):
    url = '/cipher/linear/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': CIPHERTEXT,
        'a': LINEAR_A,
        'b': LINEAR_B
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == PLAINTEXT


def test_post_linear_decode_without_key(client):
    url = '/cipher/linear/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': CIPHERTEXT
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == PLAINTEXT
    assert data['a'] == LINEAR_A
    assert data['b'] == LINEAR_B


def test_post_vigenere_encode(client):
    url = '/cipher/vigenere/encode'
    mock_request_data = {
        'request_id': '123',
        'plaintext': VIGENERE_PLAINTEXT,
        'key': VIGENERE_KEY
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['ciphertext'] == VIGENERE_CIPHERTEXT
    assert response.status_code == 200


def test_post_vigenere_decode_with_key(client):
    url = '/cipher/vigenere/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': VIGENERE_CIPHERTEXT,
        'key': VIGENERE_KEY
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == VIGENERE_PLAINTEXT
    assert response.status_code == 200


def test_post_vigenere_decode_with_key_len(client):
    url = '/cipher/vigenere/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': VIGENERE_CIPHERTEXT,
        'keylen': len(VIGENERE_KEY)
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == VIGENERE_PLAINTEXT
    assert data['key'] == VIGENERE_KEY


def test_post_vigenere_decode_with_plaintext(client):
    url = '/cipher/vigenere/decode'
    mock_request_data = {
        'request_id': '123',
        'ciphertext': VIGENERE_CIPHERTEXT,
    }
    response = client.post(url, data=json.dumps(mock_request_data))
    data = json.loads(response.get_data())
    assert data['plaintext'] == VIGENERE_PLAINTEXT
    assert data['key'] == VIGENERE_KEY
