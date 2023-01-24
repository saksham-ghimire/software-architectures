def binarySearch(array, toGuess) -> int:
    if array != sorted(array):
        return -1

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == toGuess:
            return mid
        elif array[mid] > toGuess:
            high = mid - 1
        else:
            low = mid + 1

    return -1
