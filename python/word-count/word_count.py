#!/usr/bin/env python3
import re

def count_words(sentence):
    word_list = re.findall(r"[a-z\d]+(?:'[a-z\d])?", sentence.lower())
    counting_words = {i: word_list.count(i) for i in word_list}
    return counting_words
