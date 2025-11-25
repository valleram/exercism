def find_anagrams(word, candidates):
    anagrams_list = [i for i in candidates if sorted(word.lower()) == sorted(i.lower()) and word.lower() != i.lower()]
    return anagrams_list

