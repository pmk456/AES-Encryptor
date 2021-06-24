# AES Encryptor
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
### Encrypt String
```
from Encryptor import AES
enc = AES(key='keytouse', iv='this is iv 45611')
enc.encrypt("Hello")
### OUTPUT
b'}%\x99\x00b3\xb0?\xe5\t\x07wc\xa8\xc6\x8d'
```
### Decrypt String
```
from Encryptor import AES
dec = AES(key='keytouse', iv='this is iv 45611')
dec.decrypt(b'}%\x99\x00b3\xb0?\xe5\t\x07wc\xa8\xc6\x8d')
### OUTPUT
'Hello'
```