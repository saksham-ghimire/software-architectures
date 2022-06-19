package main

import "fmt"

func getMinimum(arr []int) int {
	min := arr[0]
	minIndex := 0
	for i, v := range arr {
		if v < min {
			min = v
			minIndex = i
		}
	}
	return minIndex
}

func removeFromArray(arr []int, index int) []int {
	return append(arr[:index], arr[index+1:]...)
}

func selectionSort(arr []int) []int {
	returnArr := []int{}
	length := len(arr)
	for i := 0; i < length; i++ {
		minIndex := getMinimum(arr)
		returnArr = append(returnArr, arr[minIndex])
		arr = removeFromArray(arr, minIndex)
	}
	return returnArr
}

func main() {
	fmt.Println(selectionSort([]int{10, 5, 4, 3, 1, 2}))
}
