package main

import (
	"fmt"
)

func quicksort(array []int) []int {

	leftArray := []int{}
	rightArray := []int{}
	// returnArray := []int{}
	// handling the base case
	if len(array) < 2 {
		return array
	}
	// choose a random pivot element
	pivot := array[0]
	for _, v := range array {
		if v < pivot {
			leftArray = append(leftArray, v)
		} else if v > pivot {
			rightArray = append(rightArray, v)
		}
	}
	left, right := quicksort(leftArray), quicksort(rightArray)
	left = append(left, pivot)
	left = append(left, right...)
	return left

}
func main() {
	array := []int{55, 45, 83, 2, 1}
	fmt.Println(quicksort(array))
}
