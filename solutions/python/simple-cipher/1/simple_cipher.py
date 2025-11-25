import string
import math
from secrets import choice


class Cipher:
    ALPHABET = string.ascii_lowercase
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = "".join(choice(string.ascii_lowercase) for l in range(40))

    def get_key(self, text):
        if self.key:
            if len(self.key) < len(text):
                lens = math.ceil((len(text) // len(self.key)) + 1)
                temp = self.key * lens
                self.key = temp[0:len(text)]
            else:
                self.key = self.key[0:len(text)]
        return self.key

    def encode(self, text):
        self.key = self.get_key(text)
        if self.key:
            index_list = [Cipher.ALPHABET.index(i) for i in self.key]
            return "".join([Cipher.ALPHABET[(Cipher.ALPHABET.index(text[j]) + index_list[j]) % 26] for j in range(len(text))])
        else:
            return "".join([Cipher.ALPHABET[(Cipher.ALPHABET.index(i) + 3) % 26] for i in text if i in Cipher.ALPHABET])

    def decode(self, text):
        self.key = self.get_key(text)
        if self.key:
            index_list = [Cipher.ALPHABET.index(i) for i in self.key]
            return "".join([Cipher.ALPHABET[(Cipher.ALPHABET.index(text[j]) - index_list[j]) % 26] for j in range(len(text))])
        else:
            return "".join([Cipher.ALPHABET[(Cipher.ALPHABET.index(i) + 3) % 26] for i in text if i in Cipher.ALPHABET])
