# AES Encryptor
## What's New
```
* Added File Encryption
* Few Bugs Fixed
* Added Default IV [ Initializing Vector ]
```
## Installation
```
pip install AES-Encryptor
```
## Using git
```
git clone https://github.com/pmk456/AES-Encryptor
cd AES-Encryptor
python setup.py install
```
## Usage
### Encrypt File
```
from Encryptor import AES_Encryption
cipher = AES_Encryption(key='keytouse', iv='this is iv 45611')
print(cipher.file_encrypt(path))
### OUTPUT
File Successfully Encrypted With Given Key
In Case Of any exception:
Something Went Wrong During Encryption Of The File
path.enc // THIS IS ENCRYPTED FILE WHICH IS SAVED IN THE GIVEN PATH
```
### Decrypt File
```
from Encryptor import AES_Encryption
cipher = AES_Encryption(key='keytouse', iv='This is iv 45611')
print(cipher.file_decrypt(path))
### OUTPUT
File Successfully Decrypted With Given Key
In Case Of any exception:
Something Went Wrong During Decryption Of The File
If nothing went wrong:
path // THIS IS DECRYPTED FILE WHICH IS SAVED IN THE GIVEN PATH
```
### Encrypt String
```
from Encryptor import AES_Encryption
cipher = AES_Encryption(key='keytouse', iv='this is iv 45611')
cipher.encrypt("Hello")
### OUTPUT
b'}%\x99\x00b3\xb0?\xe5\t\x07wc\xa8\xc6\x8d'
```
### Decrypt String
```
from Encryptor import AES_Encryption
cipher = AES_Encryption(key='keytouse', iv='this is iv 45611')
cipher.decrypt(b'}%\x99\x00b3\xb0?\xe5\t\x07wc\xa8\xc6\x8d')
### OUTPUT
'Hello'
```
### About
```
Hi, I Am Patan Musthakheem I Am The Author Of This Package.
I Created This Tool For Beginners Who Want to encrypt their string or file
using any encryption but they dont know how to use it because 
for beginners it is bit of difficult for using Encryption like AES from scratch.
I Faced Many issues when learning how to encrypt strings and files in python when
i am beginner so i decided to create a very simple tool which will encrypt strings and files
in one line of code.
That day has came, Now you can encrypt and decrypt strings in one line of code.
Thanks To Me.
```
