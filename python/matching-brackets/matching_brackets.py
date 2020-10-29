def is_paired(input_string):
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    openers = []
    try:
        if input_string:
            for i in input_string:
                if i in '[{(':
                    openers.append(i)
                elif i in ']})':
                    last_bracket = openers.pop()
                    if not brackets[last_bracket] == i:
                        return  False
                else:
                    continue
            if len(openers) > 0:
                return False
            else: return True
        else:
            return True
    except IndexError:
        return False

