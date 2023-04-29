import datetime
import random

import Cryptodome.Cipher.DES as des
from Cryptodome.Random import get_random_bytes

class DES:

    def __init__(self,text_data):
        self.input_data=text_data

    def getCipher(self):
        key = b'-8B key-'
        cipher = des.new(key, des.MODE_OFB)
        msg = cipher.iv + cipher.encrypt(self.input_data.encode())
        return msg
    def toNormal(self):
        key = b'-8B key-'
        cipher = des.new(key, des.MODE_OFB)
        msg = cipher.iv + cipher.decrypt(self.input_data.encode())
        return msg


    #     generated_key = self.getKey()
    #     # generated_key= get_random_bytes(16)
    #     print(generated_key)
    #     ciphertext = des.new(generated_key,des.MODE_EAX)
    #     converted_cipher,tag = ciphertext.encrypt_and_digest(self.input_data.encode())
    #
    #     return r'{0}'.format(converted_cipher)
    #
    #     # pass
    #
    # def getKey(self):
    #     key_number = random.Random()
    #     return key_number.randint(10**16,int("9"*17)).to_bytes(16,byteorder="big")
