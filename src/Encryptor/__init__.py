from Crypto.Cipher import AES as aes
from hashlib import sha256


class AES:
    def __init__(self, key, iv, mode=aes.MODE_CBC):
        self.key = sha256(key.encode()).digest()
        self.IV = iv.encode()
        self.mode = mode

    def pad(self, msg):
        while len(msg) % 16 != 0:
            msg = msg + ' '
        return msg.encode()

    def encrypt(self, message):
        enc = aes.new(key=self.key, mode=self.mode, iv=self.IV)
        encrypted_msg = enc.encrypt(self.pad(message))
        return encrypted_msg

    def decrypt(self, data):
        dec = aes.new(key=self.key, mode=self.mode, iv=self.IV)
        decrypted_data = dec.decrypt(data)
        return decrypted_data.decode().rstrip()
