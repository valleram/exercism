def steps(number):
    if number <= 0:
        raise ValueError("Should be a positive integer")
    else:
        step = 0
        while number > 1:
            number = number/2 if number % 2 == 0 else (3*number) + 1
            step += 1
        return step