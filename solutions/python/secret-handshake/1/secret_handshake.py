
ACTIONS = {
    "4": "wink",
    "3": "double blink",
    "2": "close your eyes",
    "1": "jump",
    "0": "Reverse"
}
def commands(binary_str):

    indices = [i for i, letra in enumerate(binary_str) if letra == "1"]
    actions_lst = [ACTIONS[str(i)]for i in indices[::-1]]
    if "Reverse" in actions_lst:
        actions_lst.remove("Reverse")
        return actions_lst[::-1]
    return actions_lst
