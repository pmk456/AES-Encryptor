# Author: Patan Musthakheem
# Version: 1.8
# Licence: Apache 2.0
import os, sys
try:
    from Crypto.Cipher import AES
except ImportError:
    print("Pycryptodome Is Not Found On This Computer\n"
          "Please Install using pip [ pip install pycryptodome ]")
from hashlib import sha256

class AES_Encryption:
    """
     The Advanced Encryption Standard (AES) is a symmetric block cipher chosen by the U.S. government to
     protect classified information. AES is implemented in software and hardware throughout the world to
     encrypt sensitive data. It is essential for government computer security, cybersecurity and
     electronic data protection.
     Whats New:
     *Renamed the Current Class From AES To AES_Encryption
     * Added File Encryption
     * Few Bugs Fixed
     * Added Default IV [ Initializing Vector ]
     Please Refer To The https://github.com/pmk456/AES-Encryptor README.md
     For Perfectly Using This Package
    """
    def __init__(self, key, iv="THIS IS IV 45600", mode=AES.MODE_CBC):
        self.key = sha256(key.encode()).digest()
        self.IV = iv.encode()
        self.mode = mode

    def pad(self, msg):
        while len(msg) % 16 != 0:
            msg = msg + ' '
        return msg.encode()

    def encrypt(self, message):
        cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
        encrypted_msg = cipher.encrypt(self.pad(message))
        return encrypted_msg

    def decrypt(self, data):
        cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
        decrypted_data = cipher.decrypt(data)
        return decrypted_data.decode().rstrip()

    def file_encrypt(self, path):
        if not os.path.exists(path):
            print("Path not exists")
            sys.exit(1)
        try:
            cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
            with open(path) as file:
                data = self.pad(file.read())
                encrypted_data = cipher.encrypt(data)
            new = path + '.enc'
            with open(new, 'wb') as file:
                file.write(encrypted_data)
        except Exception:
            return '''Something Went Wrong During Encryption Of The File'''
        else:
            return '''File Successfully Encrypted With Given Key'''

    def file_decrypt(self, path):
        if not os.path.exists(path):
            print("Path not exists")
            sys.exit(1)
        try:
            cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
            with open(path, 'rb') as file:
                data = file.read()
                decrypted_data = cipher.decrypt(data)
            new = path.replace('.enc','')
            with open(new, 'wb') as file:
                file.write(decrypted_data)
        except Exception:
            return '''Something Went Wrong During Decryption Of The File, Please Cross Check Key And IV'''
        else:
            return '''File Successfully Decrypted With Given Key'''
