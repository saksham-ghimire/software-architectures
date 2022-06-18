
def binarySearch(array, toGuess) -> int:
    low = 0
    high = len(array) -1
    
    while low <= high:
        mid = (low+high) // 2
        if array[mid] == toGuess:
            return mid
        elif array[mid] > toGuess:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

def main():
    array = [1,2,3,4,5]
    print(binarySearch(array,1))


if __name__=="__main__":
    main()