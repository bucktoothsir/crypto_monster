"""
Caesar cipher encoder and decoder.
"""

from .utils import count_letter_percentage, get_possible_single_keys
from .utils import IDX_TO_CHAR, CHAR_TO_IDX, LENGTH_OF_ALPHABET, ALPHABET


def caesar_encode(plaintext: str, key: int) -> str:
    key %= LENGTH_OF_ALPHABET
    ciphertext = ''
    for c in plaintext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                upper = 1
                c = c.lower()
            c = IDX_TO_CHAR[(CHAR_TO_IDX[c] + key) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
            ciphertext += c
        else:
            ciphertext += c
    return ciphertext


def caesar_decode_with_key(ciphertext: str, key: int) -> str:
    key %= LENGTH_OF_ALPHABET
    plaintext = ''
    for c in ciphertext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                c = c.lower()
                upper = 1
            c = IDX_TO_CHAR[(CHAR_TO_IDX[c] - key) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
        plaintext += c
    return plaintext


def caesar_decode(ciphertext: str, key: int = None) -> str:
    if key:
        plaintext = caesar_decode_with_key(ciphertext, key)
        return [plaintext]
    else:
        letter_and_per_sorted = count_letter_percentage(ciphertext)
        possible_key = get_possible_single_keys(letter_and_per_sorted, 1)[0]
        plaintext = caesar_decode_with_key(ciphertext, possible_key)
        return [plaintext, possible_key]
