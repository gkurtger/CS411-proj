from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import os
import codecs

class Enc_algorithm:
    name = None

    def __init__(self):
        self.keys = dict()
        # user_key type is BYTES
    
    def __repr__(self):
        if self.name == None: return "Generic algorithm"
        else: return self.name
    
    def set_keys(self, key_name: str or list, value: any):
        """Set algorithm parameters"""
        if type(key_name) == str:
            self.keys[key_name] = value
        else:
            for k in range(len(key_name)):
                self.keys[key_name[k]] = value[k]
    
    def _get_cipher_key_from_user_key(self, user_key) -> bytes: ...

    def encrypt(self, token: str, user_key: bytes) -> bytes: ...
    def decrypt(self, token: str, user_key: bytes) -> bytes: ...


class Enc_Null(Enc_algorithm):
    
    name = "Plain-text"

    def encrypt(self, token: str, user_key: bytes) -> bytes:
        return token
        
    def decrypt(self, token: str, user_key: bytes) -> bytes:
        return token

class Enc_Fernet(Enc_algorithm):

    name = "Fernet"

    def _get_cipher_key_from_user_key(self, user_key: bytes) -> bytes:
        """Set user key. This is the user account password"""
        user_key = user_key.decode('utf-8')
        if len(user_key) > 32:
            user_key = user_key[:32]
        elif len(user_key) < 32:
            user_key = (user_key * (int(32/len(user_key)) + 3))[:32]
        return codecs.encode(bytes(user_key, "utf-8"), 'base64')


    def encrypt(self, token: str, user_key) -> bytes:
        algo = Fernet(self._get_cipher_key_from_user_key(user_key))
        return algo.encrypt(bytes(token, 'utf-8'))

    def decrypt(self, token: str, user_key: bytes) -> str:
        algo = Fernet(self._get_cipher_key_from_user_key(user_key))
        return algo.decrypt(token).decode('utf-8')


if __name__ == "__main__":
    a = Enc_Fernet()
    test = a.encrypt("user2", b"1234")
    print(test)
    c = a.decrypt(test, b"1234")
    print(c)
    print(type(c))

    a = Enc_Fernet()
    test = a.encrypt("user2", b"1234")
    print(test)
    c = a.decrypt(test, b"1234")
    print(c)
    print(type(c))
