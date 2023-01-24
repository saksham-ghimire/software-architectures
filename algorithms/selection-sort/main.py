from array import array


def selectionSort(array) -> list:
    # for sorting in descending order change min to max
    returnArr = []
    for i in range(len(array)):
        returnArr.append(min(array))
        array.remove(min(array))
    return returnArr
