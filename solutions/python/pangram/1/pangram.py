#!/usr/bin/env python3
import string 

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    isalpha = [i.lower() for i in sentence if i.isalpha()]
    unique_values = "".join(sorted(set(isalpha)))
    return unique_values == alphabet
