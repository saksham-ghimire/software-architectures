package main

import "fmt"

func in(str string, array []string) bool {
	for _, v := range array {
		if v == str {
			return true
		}
	}
	return false
}

func breadth_first(graph map[string][]string, element string, start string) string {
	queue := []string{}
	processed := []string{}
	for _, v := range graph[start] {
		queue = append(queue, v)
	}
	for len(queue) > 0 {
		if in(queue[0], processed) {
			continue
		}
		if queue[0] == element {
			return "Found"
		} else {
			for _, v := range graph[queue[0]] {
				queue = append(queue, v)
			}

		}
		processed = append(processed, queue[0])
		queue = queue[1:]
	}
	return "Not Found"
}

func main() {

	graph := map[string][]string{"start": {"a", "b", "c"}, "a": {"e", "f"}, "b": {"a", "g", "h"}}
	fmt.Println(breadth_first(graph, "g", "a"))
}
