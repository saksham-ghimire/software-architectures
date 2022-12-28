# Quick Sort

An convenient sorting algorithm that uses recursion to sort element of list/array.

* Time Complexity => O(n<sup>2</sup>) *Where n is number of element in array*

## Flowchart
<!-- picture here -->

## Pseudocode
**Note : Pseudocode resembles python syntaxing because of convenience**
```
Recursion


# enclose this on function namely quicksort
if len(array) < 2: # base case to break recursion
	return array
pivot = <any element in array> # safe to take 0 index
lessThanpivot = [i for i in array if i < pivot]
greaterThanpivot = [i for i in array if i > pivot]
return quicksort(lessThanpivot) + pivot + quicksort(greaterThanPivot)
```