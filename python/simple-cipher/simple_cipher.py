import string

class Cipher:
    def __init__(self, key=None):
        self.key = key

    def encode(self, text):
        alphabet = string.ascii_lowercase
        data = []
        for i in text.lower():
            if i in alphabet:
                data.append(alphabet[(alphabet.index(i) + 3) % 26])
        output = ''.join(data)
        return output

    def decode(self, text):
        alphabet = string.ascii_lowercase
        data = []
        for i in text.lower():
            if i in alphabet:
                data.append(alphabet[(alphabet.index(i) - 3) % 26])
        output = ''.join(data)
        return output
