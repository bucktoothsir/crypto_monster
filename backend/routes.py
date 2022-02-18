"""
App routes.
"""

import json
from flask import request

from ciphers.caesar_cipher import caesar_encode, caesar_decode
from ciphers.linear_cipher import linear_decode, linear_encode
from ciphers.vigenere_cipher import vigenere_encode, vigenere_decode


def configure_routes(app):
    @app.route('/')
    def index():
        return 'Hello World'

    @app.route('/cipher/linear/<mode>', methods=['POST'])
    def linear(mode):
        data = request.data.decode('utf-8')
        dic = json.loads(data)
        if(mode == 'encode'):
            try:
                cipher = linear_encode(dic['plaintext'], dic['a'], dic['b'])
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            ret = {'status': 'ok', 'ciphertext': cipher}
        else:
            try:
                plain = linear_decode(dic['ciphertext'], dic.get('a'), dic.get('b'))
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            if(len(plain) == 1):
                ret = {"status": "ok", "plaintext": plain[0]}
            else:
                ret = {"status": "ok", "plaintext": plain[0], "a": plain[1], "b": plain[2]}
        return json.dumps(ret)

    @app.route('/cipher/caesar/<mode>', methods=['POST'])
    def caesar(mode):
        data = request.data.decode('utf-8')
        dic = json.loads(data)
        if(mode == 'encode'):
            try:
                print('type of key')
                print(type(dic['key']))
                cipher = caesar_encode(dic['plaintext'], dic['key'])
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            ret = {'status': 'ok', 'ciphertext': cipher}
        else:
            try:
                plain = caesar_decode(dic['ciphertext'], dic.get('key'))
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            if(len(plain) == 1):
                ret = {'status': 'ok', 'plaintext': plain[0]}
            else:
                ret = {'status': 'ok', 'plaintext': plain[0], 'key': plain[1]}
        return json.dumps(ret)

    @app.route('/cipher/vigenere/<mode>', methods=['POST'])
    def vigenere(mode):
        data = request.data.decode('utf-8')
        dic = json.loads(data)
        if(mode == 'encode'):
            try:
                cipher = vigenere_encode(dic['plaintext'], dic['key'])
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            ret = {'status': 'ok', 'ciphertext': cipher}
        else:
            try:
                plain = vigenere_decode(
                    dic['ciphertext'], dic.get('key'), dic.get('keylen'))
            except Exception as e:
                print(e)
                ret = {'status': 'failed'}
                return json.dumps(ret)
            if(len(plain) == 1):
                ret = {'status': 'ok', 'plaintext': plain[0]}
            else:
                ret = {'status': 'ok', 'plaintext': plain[0], 'key': plain[1]}
        return json.dumps(ret)
