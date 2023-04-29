import random

import Cryptodome.Cipher.AES as aes
from Cryptodome.Random import get_random_bytes

class AES:

    def __init__(self,text_data):
        self.input_data=text_data

    def getCipher(self):
        generated_key = self.getKey()
        # generated_key= get_random_bytes(16)
        print(generated_key)
        ciphertext = aes.new(generated_key,aes.MODE_EAX)
        converted_cipher,tag = ciphertext.encrypt_and_digest(self.input_data.encode())

        return r'{0}'.format(converted_cipher)

    def toNormal(self):
        generated_key = self.getKey()
        # generated_key= get_random_bytes(16)
        print(generated_key)
        ciphertext = aes.new(generated_key, aes.MODE_EAX)
        converted_cipher, tag = ciphertext.decrypt_and_verify(self.input_data.encode())

        return r'{0}'.format(converted_cipher)

        # pass

    def getKey(self):
        key_number = random.Random()
        return key_number.randint(10**16,int("9"*17)).to_bytes(16,byteorder="big")


#
# from Cryptodome.Cipher import AES
# from Cryptodome.Random import get_random_bytes
#
# data=b"SECRETDATA"
# key = get_random_bytes(16) #must be 16, 24 or 32 bytes long
# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext, tag = cipher.encrypt_and_digest(data)
#
# file_out = open("encryptedfile.bin", "wb")
# [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
# file_out.close()