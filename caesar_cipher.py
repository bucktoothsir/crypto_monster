"""
Caesar cipher.
"""

import argparse
from utils import count_letter_percentage, get_possible_single_keys
from utils import IDX_TO_CHAR, CHAR_TO_IDX, LENGTH_OF_ALPHABET, ALPHABET


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--plaintext', type=str, default='', help='Plaintext')
    parser.add_argument('-pf', '--plaintext_file', type=str, default='', help='Plaintext File')
    parser.add_argument('-c', '--ciphertext', type=str, default='', help='Caesar Cipher')
    parser.add_argument('-cf', '--ciphertext_file', type=str, default='', help='Caesar Cipher File')
    parser.add_argument('-k', '--key', type=int, default=None, help='key to decode the cipher')
    args = parser.parse_args()
    if args.plaintext or args.plaintext_file:
        if args.plaintext:
            plaintext = args.plaintext
        if args.plaintext_file:
            with open(args.plaintext_file) as f:
                plaintext = f.read()
        if args.key:
            print('The plaintext is:\n%s' % plaintext)
            print('The key is:\n%d' % args.key)
            ciphertext = caesar_encode(plaintext, args.key)
            print('The ciphertext is:\n%s' % ciphertext)
    if args.ciphertext or args.ciphertext_file:
        if args.ciphertext:
            ciphertext = args.ciphertext
        if args.ciphertext_file:
            with open(args.ciphertext_file) as f:
                ciphertext = f.read()
        print('The ciphertext is:\n%s' % ciphertext)
        key = None
        if args.key:
            key = args.key
            print('The key is:\n%s' % args.key)
        res = caesar_decode(ciphertext, key)
        if len(res) > 1:
            plaintext, possible_key = res[0], res[1]
            print('The possible key is\n%d' % possible_key)
        else:
            plaintext = res[0]
        print('The plaintext is:\n%s' % plaintext)
