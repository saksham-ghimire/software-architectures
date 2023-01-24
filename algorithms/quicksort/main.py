def quicksort(arr):
    if len(arr) < 2:
        return arr
    # select random pivot element
    pivot = arr[0]
    # sort every less element to left
    left = [i for i in arr if i < pivot]
    # sort every greater element to right
    right = [i for i in arr if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)
