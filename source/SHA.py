import hashlib

class SHA:

    def __init__(self, text_data):
        self.input_data = text_data

    def getCipher(self):
        result = hashlib.sha256(self.input_data.encode())
        print(result.hexdigest())
