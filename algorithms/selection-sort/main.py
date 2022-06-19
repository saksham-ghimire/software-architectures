
from array import array

def selectionSort(array) -> list:
    # for sorting in descending order change min to max
    returnArr = []
    for i in range(len(array)):
        returnArr.append(min(array))
        array.remove(min(array))
    return returnArr

def main():
    array = [10,80,20,40,70]
    print(selectionSort(array))


if __name__=="__main__":
    main()