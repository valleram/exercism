def find(arr, search_element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == search_element:
            return mid
        elif arr[mid] < search_element:
            low = mid + 1
        else:
            high = mid - 1

    # Raise the error expected by your unit tests
    raise ValueError("value not in array")


if __name__ == '__main__':
    find([1, 3, 4, 6, 8, 9, 11], 6)
    find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21)
    find([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)

