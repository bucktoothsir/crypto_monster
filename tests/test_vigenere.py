import pytest
from backend.ciphers.vigenere_cipher import vigenere_encode, vigenere_decode


PLAINTEXT = "As temperatures drop and daylight hours decrease, it's not unusual for people to express dread about the dark days ahead. Many of us also continue to work from home and spend much of our time indoors. Without the change of environment and personal interactions that workplaces can provide, it's even more difficult to escape the winter blues. For many, though, this time of year marks the onset of a more serious condition. Seasonal affective disorder, or SAD, is a type of depression that usually gets worse during the fall and winter."
CIPHERTEXT = "Cj rtfxmtrrjkma fime tvl frwabopv ymjka lgtpttam, kk'q chb cplqjtt nqi nthxtg km tqxzgjq skmif rzdnb bjv bpks lcpq pamif. Dycr wn wj yalw kqerxgcm vf udks ntfk whum ceb himvf dsra wn qlp ibum kebdhza. Yzrwhcb vyc raiviv mu xvdkimcfmvv rls imzuflpe qvvvppvbqqeq iaib yfpzitievq rtv xtftxwm, qv'j ckxv uqic sbnnktsam bw gjapim bjv uxgbmt sjjxa. Nqi kpgg, bjfsva, bpkj rxfm wh pcpk uitbq iam wpjci hn i ofpt lmzkfsh vwvfzrxhv. Agrqdgit cwdtvbqxv bxlwzfvp, dk AIF, zq p mgxg fd sxxzgjqxhv bjrr jlcincw vxba yfphx lctzlv mpm hrja tvl yzlixz."
KEY = "cryptii"


@pytest.mark.parametrize('plaintext', [PLAINTEXT])
@pytest.mark.parametrize('key', [KEY])
def test_vigenere_encode(plaintext: str, key: int) -> None:
    ciphertext = vigenere_encode(plaintext, key)
    assert ciphertext == CIPHERTEXT


@pytest.mark.parametrize('ciphertext', [CIPHERTEXT])
@pytest.mark.parametrize('key', [KEY])
def test_vigenere_decode_with_key(ciphertext: str, key: int) -> None:
    res = vigenere_decode(ciphertext, key=key)
    plaintext = res[0]
    assert plaintext == PLAINTEXT


@pytest.mark.parametrize('ciphertext', [CIPHERTEXT])
@pytest.mark.parametrize('keylen', [len(KEY)])
def test_vigenere_decode_with_key_len(ciphertext: str, keylen: int) -> None:
    res = vigenere_decode(ciphertext, keylen=keylen)
    plaintext, possible_key = res[0], res[1]
    assert plaintext == PLAINTEXT and possible_key == KEY


@pytest.mark.parametrize('ciphertext', [CIPHERTEXT])
def test_vigenere_decode_with_cipher(ciphertext: str) -> None:
    res = vigenere_decode(ciphertext)
    plaintext, possible_key = res[0], res[1]
    assert plaintext == PLAINTEXT and possible_key == KEY