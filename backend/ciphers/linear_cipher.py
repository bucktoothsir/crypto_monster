"""
Linear cipher.
"""

import argparse
import math
from utils import count_letter_percentage, get_possible_linear_keys
from utils import IDX_TO_CHAR, CHAR_TO_IDX, LENGTH_OF_ALPHABET, ALPHABET


def linear_encode(plaintext: str, a: int, b: int) -> str:
    if(math.gcd(26, a) != 1):
        raise ValueError("Bad Key.")
    ciphertext = ''
    for c in plaintext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                upper = 1
                c = c.lower()
            c = IDX_TO_CHAR[(a * CHAR_TO_IDX[c] + b) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
        ciphertext += c
    return ciphertext


def linear_decode_with_key(ciphertext: str, a: int, b: int) -> str:
    if(math.gcd(26, a) != 1):
        raise ValueError("Bad Key.")
    inv = pow(a, -1, 26)
    plaintext = ''
    for c in ciphertext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                upper = 1
                c = c.lower()
            c = IDX_TO_CHAR[inv * (CHAR_TO_IDX[c] - b) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
        plaintext += c
    return plaintext


def linear_decode(ciphertext: str, a: int = None, b: int = None) -> str:
    if a and b:
        plaintext = linear_decode_with_key(ciphertext, a, b)
        return [plaintext]
    else:
        letter_and_per_sorted = count_letter_percentage(ciphertext)
        a, b = get_possible_linear_keys(letter_and_per_sorted, 1)[0]
        plaintext = linear_decode_with_key(ciphertext, a, b)
        return [plaintext, a, b]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--plaintext', type=str, default='', help='Plaintext')
    parser.add_argument('-c', '--ciphertext', type=str, default='', help='Ciphertext')
    parser.add_argument('-a', type=int, default=None, help='linear cypher: c=a*p+b mod 26')
    parser.add_argument('-b',  type=int, default=None, help='linear cypher: c=a*p+b mod 26')
    args = parser.parse_args()
    if args.plaintext:
        if args.a and args.b:
            print("The plaintext is: \"{}\".".format(args.plaintext))
            print("a is: {} b is: {}.".format(args.a, args.b))
            ciphertext = linear_encode(args.plaintext, args.a, args.b)
            print("The ciphertext is : \"{}\".".format(ciphertext))
    if args.ciphertext:
        if args.a and args.b:
            print("The ciphertext is: \"{}\".".format(args.ciphertext))
            print("a is: {} b is: {}.".format(args.a, args.b))
            plaintext = linear_decode(args.ciphertext, args.a, args.b)
            print("The plaintext is : \"{}\".".format(plaintext))
