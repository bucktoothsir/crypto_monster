"""
Casear test
"""

import pytest

from backend.ciphers.caesar_cipher import caesar_encode, caesar_decode


PLAINTEXT = 'If he had anything confidential to say.'
CIPHERTEXT = 'Pm ol ohk hufaopun jvumpkluaphs av zhf.'
KEY = 7


@pytest.mark.parametrize('plaintext', [PLAINTEXT])
@pytest.mark.parametrize('key', [KEY])
def test_caesar_encode(plaintext: str, key: int) -> None:
    ciphertext = caesar_encode(plaintext, key)
    assert ciphertext == CIPHERTEXT


@pytest.mark.parametrize('ciphertext', [CIPHERTEXT])
@pytest.mark.parametrize('key', [KEY])
def test_caesar_decode_with_key(ciphertext: str, key: int) -> None:
    res = caesar_decode(ciphertext, key)
    plaintext = res[0]
    assert plaintext == PLAINTEXT


@pytest.mark.parametrize('ciphertext', [CIPHERTEXT])
def test_caesar_decode_without_key(ciphertext: str) -> None:
    res = caesar_decode(ciphertext)
    plaintext, possible_key = res[0], res[1]
    assert plaintext == PLAINTEXT and possible_key == KEY
