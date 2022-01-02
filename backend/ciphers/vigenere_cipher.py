"""
Vigenere Cipher encoder and decoder.
"""

from .utils import IDX_TO_CHAR, LENGTH_OF_ALPHABET, ALPHABET, CHAR_TO_IDX
from .utils import Friedman, count_letter_percentage, get_possible_single_keys, get_group_of_cipher


def vigenere_encode(plaintext: str, key: str) -> str:
    key_int_list = []
    for c in key:
        if c not in ALPHABET:
            raise ValueError('Key must be all letters.')
        key_int_list.append(CHAR_TO_IDX[c.lower()])
    ciphertext = ''
    idx_of_key = 0
    for c in plaintext:
        if c in ALPHABET:
            upper = 0
            if c.isupper():
                c = c.lower()
                upper = 1
            c = IDX_TO_CHAR[(CHAR_TO_IDX[c] + key_int_list[idx_of_key]) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
            idx_of_key += 1
            idx_of_key %= len(key_int_list)
        ciphertext += c
    return ciphertext


def vigenere_decode(ciphertext: str, key: str = '', keylen: int = None) -> str:
    if key:
        plaintext = vigenere_decode_with_key(ciphertext, key)
        return [plaintext]
    elif keylen:
        plaintext, possbile_key = vigenere_decode_with_keylen(ciphertext, keylen)
        return [plaintext, possbile_key]
    else:
        possbile_keylen = Friedman(ciphertext)[0]
        plaintext, possbile_key = vigenere_decode_with_keylen(ciphertext, possbile_keylen)
        return [plaintext, possbile_key]


def vigenere_decode_with_keylen(ciphertext: str, keylen: int) -> str:
    """
    Decode vigenere code just knowing the length of key.
    Guess the possbile key and decode the cipher.
    Maybe not precise when the cipher is too short.
    """
    possbile_key = ''
    cipher_group = get_group_of_cipher(ciphertext, keylen)
    for g in cipher_group:
        letter_and_per_sorted = count_letter_percentage(g)
        possible_key_int = get_possible_single_keys(letter_and_per_sorted, 1)
        possbile_key += IDX_TO_CHAR[possible_key_int[0]]
    plaintext = vigenere_decode_with_key(ciphertext, possbile_key)
    return plaintext, possbile_key


def vigenere_decode_with_key(ciphertext: str, key: str) -> str:
    key_int_list = []
    for c in key:
        if c not in ALPHABET:
            raise ValueError('Key must be all letters.')
        key_int_list.append(CHAR_TO_IDX[c.lower()])
    plaintext = ''
    idx_of_key = 0
    for c in ciphertext:
        if c in ALPHABET:
            upper = 0
            if c.isupper():
                c = c.lower()
                upper = 1
            c = IDX_TO_CHAR[(CHAR_TO_IDX[c] - key_int_list[idx_of_key]) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
            idx_of_key += 1
            idx_of_key %= len(key_int_list)
        plaintext += c
    return plaintext
