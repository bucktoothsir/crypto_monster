import os
import json
from flask import Flask, request
from caesar_cipher import caesar_encode,  caesar_decode
from linear_cipher import linear_decode, linear_encode
from vigenere_cipher import vigenere_encode, vigenere_decode

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = 1000


@app.route('/cipher/linear/<mode>', methods=['POST'])
def linear(mode):
    data = request.data.decode("utf-8")
    dic = json.loads(data)
    if(mode == 'encode'):
        try:
            cipher = linear_encode(dic['plaintext'], dic['a'], dic['b'])
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        ret = {"status": "ok", "ciphertext": cipher}
    else:
        try:
            plain = linear_decode(dic['ciphertext'], dic['a'], dic['b'])
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        ret = {"status": "ok", "plaintext": plain}
    return json.dumps(ret)


@app.route('/cipher/caesar/<mode>', methods=['POST'])
def caesar(mode):
    data = request.data.decode("utf-8")
    dic = json.loads(data)
    if(mode == 'encode'):
        try:
            cipher = caesar_encode(dic['plaintext'], dic['key'])
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        ret = {"status": "ok", "ciphertext": cipher}
    else:
        try:
            plain = caesar_decode(dic['ciphertext'], dic.get('key'))
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        if(len(plain) == 1):
            ret = {"status": "ok", "plaintext": plain[0]}
        else:
            ret = {"status": "ok", "plaintext": plain[0], "key": plain[1]}
    return json.dumps(ret)


@app.route('/cipher/vigenere/<mode>', methods=['POST'])
def vigenere(mode):
    data = request.data.decode("utf-8")
    dic = json.loads(data)
    if(mode == 'encode'):
        try:
            cipher = vigenere_encode(dic['plaintext'], dic['key'])
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        ret = {"status": "ok", "ciphertext": cipher}
    else:
        try:
            plain = vigenere_decode(dic['ciphertext'], dic.get('key'), dic.get('keylen'))
        except Exception as e:
            print(e)
            ret = {"status": "failed"}
            return json.dumps(ret)
        if(len(plain) == 1):
            ret = {"status": "ok", "plaintext": plain[0]}
        else:
            ret = {"status": "ok", "plaintext": plain[0], "key": plain[1]}
    return json.dumps(ret)


if __name__ == '__main__':
    app.run()
