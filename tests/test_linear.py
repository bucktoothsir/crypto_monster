import string
import random
import math
from backend.ciphers.linear_cipher import linear_encode, linear_decode


def test_linear():
    num_tests = 1000
    letters = string.ascii_letters
    a_param = [x for x in range(1,26) if(math.gcd(x, 26) == 1)]
    for i in range(num_tests):
        str_len = random.randint(1, 15)
        test_str = ''.join(random.choice(letters) for i in range(str_len))
        test_a = random.choice(a_param)
        test_b = random.randint(0, 25)
        assert test_str == linear_decode(linear_encode(test_str, test_a, test_b), test_a, test_b)[0]
