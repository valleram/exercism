import string
import math

class Cipher:
    def __init__(self, key=None):
        self.key = key

    def encode(self, text):
        alphabet = string.ascii_lowercase
        if self.key:
            if len(self.key) < len(text):
                lens = math.ceil((len(text) // len(self.key)) + 1)
                temp = self.key * lens
                self.key = temp[0:len(text)]
            do = [alphabet.index(i) for i in self.key]
            el = [alphabet[(alphabet.index(text[j]) + do[j]) % 26] for j in range(len(text))]
            return "".join(el)
        else:
            data = [alphabet[(alphabet.index(i) + 3) % 26] for i in text if i in alphabet]
            return "".join(data)


    def decode(self, text):
        alphabet = string.ascii_lowercase
        data = []
        for i in text.lower():
            if i in alphabet:
                data.append(alphabet[(alphabet.index(i) - 3) % 26])
        output = ''.join(data)
        return output
