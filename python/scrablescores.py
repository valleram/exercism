scores = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "I"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def scores(word):
    return sum([i for l in word.upper() for i in scores if l in scores[i]])