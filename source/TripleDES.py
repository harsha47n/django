import random

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import datetime

class TripleDES:

    def __init__(self,textData):
        self.textData=textData
        self.BS = DES3.block_size
        while len(self.textData) % 8 != 0:
            self.textData += b' '
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode()
        self.unpad = lambda s: s[0:-ord(s[-1])]
        self.key =b"1234567887654321"
        self.iv =b"1234567337654321"
    def getCipher(self):
        backend = default_backend()
        cipher = Cipher(algorithms.TripleDES(self.key), modes.CBC(self.iv), backend=backend)
        encryptor = cipher.encryptor()

        # Encrypt the message
        encrypted_message = encryptor.update(self.message) + encryptor.finalize()

        return base64.b64encode(encrypted_message)

    def toNormal(self):
        # Encrypted message to be decrypted (in base64 encoding)
        encrypted_message = base64.b64decode(self.textData)

        # Create a 3DES cipher object
        backend = default_backend()
        cipher = Cipher(algorithms.TripleDES(self.key), modes.CBC(self.iv), backend=backend)
        decryptor = cipher.decryptor()

        # Decrypt the message
        decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

        # Remove the padding from the decrypted message
        decrypted_message = decrypted_message.rstrip()
        return decrypted_message