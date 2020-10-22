import re


def abbreviate(words):
    word_list = re.findall(r"[HA-Za-z']*", words)
    return "".join([i[0].upper() for i in word_list if i.isalpha()])
