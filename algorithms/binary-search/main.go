package main

import "fmt"

func binarySearch(arr []int, toFind int) int {
	lowPoint := 0
	highPoint := len(arr) - 1
	var mid int
	for {
		if lowPoint > highPoint {
			mid = -1
			break
		}
		mid = (lowPoint + highPoint) / 2
		if arr[mid] == toFind {
			break
		} else if arr[mid] > toFind {
			highPoint = mid - 1
		} else {
			lowPoint = mid + 1
		}

	}
	return mid
}

func main() {
	// var sortedArray []int
	sortedArray := []int{2, 3, 8, 9, 12, 25, 84, 92, 100, 125, 185}
	fmt.Println(binarySearch(sortedArray, 185))

}
