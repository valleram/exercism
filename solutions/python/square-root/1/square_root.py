def square_root(number):
    digit_array = list(range(1, number))
    low = 0
    high = len(digit_array) - 1
    if number == 1 : return  1
    while low <= high:
        mid = low + (high - low) // 2
        square= (mid * mid)
        if square == number:
            return mid
        elif square < number:
            low = mid + 1
        else:
            high = mid - 1
