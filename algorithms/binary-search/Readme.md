# Binary Search

An search algorithm that works on **sorted** list and returns index of element meant to be searched.

* Time Complexity =>  O(logN) *Where n is length of array*

## Flowchart
<!-- picture here -->
![flowchart](https://github.com/saksham-ghimire/software-architectures/blob/main/algorithms/binary-search/binary_search.jpg)

## Pseudocode
**Note : Pseudocode resembles python syntaxing because of convenience**
```
array = array.sort() #must be sorted
element = <elemnent to be found>

# enclose this in function
leftHandLimit = 0
rightHandLimit = len(array) - 1 # because i am checking element and element index is always one less than len

while leftHandLimit <= rightHandLimit: #sometime they might be on same index where element lies so equal condition
			mid = (leftHandLimit + rightHandLimit) // 2
			if array[mid] == element:
							print(mid)
			elif array[mid] < element: 
							leftHandLimit = mid + 1
			else:
							rightHandLimit = mid -1
```
