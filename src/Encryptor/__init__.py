# Author: Patan Musthakheem
# Version: 2.0
# Licence: Apache 2.0
#  Please Refer To The https://github.com/pmk456/AES-Encryptor README.md
# Whats New:
# * Renamed the Main Class From AES To AES_Encryption
# * Added File Encryption
# * Many Bugs Fixed
# * Added Default IV [ Initializing Vector ]
# * Many Exceptions Are Catched Now Under Try Except Blocks
try:
    from Crypto.Cipher import AES
except ImportError:
    print("Pycryptodome Is Not Found On This Computer\n"
          "Please Install using pip [ pip install pycryptodome ]")
    sys.exit(1)
import os, sys
from hashlib import sha256


class AES_Encryption:
    """
     The Advanced Encryption Standard (AES) is a symmetric block cipher chosen by the U.S. government to
     protect classified information. AES is implemented in software and hardware throughout the world to
     encrypt sensitive data. It is essential for government computer security, cybersecurity and
     electronic data protection.
     Please Refer To The https://github.com/pmk456/AES-Encryptor README.md
     For Perfectly Using This Package
    """

    def __init__(self, key, iv="THIS IS IV 45600", mode=AES.MODE_CBC):
        """
        Constructor For This Class
        :param key: Key Must be string which will used to encrypt the strings or files
        :param iv: initializing vector which is used to randomize the encrypted data, This Must Be 16 Bytes Long, default=THIS IS IV 45600
        :param mode: mode for encrytping data, default=MODE_CBC
        """
        if len(iv) < 16 or len(iv) > 16:
            print("Incorrect IV Length (It Must Be 16 Bytes Long)")
            sys.exit(1)
        if not isinstance(key, str):
            print("Key Must Be String")
            sys.exit(1)
        if not isinstance(iv, str):
            print("IV Must Be String")
            sys.exit(1)
        self.key = sha256(key.encode()).digest()
        self.IV = iv.encode()
        self.mode = mode

    def pad(self, data):
        """
        This Function Is Created For Padding Messages into multiple of 16
        :param data: Data which is not a multiple of 16
        :return: returns encoded string and make it multiple of 16
        """
        while len(data) % 16 != 0:
            data = data + ' '
        return data.encode()

    def encrypt(self, message):
        """
        Used To Encrypt Strings
        :param message: String Which Want To Be Encrypted
        :return: Encrypted Data Of The String Which Will Be In Bytes
        """
        if not isinstance(message, str):
            return "Encrypt Function Only Accepts Strings"
        try:
            cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
            encrypted_msg = cipher.encrypt(self.pad(message))
        except Exception:
            return "Failed To Encrypt String"
        else:
            return encrypted_msg

    def decrypt(self, data):
        """
        Used To Decrypt Data Given
        :param data: data which is encrypted with the same given key
        :return: Plain string
        """
        if not isinstance(data, bytes):
            return "Decrypt Function Only Accepts Bytes"
        try:
            cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
            decrypted_data = cipher.decrypt(data)
        except Exception:
            return "Failed To Decrypt String Please Check The Key And IV\n" \
                   "Please Re-Verify The Given Data, Data May Be Changed\n" \
                   "Data Bytes Must Be Multiple Of 16"
        else:
            return decrypted_data.decode().rstrip()

    def file_encrypt(self, path):
        """
        Used To Encrypt The File
        :param path: Path Of The File Note: If You are using windows please put [ \\ ]
        :return: Encrypted File In the same given path with the same name but with extension .enc
        """
        if not os.path.exists(path):
            print("Path not exists")
            if sys.platform == 'win32':
                print(r"Note: If You are using windows please put[ \\ ]\n"
                      r"Example: C:\\Windows\\System32\\File.txt")
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
        """
        Used To Decrypt The File
        :param path: Path Of The File Note: If You are using windows please put [ \\ ] Example: C:\\Windows\\System32\\File.txt
        :return: Decrypted File With Removed .enc extension In the same given path
        """
        if not isinstance(path, str):
            print("Path Must Be String")
        if not os.path.exists(path):
            print("Path not exists")
            if sys.platform == 'win32':
                print(r"Note: If You are using windows please put[ \\ ]\n"
                      r"Example: C:\\Windows\\System32\\File.txt")
            sys.exit(1)
        try:
            cipher = AES.new(key=self.key, mode=self.mode, iv=self.IV)
            with open(path, 'rb') as file:
                data = file.read()
                decrypted_data = cipher.decrypt(data)
            new = path.replace('.enc', '')
            with open(new, 'wb') as file:
                file.write(decrypted_data)
        except Exception:
            return '''Something Went Wrong During Decryption Of The File, Please Cross Check Key And IV'''
        else:
            return '''File Successfully Decrypted With Given Key'''
