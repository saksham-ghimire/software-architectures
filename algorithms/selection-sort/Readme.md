# Selection Sort

Generally considered as slow and easy sorting algorithm, easy to implement and undestand.

* Time Complexity => O(n<sup>2</sup>) *Where n is number of element in array*

## Flowchart
<!-- picture here -->

## Pseudocode
**Note : Pseudocode resembles python syntaxing because of convenience**
```
array = <array to sort>

# enclose this on function
returnarray = []
for i in range(0,len(array)):
		returnarray.append(min(array))
		array.remove(min(array)
return returnarray
```