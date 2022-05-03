package main

import (
	"pubsub/manager"
)

// Just a general main function that calls publisher and subscriber as needed.
func main() {
	pub := &manager.Publisher{
		Subscribers:       make(map[string]chan string),
		SubscribersErrors: make(map[string]chan error),
		Filepath:          "./testlog.txt",
	}

	go pub.StartPublisher()

	go pub.StartSubscriber("s1")
	go pub.StartSubscriber("s2")
	select {}
}
